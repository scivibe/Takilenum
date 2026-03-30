import cairo
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from Vowels import *
from Letters import *

class Glyph:
    def __init__(self):
        self.slots = [{"cons": None, "vowel": None},
                      {"cons": None, "vowel": None},
                      {"cons": None, "vowel": None}]
        
    def set_slot(self, index, consonant=None, vowel=None):
        self.slots[index]["cons"] = consonant
        self.slots[index]["vowel"] = vowel

    def is_full(self):
        return all(slot["cons"] is not None or slot["vowel"] is not None for slot in self.slots)


def preprocessString(inputString, doLongVowels=False):
    inputString = inputString.replace("ng", "N")
    inputString = inputString.replace("sh", "S")
    inputString = inputString.replace("zh", "Z")
    inputString = inputString.replace("th", "T")
    inputString = inputString.replace("dh", "D")

    if (doLongVowels):
        inputString = inputString.replace("aa", "A")
        inputString = inputString.replace("ee", "E")
        inputString = inputString.replace("ii", "I")
        inputString = inputString.replace("oo", "O")
        inputString = inputString.replace("uu", "U")
        inputString = inputString.replace("yy", "Y")

    return inputString

def stringToGlyphs(glyphStr):
    vowels = {"a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"}
    glyphs = []
    current = Glyph()
    slotIndex = 0

    i = 0
    while i < len(glyphStr):
        char = glyphStr[i]

        if char in vowels:
            current.set_slot(slotIndex, vowel=char)
            slotIndex += 1
        else:
            current.set_slot(slotIndex, consonant=char)
            if (i + 1 < len(glyphStr) and glyphStr[i + 1] in vowels):
                i += 1
                current.set_slot(slotIndex, consonant=char, vowel=glyphStr[i])

            slotIndex += 1

        if slotIndex == 3:
            glyphs.append(current)
            current = Glyph()
            slotIndex = 0
        i += 1

    if slotIndex > 0:
        glyphs.append(current)

    return glyphs



