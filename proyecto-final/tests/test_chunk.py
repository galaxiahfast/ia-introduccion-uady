import unittest

from app.chunk import split_text


class ChunkTests(unittest.TestCase):
    def test_divide_y_conserva_solapamiento(self):
        text = " ".join(f"palabra{i}" for i in range(700))
        chunks = split_text(text, "prueba.txt", size=300, overlap=60)

        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0].text.split()[-60:], chunks[1].text.split()[:60])
        self.assertEqual(chunks[0].source, "prueba.txt")


if __name__ == "__main__":
    unittest.main()

