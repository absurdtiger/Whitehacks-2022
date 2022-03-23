40 SOLVES 767 POINTS

DESCRIPTION
Author: xbowery

Difficulty: Easy

The mischievous aliens have dumped our lovely poster into the trash can, maybe you can walk through it to find some treasure?

---
# sol
- "walking through" indicates that you need to use binwalk
- extract the files in the pdf with `binwalk --dd=.* treasure.pdf`
- as we can see from the [extracted folder](./_treasure.pdf.extracted) and from running `file *` there are a few image files
- from my ubuntu wsl I ran `wslview file` to view each image and on the second image, [460](./_treasure.pdf.extracted/460.jpg) there's our flag.
`WH2022{m0r3th4n_m33t5_th3_3y3}`
