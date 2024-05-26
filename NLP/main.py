class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self.r, self.g, self.b = int(hexcode[:2], 16), int(hexcode[2:4], 16), int(hexcode[4:6], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self.r, self.g, self.b = int(hexcode[:2],16), int(hexcode[2:4], 16), int(hexcode[4:6], 16)
        self._hexcode = hexcode

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)