# matrox

[![Build Status](https://travis-ci.org/rkty13/matrox.svg?branch=master)](https://travis-ci.org/rkty13/matrox) [![Coverage Status](https://coveralls.io/repos/github/rkty13/matrox/badge.svg?branch=master)](https://coveralls.io/github/rkty13/matrox?branch=master) [![PyPI](https://img.shields.io/pypi/pyversions/matrox.svg)](https://pypi.python.org/pypi/matrox)

matrox is a linear algebra library. The purpose of this project is for my own educational value as I learn more about linear algebra. **This is not a production ready library.** The contents of this project will loosely follow the following resources:

* Linear Algebra and Its Applications - Gilbert Strang
* Worldwide Differential Equations with Linear Algebra - Robert McOwen
* Stuff I learn online and in class

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

