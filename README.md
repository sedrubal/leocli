leo - a console translation script for https://dict.leo.org
===========================================================

leo is a python script that queries `dict.leo.org` for one or more given keywords
and prints their meanings and translations to stdout

Installation
------------

If you want to install leo system-wide, you should use setup.py:

    python setup.py install

This will invoke python's setuptools and install leo to the system's
site-packages directory and create an executable script in `/usr/bin/leo`
To choose other install locations refer to setuptool's help by invoking

    python setup.py install --help

If you do not wish to install leo system-wide you can simply call it by invoking

    leo/leo.py

from the directory you downloaded leo to.

Usage
-----

After installing, run `leo` or if you don't want to install it, run `leo/leo.py.

```
usage: leo.py [-h] [-l lang] word [word ...]

leo - a console translation script for https://dict.leo.org

positional arguments:
  word                  the words you want to translate

optional arguments:
  -h, --help            show this help message and exit
  -l lang, --lang lang  the languagecode to translate to or from
                        (en, fr, es, it, ch, ru, pt, pl)
```

License
-------

[MIT](COPYING)
