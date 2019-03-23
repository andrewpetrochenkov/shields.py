#!/usr/bin/env python
import public
import shields

"""
http://shields.io/
version:              https://img.shields.io/pypi/v/Django.svg

License:              https://img.shields.io/pypi/l/Django.svg
Wheel:                https://img.shields.io/pypi/wheel/Django.svg
Format:               https://img.shields.io/pypi/format/Django.svg
pyversions:           https://img.shields.io/pypi/pyversions/Django.svg
Implementation:       https://img.shields.io/pypi/implementation/Django.svg
Status:               https://img.shields.io/pypi/status/Django.svg
"""


class Pypi(shields.Abstract):
    __readme__ = []
    name = None
    link = "https://pypi.org/project/{name}/"
    path = "pypi/{cls}/{name}.svg"

    def __init__(self, name, **kwargs):
        self.name = name
        self.update(kwargs)

    @property
    def cls(self):
        return self.__class__.__name__.lower()


@public.add
class V(Pypi):
    """pypi Version badge"""


@public.add
class L(Pypi):
    """pypi License badge"""


class Wheel(Pypi):
    pass


class Format(Pypi):
    pass


@public.add
class Pyversions(Pypi):
    """pypi pyversions badge"""


class Implementation(Pypi):
    pass


class Status(Pypi):
    pass
