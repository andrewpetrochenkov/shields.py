#!/usr/bin/env python
import shields


class Npm(shields.Abstract):
    path = "npm/v/{name}.svg"
    link = "https://www.npmjs.com/package/{name}"


badge = Npm(name="jquery")
print(badge)
