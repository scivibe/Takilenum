import numpy as np

def draw_letter(letter, ctx, centroidX, centroidY, cornerX, cornerY, glyphSize):
    dx = cornerX - centroidX 
    dy = cornerY - centroidY
    l = np.sqrt(dx**2 + dy**2)
    ang = np.arctan2(dy, dx)
    if letter == " " or letter is None:
        print("space")
    elif letter == "t":
        print("t")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.39 * l, -0.15 * l)
        ctx.line_to(0.15 * l, -0.25 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "d":
        print("d")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.39 * l, -0.15 * l)
        ctx.line_to(1.0 * l, 0.0 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "p":
        print("p")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.39 * l, -0.15 * l)
        ctx.line_to(0.3 * l, -0.188 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "b":
        print("b")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.39 * l, -0.15 * l)
        ctx.line_to(0.48 * l, -0.128 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "k":
        print("k")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.36 * l, -0.1 * l)
        ctx.line_to(0.06 * l, -0.1 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "q":
        print("q")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.48 * l, -0.3 * l)
        ctx.stroke()
        ctx.move_to(0.36 * l, -0.1 * l)
        ctx.line_to(0.48 * l, -0.1 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "l":
        print("l")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "r":
        print("r")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.line_to(0, 0)
        ctx.stroke()
        ctx.restore()

    elif letter == "m":
        print("m")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.2 * l, -0.1 * l)
        ctx.stroke()

        ctx.move_to(0.3 * l, 0.1 * l)
        ctx.line_to(0.4 * l, 0.0 * l)
        ctx.line_to(0.3 * l, -0.1 * l)
        ctx.stroke()
        
        ctx.stroke()
        ctx.restore()

    elif letter == "n":
        print("n")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.2 * l, -0.1 * l)
        ctx.stroke()
        
        ctx.stroke()
        ctx.restore()

    elif letter == "N":
        print("ng")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.2 * l, -0.1 * l)
        ctx.stroke()

        ctx.move_to(0.3 * l, 0.08 * l)
        ctx.line_to(0.4 * l, 0.0 * l)
        ctx.line_to(0.3 * l, -0.08 * l)
        
        ctx.stroke()
        ctx.restore()

    elif letter == "f":
        print("f")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.275 * l, 0.215 * l)
        ctx.line_to(1.0 * l, 0.0 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "v":
        print("v")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, 0.0 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.275 * l, 0.215 * l)
        ctx.line_to(1.0 * l, 0.0 * l)
        ctx.stroke()
        ctx.move_to(0.8 * l, 0.0 * l)
        ctx.line_to(0.835 * l, 0.1 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "T":
        print("th")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.2 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.275 * l, 0.215 * l)
        ctx.line_to(1.0 * l, 0.0 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "D":
        print("dh")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.2 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.275 * l, 0.215 * l)
        ctx.line_to(1.0 * l, 0.0 * l)
        ctx.stroke()
        ctx.move_to(0.8 * l, -0.05 * l)
        ctx.line_to(0.835 * l, 0.1 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "s":
        print("s")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.25 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.25 * l, 0.43 * l)
        ctx.line_to(0, 0)
        ctx.stroke()
        ctx.restore()

    elif letter == "z":
        print("z")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.25 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.25 * l, 0.43 * l)
        ctx.line_to(0, 0)
        ctx.stroke()
        ctx.move_to(0.8 * l, -0.05 * l)
        ctx.line_to(0.835 * l, 0.1 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "S":
        print("sh")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.25 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.25 * l, 0.43 * l)
        ctx.line_to(0, 0)
        ctx.stroke()
        ctx.move_to(0.15 * l, -0.2 * l)
        ctx.line_to(0.35 * l, 0.0 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "Z":
        print("zh")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)
        ctx.move_to(0.3 * l, -0.25 * l)
        ctx.line_to(0.25 * l, 0.43 * l)
        ctx.stroke()
        ctx.move_to(0.25 * l, 0.43 * l)
        ctx.line_to(0, 0)
        ctx.stroke()
        ctx.move_to(0.8 * l, -0.05 * l)
        ctx.line_to(0.835 * l, 0.1 * l)
        ctx.stroke()
        ctx.move_to(0.15 * l, -0.2 * l)
        ctx.line_to(0.35 * l, 0.0 * l)
        ctx.stroke()
        ctx.restore()

    elif letter == "j":
        print("j")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.3 * l, 0.0 * l)
        ctx.stroke()

        ctx.move_to(0.3 * l, 0.1 * l)
        ctx.line_to(0.4 * l, 0.0 * l)
        ctx.stroke()

        ctx.move_to(0.1 * l, 0.1 * l)
        ctx.line_to(0.2 * l, 0.0 * l)
        ctx.stroke()
        
        ctx.stroke()
        ctx.restore()

    elif letter == "w":
        print("w")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.4 * l, -0.1 * l)
        ctx.stroke()

        ctx.move_to(0.3 * l, 0.1 * l)
        ctx.line_to(0.4 * l, 0.0 * l)
        ctx.stroke()

        ctx.move_to(0.1 * l, 0.1 * l)
        ctx.line_to(0.2 * l, 0.0 * l)
        ctx.stroke()
        
        ctx.stroke()
        ctx.restore()

    elif letter == "x":
        print("x")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.4 * l, -0.1 * l)
        ctx.stroke()
        
        ctx.stroke()
        ctx.restore()

    elif letter == "h":
        print("h")
        ctx.save()
        ctx.translate(centroidX, centroidY)
        ctx.rotate(ang)

        ctx.move_to(0.1 * l, 0.1 * l)
        ctx.line_to(0.3 * l, -0.1 * l)
        ctx.stroke()
        ctx.move_to(0.2 * l, 0.1 * l)
        ctx.line_to(0.4 * l, -0.1 * l)
        ctx.stroke()

        ctx.stroke()
        ctx.restore()