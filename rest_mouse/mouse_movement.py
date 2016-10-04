from pymouse import PyMouse
from pykeyboard import PyKeyboard

from rest_mouse.models.mouse_model import MouseModel

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
_x, _y = m.position()


def mouse_post(json):
    _x, _y = m.position()
    try:
        method = json["method"]  # type: str
    except KeyError:
        raise KeyError("Json must provide method")

    if method.lower() == "move":
        try:
            x, y = json["x"], json["y"]
        except KeyError:
            raise KeyError("Move method requires x, y")

        try:
            x, y = float(x), float(y)
            x, y = int(x * x_dim), int(y * y_dim)

            _x, _y = x, y
        except ValueError:
            raise ValueError("Failed to cast x or y to int (we first resize x, y)")

        m.move(_x, _y)
        return

    if method.lower() == "left":
        m.click(_x, _y, 1)
        return

    if method.lower() == "right":
        m.click(_x, _y, 2)
        return

    raise ValueError("Invalid method provided")

def mouse_get():
    _x, _y = m.position()
    return MouseModel(method="request", x=_x, y=_y)