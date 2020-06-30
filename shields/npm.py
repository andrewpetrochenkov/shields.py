__all__ = ['V']


import shields

"""

"""


class Npm(shields.Abstract):
    name = None
    link = "https://www.npmjs.com/package/{name}"

    def __init__(self, name, **kwargs):
        self.name = name
        self.update(kwargs)


class V(Npm):
    """npm Version badge"""
    path = "npm/v/{name}.svg"
    __readme__ = []
