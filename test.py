def _tex_coord(x, y, n=8):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = 1 - (y + 1) * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def _tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = _tex_coord(*top)
    bottom = _tex_coord(*bottom)
    side = _tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result

print(_tex_coords((0, 2), (0, 2), (0, 2)))