def write_takilenum(inputString, outputFile="glyph.png", maxGlyphPerRow=10, glyphSize=500, backgroundColor=(1.0, 1.0, 1.0), writingColor=(0.0, 0.0, 0.0), padding=50, doLongVowels=False):
    glyphStr = preprocessString(inputString.lower(), doLongVowels=doLongVowels)
    print(f"string processed into: {glyphStr}")
    glyphs = stringToGlyphs(glyphStr)

    print(f"{len(glyphs)} glyphs will be written")

    maxGlyphPerRow = min(maxGlyphPerRow, len(glyphs))
    
    if maxGlyphPerRow % 2 != 0:
        maxGlyphPerRow += 1  # enforce even

    row_length = maxGlyphPerRow

    colSize = int(np.ceil(len(glyphs) / row_length))
    rowSize = row_length

    print(f"glyph grid will be ({rowSize}, {colSize})")

    s = glyphSize
    h = (np.sqrt(3) / 2) * s
    
    canvasWidth = (rowSize) * (s/2) + s + 2*padding
    canvasHeight = colSize*h + 2*padding

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(canvasWidth), int(canvasHeight))
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(backgroundColor[0], backgroundColor[1], backgroundColor[2])
    ctx.rectangle(0, 0, canvasWidth, canvasHeight)
    ctx.fill()

    ctx.set_source_rgb(writingColor[0], writingColor[1], writingColor[2])
    ctx.set_line_width(4)
    ctx.set_line_join(cairo.LineJoin.ROUND)
    
    

    glyphX = (s) + padding
    glyphY = (h/2) + padding

    glyphSign = -1
    glyphDir = 1

    index_in_row = 0
    for i, glyph in enumerate(glyphs):

        #Start with enclosing triangle
        c1x = glyphX - s/2
        c3x = glyphX + s/2
        c2x = glyphX
        c1y = glyphY + (glyphSign*h/2)
        c3y = glyphY + (glyphSign*h/2)
        c2y = glyphY - (glyphSign*h/2)

        centroidX = glyphX
        centroidY = glyphY + (glyphSign * h/6)

        ctx.move_to(c1x, c1y)
        ctx.line_to(c2x, c2y)
        ctx.line_to(c3x, c3y)
        ctx.close_path()
        ctx.stroke()
        
        #Draw glyph spokes
        ctx.move_to(centroidX, centroidY)
        ctx.line_to(c1x, c1y)
        ctx.stroke()
        ctx.move_to(centroidX, centroidY)
        ctx.line_to(c2x, c2y)
        ctx.stroke()
        ctx.move_to(centroidX, centroidY)
        ctx.line_to(c3x, c3y)
        ctx.stroke()

        #Draw starting line
        dx = c1x - centroidX
        dy = c1y - centroidY
        ang = np.arctan2(dy, dx)
        l = np.sqrt(dx**2 + dy**2)

        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.48 * l, 0.3 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.restore()


        #Draw consonants and vowel for slot 1
        draw_letter(glyph.slots[0]["cons"], ctx, centroidX, centroidY, c1x, c1y, glyphSize)
        draw_vowel(glyph.slots[0]["vowel"], ctx, centroidX, centroidY, c1x, c1y, glyphSize)
        #Draw consonants and vowel for slot 2
        draw_letter(glyph.slots[1]["cons"], ctx, centroidX, centroidY, c2x, c2y, glyphSize)
        draw_vowel(glyph.slots[1]["vowel"], ctx, centroidX, centroidY, c2x, c2y, glyphSize)
        #Draw consonants and vowel for slot 3
        draw_letter(glyph.slots[2]["cons"], ctx, centroidX, centroidY, c3x, c3y, glyphSize)
        draw_vowel(glyph.slots[2]["vowel"], ctx, centroidX, centroidY, c3x, c3y, glyphSize)

        #Directional bars
        if i < len(glyphs):
            nextX = glyphX + glyphDir * (s/2)
            nextY = glyphY
            nextSign = -glyphSign

            if ((i + 1) % maxGlyphPerRow == 0):
                nextY = glyphY + h
                nextSign = -glyphSign

            nextCentroidX = nextX
            nextCentroidY = nextY + (nextSign * h/6)

            dxn = nextCentroidX - centroidX
            dyn = nextCentroidY - centroidY
            ang_to_next = np.arctan2(dyn, dxn)

            edges = [((c1x + c2x)/2, (c1y + c2y)/2),
                        ((c2x + c3x)/2, (c2y + c3y)/2),
                        ((c3x + c1x)/2, (c3y + c1y)/2)]

            bestEdge = None
            bestDot = -1e9

            for ex, ey in edges:
                vx = ex - centroidX
                vy = ey - centroidY
                l = np.sqrt(vx**2 + vy**2)
                vx /= l
                vy /= l

                dot = vx * np.cos(ang_to_next) + vy * np.sin(ang_to_next)

                if dot > bestDot:
                    bestDot = dot
                    bestEdge = (ex, ey)

            ctx.save()
            ctx.translate(bestEdge[0], bestEdge[1])
            dx = centroidX - bestEdge[0]
            dy = centroidY - bestEdge[1]
            newAng = np.arctan2(dy, dx)
            ctx.rotate(newAng)
            ctx.move_to(0.025 * glyphSize, 0.05 * glyphSize)
            ctx.line_to(-0.025 * glyphSize, 0.05 * glyphSize)
            ctx.stroke()
            ctx.move_to(0.025 * glyphSize, -0.05 * glyphSize)
            ctx.line_to(-0.025 * glyphSize, -0.05 * glyphSize)
            ctx.stroke()
            ctx.restore()

        glyphSign *= -1
        glyphX += glyphDir * (s/2)
        index_in_row += 1

        if index_in_row == row_length:
            index_in_row = 0
            glyphY += h
            glyphDir *= -1
            glyphX += glyphDir * (s/2)

    surface.write_to_png(outputFile)



write_takilenum("this is a test of takiilenum script in english mode", outputFile="glyph1.png", maxGlyphPerRow=6, doLongVowels=False)

img = np.asarray(Image.open("glyph1.png"))
plt.figure()
plt.imshow(img)
plt.show()

