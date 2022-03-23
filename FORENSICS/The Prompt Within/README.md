38 SOLVES 799 POINTS

# DESCRIPTION
Author: iPhantasmic (Justin)

Difficulty: Easy

The aliens that invaded Earth have gotten a hold of the Whitehacks console and are attempting to communicate back to base! Thankfully, we caught them red-handed... Can you figure out what they have sent back to the Mothership?

# Solution
(the file is too large to attach.)

basically, you need to open the file in volatility.
- find the recommended profile with `vol.py memdump.mem imageinfo`
- use the profile in further commands
- `vol.py memdump.mem --profile=<profile> consoles`
- the flag will show up