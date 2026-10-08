import hashlib
import json
from pathlib import Path
import unittest


class ValidationBaselineTests(unittest.TestCase):
    def test_original_published_documents_remain_exact(self):
        root = Path(__file__).parent
        directory = root / "docs/factory/validation-spec-7/da123bcf443d3605e5f0d22172823ab483ff9bd0f264e89bdf3ba9ec0f6ebf61"
        expected = {
            "decisions.json": "f6968a4f62da754868fac273b9646d962395dc94",
            "milestone.json": "bf8fb8b8feddc5ed15d77d2c90e2de98c37f69be",
            "vision.json": "d9750ec8375c4c7844f6143b50cf85a564fab5ce",
        }
        for name, blob in expected.items():
            with self.subTest(document=name):
                path = directory / name
                self.assertFalse(path.is_symlink())
                data = path.read_bytes()
                git_object = b"blob " + str(len(data)).encode() + b"\0" + data
                self.assertEqual(hashlib.sha1(git_object).hexdigest(), blob)
                document = json.loads(data)
                self.assertIsInstance(document, dict)
                self.assertTrue(document)


if __name__ == "__main__":
    unittest.main()
