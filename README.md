# matrox

[![Build Status](https://travis-ci.org/rkty13/matrox.svg?branch=master)](https://travis-ci.org/rkty13/matrox) [![Coverage Status](https://coveralls.io/repos/github/rkty13/matrox/badge.svg?branch=master)](https://coveralls.io/github/rkty13/matrox?branch=master) [![PyPI](https://img.shields.io/pypi/pyversions/matrox.svg)](https://pypi.python.org/pypi/matrox)

matrox is a linear algebra library. The purpose of this project is for my own educational value as I learn more about linear algebra. The contents of this project will follow Gilbert Strang's textbook, "Linear Algebra and Its Applications, 4th Edition" as well as other topics/methods I learn online.

## Installation

Run `pip install matrox` to install the latest version.

## Basic Usage

```
>>> from matrox import *
>>> from matrox.linalg import *
>>> matrix = Matrix([[1, 2], [3, 4]], fraction=True)
>>> gaussian_elimination(matrix)
Matrix([['1', '0'], ['0', '1']])
```

## Running Tests
```
pip install coverage
coverage run --source=matrox -m unittest discover
```