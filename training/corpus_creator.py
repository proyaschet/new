from pathlib import Path

import srsly
from spacy.tokens import DocBin
from spacy.training.converters import json_to_docs


class CorpusCreator:
    """
    Class for creating spaCy-compatible corpora from processed data.
    """

    @staticmethod
    def create_corpus(corpus, path, filename):
        """
        Create and save a corpus in spaCy's binary format.
        :param corpus: Processed data to save.
        :param path: Path to save the file.
        :param filename: File name for the corpus.
        :return: Path to the created corpus file.
        """
        corpus_json = srsly.json_dumps(corpus)
        corpus_bytes = DocBin(docs=json_to_docs(corpus_json.encode("utf8")), store_user_data=True).to_bytes()

        file_path = path / filename
        with file_path.open("wb") as file:
            file.write(corpus_bytes)

        return file_path
