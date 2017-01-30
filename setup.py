from distutils.core import setup

try:
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

exec(open("matrox/version.py", "r").read())

setup(
    name="matrox",
    version=__version__,
    author="Robert Kim",
    author_email="me@robertkim.io",
    packages=["matrox", "matrox.linalg", "matrox.tests"],
    url="https://github.com/rkty13/matrox",
    license="The MIT License (MIT)",
    description="Linear Algebra library."
)