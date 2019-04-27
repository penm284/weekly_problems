def rgb(r, g, b):
    if r < 0:
        r = "00"
    elif r > 255:
        r = "FF"
    elif r < 15:
        r = "0" + str(hex(r).split("x")[1]).upper()
    else:
        r = str(hex(r).split("x")[1]).upper()
    if g < 0:
        g = "00"
    elif g > 255:
        g = "FF"
    elif g < 15:
        g = "0" + str(hex(g).split("x")[1]).upper()
    else:
        g = str(hex(g).split("x")[1]).upper()
    if b < 0:
        b = "00"
    elif b > 255:
        b = "FF"
    elif b < 15:
        b = "0" + str(hex(b).split("x")[1]).upper()
    else:
        b = str(hex(b).split("x")[1]).upper()
    return r+g+b
