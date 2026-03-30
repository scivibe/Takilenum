from Glyph import write_takilenum

'''
A quick note on the available letters
First off, there is no c. It either gets absorbed into the ch character, or is replaced with a k
There are special characters for ng, sh, and zh
There are also special characters for th and dh, if you want to differentiate th is the th sound as in "thistle" and dh is the th sound as in "this"
Vowels are a, e, i, o, u, and y
If you enable doLongVowels, the long vowels would be written as aa, ee, ii, oo, uu, and yy
Also there's no puncuation or other special characters
Otherwise, here's the list of all letters available. If you use one that hasn't been created, it'll yell at you. 
t
d
p
b
k
g
q
l
r
m
n
ng
f
v
th
dh
s
z
sh
zh
j
w
x
h
'''

write_takilenum("The quick brown fox jumps over the lazy dog", outputFile="glyph1.png", maxGlyphPerRow=4, doLongVowels=False)


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.asarray(Image.open("glyph1.png"))
plt.figure()
plt.imshow(img)
plt.show()
