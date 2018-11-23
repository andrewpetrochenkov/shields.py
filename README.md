[![](https://img.shields.io/pypi/pyversions/shields.svg?longCache=True)](https://pypi.org/pypi/shields/)
[![](https://img.shields.io/pypi/v/shields.svg?maxAge=3600)](https://pypi.org/pypi/shields/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/shields.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/shields.py/)

#### Install
```bash
$ [sudo] pip install shields
```

#### Features
+   autoformat strings
+   [shields.io](http://shields.io/) **parameters**: `style`, `for-the-badge`, `social`), `label`, `logo`, `logoWidth`, `colorA`, `colorB`, `maxAge`, `longCache`
+   [shields.io](http://shields.io/) **styles**: `flat` (default), `plastic`, `flat-square`, `for-the-badge`, `social`

#### Classes

###### `shie.Badge`

shields.io custom Badge

attr|default value
-|-
`color`|`green`
`status`|`None`
`subject`|`None`

###### `shields.npm.V`

npm Version badge

###### `shields.pypi.L`

pypi License badge

###### `shields.pypi.Pyversions`

pypi pyversions badge

###### `shields.pypi.V`

pypi Version badge

#### Examples
static badge [![](https://img.shields.io/badge/subject-status-blue.svg)]()
```python
>>> shields.Badge(subject="subject", status="status", color="blue", maxAge=3600)
'[![](https://img.shields.io/badge/subject-status-blue.svg)]()'
```

##### pypi badges

[![](https://img.shields.io/pypi/v/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/pyversions/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/l/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/wheel/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/format/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/implementation/django.svg)](https://pypi.org/pypi/django/)
[![](https://img.shields.io/pypi/status/django.svg)](https://pypi.org/pypi/django/)

```python
>>> shields.pypi.V("django")
'[![](https://img.shields.io/pypi/v/django.svg)](https://pypi.org/pypi/name/)'

>>> shields.pypi.Pyversions("django")
'[![](https://img.shields.io/pypi/pyversions/django.svg)](https://pypi.org/pypi/name/)'

>>> shields.pypi.L("django")
'[![](https://img.shields.io/pypi/l/django.svg)](https://pypi.org/pypi/name/)'
```

##### subclass

```python
>>> class New(shields.Abstract):
    path = "npm/v/{name}.svg"
    link = "https://www.npmjs.com/package/{name}"

>>> Npm(name="jquery")
'[![](https://img.shields.io/npm/v/jquery.svg)](https://www.npmjs.com/package/jquery)'
```

#### Links
+   [shields.io](http://shields.io/)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>