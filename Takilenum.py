from Glyph import write_takilenum


write_takilenum("this is a test of takiilenum script in english mode", outputFile="glyph1.png", maxGlyphPerRow=6, doLongVowels=False)
write_takilenum("this is a test of takiilenum script in takiilenum mode and also bigger and longer script giving more and more wrapping", outputFile="glyph2.png", maxGlyphPerRow=4, glyphSize=500, doLongVowels=True)
write_takilenum("and this here is one last sentence to just show off the rest of the features ive got notice how there is no puncuation or apostrophes or shit like that", outputFile="glyph3.png", maxGlyphPerRow=10, glyphSize=250, doLongVowels=True, writingColor=(1.0, 0.0, 0.0), backgroundColor=(0.0, 0.0, 1.0), padding=10)


#Optional code to immediately display results instead of having to dig through folder
'''
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.asarray(Image.open("glyph1.png"))
plt.figure()
plt.imshow(img)
plt.show()

img = np.asarray(Image.open("glyph2.png"))
plt.figure()
plt.imshow(img)
plt.show()

img = np.asarray(Image.open("glyph3.png"))
plt.figure()
plt.imshow(img)
plt.show()
'''
