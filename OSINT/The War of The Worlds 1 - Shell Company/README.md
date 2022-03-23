20 SOLVES 957 POINTS

# DESCRIPTION
Author: Hartanto

Difficulty: Easy

Anyway, before Lewis disappeared, he got alerted that some company is providing CTFSolver-as-a-Service. I mean, what kind of cruel human being would take away all the F(un) from CTF, and we surely don't want anyone to be using their service for our upcoming CTF.

Check this out: https://github.com/CTFSolverService

In any case, find out who owns the company. Maybe they have something to do with Lewis's disappearance.

Flag is in the format: WH2022{FullNameWithNoSpaceAndInitialCaps}
# Solution
- on the github page there is some strange hex string
- search for types of keys
- learn that GPG and PGP are keys
- be very confused while you ignore this fact and continue thinking the string is part of SSH and pester admins for 5 tickets
- learn that you can search the key fingerprint on the internet and get the full key
- remember that GPG and PGP are keys
- search PGP lookup
- <https://pgp.mit.edu/>
- panic during your resolve because the database is down and the admins might not believe you
- breathe when the server works again
- briefly wonder if you DDOSed the server with one lookup
- anyway, `WH2022{NgEngSiangKurt}`