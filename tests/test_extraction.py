import unittest
from extraction.extract_triples import extract_triples

class TestTripleExtraction(unittest.TestCase):
    def test_extract_triples(self):
        text = "Yao's Garbled Circuits implements privacy-preserving computations."
        expected = [("Yao's Garbled Circuits", "implements", "privacy-preserving computations")]
        self.assertEqual(extract_triples(text), expected)

if __name__ == "__main__":
    unittest.main()
