import numpy as np

def draw_vowel(vowel, ctx, centroidX, centroidY, cornerX, cornerY, glyphSize):
    dx = cornerX - centroidX 
    dy = cornerY - centroidY
    l = np.sqrt(dx**2 + dy**2)
    ang = np.arctan2(dy, dx)

    if vowel == "a":
        print("a")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.56 * l, 0.1 * l)
        ctx.line_to(0.55 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.56 * l, -0.1 * l)
        ctx.line_to(0.55 * l, -0.1 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "A":
        print("aa")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.46 * l, 0.1 * l)
        ctx.line_to(0.45 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.46 * l, -0.1 * l)
        ctx.line_to(0.45 * l, -0.1 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "e":
        print("e")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.55 * l, 0.1 * l)
        ctx.line_to(0.55 * l, 0.15 * l)
        ctx.stroke()

        ctx.move_to(0.55 * l, -0.1 * l)
        ctx.line_to(0.55 * l, -0.15 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "E":
        print("ee")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.45 * l, 0.1 * l)
        ctx.line_to(0.45 * l, 0.15 * l)
        ctx.stroke()

        ctx.move_to(0.45 * l, -0.1 * l)
        ctx.line_to(0.45 * l, -0.15 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "i":
        print("i")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.53 * l, 0.1 * l)
        ctx.line_to(0.55 * l, 0.15 * l)
        ctx.line_to(0.58 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.53 * l, -0.1 * l)
        ctx.line_to(0.55 * l, -0.15 * l)
        ctx.line_to(0.58 * l, -0.1 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "I":
        print("ii")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.43 * l, 0.1 * l)
        ctx.line_to(0.45 * l, 0.15 * l)
        ctx.line_to(0.48 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.43 * l, -0.1 * l)
        ctx.line_to(0.45 * l, -0.15 * l)
        ctx.line_to(0.48 * l, -0.1 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "o":
        print("o")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.53 * l, 0.07 * l)
        ctx.line_to(0.58 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.53 * l, -0.07 * l)
        ctx.line_to(0.58 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "O":
        print("oo")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.43 * l, 0.07 * l)
        ctx.line_to(0.48 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.43 * l, -0.07 * l)
        ctx.line_to(0.48 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "u":
        print("u")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.58 * l, 0.1 * l)
        ctx.line_to(0.58 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.58 * l, -0.1 * l)
        ctx.line_to(0.58 * l, -0.13 * l)
        ctx.stroke()

        ctx.move_to(0.55 * l, 0.1 * l)
        ctx.line_to(0.55 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.55 * l, -0.1 * l)
        ctx.line_to(0.55 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "U":
        print("uu")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.48 * l, 0.1 * l)
        ctx.line_to(0.48 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.48 * l, -0.1 * l)
        ctx.line_to(0.48 * l, -0.13 * l)
        ctx.stroke()

        ctx.move_to(0.45 * l, 0.1 * l)
        ctx.line_to(0.45 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.45 * l, -0.1 * l)
        ctx.line_to(0.45 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "y":
        print("y")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.58 * l, 0.1 * l)
        ctx.line_to(0.55 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.58 * l, -0.1 * l)
        ctx.line_to(0.55 * l, -0.1 * l)
        ctx.stroke()

        ctx.move_to(0.58 * l, 0.13 * l)
        ctx.line_to(0.55 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.58 * l, -0.13 * l)
        ctx.line_to(0.55 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()

    if vowel == "Y":
        print("yy")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.48 * l, 0.1 * l)
        ctx.line_to(0.45 * l, 0.1 * l)
        ctx.stroke()

        ctx.move_to(0.48 * l, -0.1 * l)
        ctx.line_to(0.45 * l, -0.1 * l)
        ctx.stroke()

        ctx.move_to(0.48 * l, 0.13 * l)
        ctx.line_to(0.45 * l, 0.13 * l)
        ctx.stroke()

        ctx.move_to(0.48 * l, -0.13 * l)
        ctx.line_to(0.45 * l, -0.13 * l)
        ctx.stroke()

        ctx.restore()
