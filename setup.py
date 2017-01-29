from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

exec(open("matrox/version.py", "r").read())

setup(
    name="matrox",
    version=__version__,
    install_requires=requirements,
    author="Robert Kim",
    author_email="me@robertkim.io",
    packages=["matrox", "matrox.linalg", "matrox.tests"],
    url="https://github.com/rkty13/matrox",
    license="The MIT License (MIT)",
    description="Linear Algebray library.",
    include_package_data=False
)