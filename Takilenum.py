from Glyph import write_takilenum


write_takilenum("kakakakakakaqaqaqaqaqaqagagagagagaga", outputFile="glyph1.png")

#write_takilenum("this is a test of takiilenum script in english mode", outputFile="glyph1.png", maxGlyphPerRow=6, doLongVowels=False)
#write_takilenum("this is a test of takiilenum script in takiilenum mode and also bigger and longer script giving more and more wrapping", outputFile="glyph2.png", maxGlyphPerRow=4, glyphSize=500, doLongVowels=True)


#Optional code to immediately display results instead of having to dig through folder
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.asarray(Image.open("glyph1.png"))
plt.figure()
plt.imshow(img)
plt.show()

#img = np.asarray(Image.open("glyph2.png"))
#plt.figure()
#plt.imshow(img)
#plt.show()

