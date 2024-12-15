import os
import unittest
from pathlib import Path

from training.corpus_creator import CorpusCreator
from training.data_utils import DataUtils


class TestCorpusCreator(unittest.TestCase):
    def setUp(self):
        self.creator = CorpusCreator()
        self.sample_data = [
            ("Maria Garcia is the CEO.", {"entities": [(0, 12, "NAME")]})
        ]
        self.output_dir = Path(".")

    def test_create_corpus(self):
        data_utils = DataUtils()
        biluo_data = data_utils.convert_to_biluo(self.sample_data)
        corpus = data_utils.biluo_to_json(biluo_data)
        file_path = self.creator.create_corpus(corpus, self.output_dir, "test_corpus.spacy")
        self.assertTrue(file_path.exists())
        self.assertTrue(file_path.suffix == ".spacy")

        # Cleanup
        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
