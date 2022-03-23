31 SOLVES 886 POINTS

DESCRIPTION
Author: xbowery

Difficulty: Easy

We know the infamous murderer Jack the Ripper from the 1880s, but are you aware that Jack had a twin brother, John, who also turned out to be his fiercest rival as they compete for fame?

John was last seen competing to see who could outsing Freddie Mercury in a soprano contest out in the public before he went hiding. He left a file containing a note about his darkest secret. Are you able to retrieve it?

---
# SOL
use the zip2john utility to extract the hash and run john with the rockyou.txt wordlist. jumbo john didn't work on my local environment so I ran it in a kali vm.
- this will give you the password as `myroomisblue`.
- using the password on the text file in the zip will give you flag `WH2022{W3_wi11_w3_w1ll_r0cky0u}`