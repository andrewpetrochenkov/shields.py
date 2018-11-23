#!/usr/bin/env python
import shields

"""
http://shields.io/
https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg

brightgreen, green, yellowgreen, yellow, orange, red, lightgrey, blue
"""


class Badge(shields.Abstract):
    """shields.io custom Badge"""
    __readme__ = ["subject", "status", "color"]
    path = "badge/{subject}-{status}-{color}.svg"
    subject = None
    status = None
    color = "green"
