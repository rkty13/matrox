import unittest

from matrox.version import __version__

class TestMeta(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, "0.1.2")