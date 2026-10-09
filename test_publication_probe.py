import unittest

from publication_probe import greet


class PublicationProbeTests(unittest.TestCase):
    def test_greet_ada(self):
        self.assertEqual(greet("Ada"), "Publication proof: Ada")

    def test_greet_zoe(self):
        self.assertEqual(greet("Zoë"), "Publication proof: Zoë")


if __name__ == "__main__":
    unittest.main()
