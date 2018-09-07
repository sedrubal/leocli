# leo

a console translation script for https://dict.leo.org

[![Code Health](https://landscape.io/github/sedrubal/leo/master/landscape.svg?style=flat)](https://landscape.io/github/sedrubal/leo/master)

leo is a python script that queries `dict.leo.org` for one or more given keywords
and prints their meanings and translations to stdout

# Installation

```sh
pipenv sync
```

Usage
-----

TODO: This should be improved...

```sh
pipenv run python -m leo --help
```

```
usage: leo [-h] [-l lang] [--version] word [word ...]

leo - a console translation script for https://dict.leo.org

positional arguments:
  word                  the words you want to translate

optional arguments:
  -h, --help            show this help message and exit
  -l lang, --lang lang  the languagecode to translate to or from
                        (en, fr, es, it, ch, ru, pt, pl)
  --version             show program's version number and exit
```

License
-------

[MIT](COPYING)
