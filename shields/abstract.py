#!/usr/bin/env python
try:
    from urllib import urlencode  # python2
except ImportError:
    from urllib.parse import urlencode  # python3
import badge
import public

"""
http://shields.io/

The following styles are available (flat is the default as of Feb 1st 2015)
"""
STYLES = ["plastic", "flat", "flat-square", "for-the-badge", "social"]
"""without 'link'"""
PARAMETERS = ["style", "label", "logo", "logoWidth", "colorA", "colorB", "maxAge", "longCache"]


class Abstract(badge.Badge):
    @property
    def parameters(self):
        parameters = dict()
        for key in PARAMETERS:
            value = getattr(self, key, None)
            if value:
                parameters[key] = value
        return parameters

    @property
    def query(self):
        return urlencode(self.parameters)

    @property
    def image(self):
        image = "https://img.shields.io/%s" % self.path
        if self.parameters:
            return "%s?%s" % (image, self.query)
        return image
