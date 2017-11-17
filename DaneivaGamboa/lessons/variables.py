sz = 2
def h2():
    """ Draw the next step of a spiral on each call. """
    global sz
    tess.turn(42)
    tess.forward(sz)
    sz += 1