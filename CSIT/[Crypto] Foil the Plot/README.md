6 SOLVES 989 POINTS

# DESCRIPTION
Author: Chun

Difficulty: Hard

APOCALYPSE activated a sleeper cell for a suicide bombing but the target location is not known.....

Experts from CSIT have discovered the attacker-controlled server that was used to send a secret message to the sleeper cell. The server is protected with a password that is at least 40 chars long! The server does not store the password but to our good fortune, a weakness has been discovered in the way it performs the authentication.

It validates the password by performing the following steps:
Split the 40 char password into 2 equally-sized segments
Check that the segments are not identical
Generate the SHA-256 digests of both segments
Check that the last 5 bytes of both digests are identical
Your task is to gain authentication to the server, decipher the message and determine the target location before it's too late!

Challenge Access:
http://challenges1.whitehacks.xyz:28800
http://challenges2.whitehacks.xyz:28800


Enter the flag as WH2022{ID_postal code}

Eg. WH2022{s@m_pl3_123456}
---
this is bruteforcing but our crypto man was lazy to script. lost points lor