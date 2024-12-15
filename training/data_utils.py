import json
import re

from spacy.lang.en import English
from spacy.training import offsets_to_biluo_tags


class DataUtils:
    """
    Utility class for handling training data and entity extraction.
    """

    def __init__(self):
        self.nlp = English()

    def load_training_data(self, file_path):
        """
        Load and preprocess training data from a JSON file.
        :param file_path: Path to the JSON file.
        :return: List of tuples with "text" and "entities".
        """
        with open(file_path, "r") as f:
            raw_data = json.load(f)

        processed_data = []
        for item in raw_data:
            text = item["text"]
            redacted_text = item["redacted_text"]

            # Extract entities
            entities = self.extract_entities(text, redacted_text)

            if entities:
                processed_data.append((text, {"entities": entities}))

        return processed_data

    def extract_entities(self, text, redacted_text):
        """
        Extract entities (start, end, label) from redacted text.
        :param text: Original text.
        :param redacted_text: Text with placeholders like [NAME].
        :return: List of tuples (start, end, label).
        """
        entities = []
        placeholder_pattern = r"\[(.*?)\]"  # Matches placeholders like [NAME]

        # Split redacted_text on placeholders
        parts = re.split(placeholder_pattern, redacted_text)

        current_pos = 0
        for i in range(len(parts)):
            if i % 2 == 1:  # Placeholder (e.g., NAME)
                label = parts[i]
                before_placeholder = parts[i - 1]
                after_placeholder = parts[i + 1] if i + 1 < len(parts) else ""

                # Locate entity span
                start_in_text = text.find(before_placeholder, current_pos) + len(before_placeholder)
                end_in_text = text.find(after_placeholder, start_in_text) if after_placeholder else len(text)

                if start_in_text < end_in_text:
                    entities.append((start_in_text, end_in_text, label))

                current_pos = end_in_text

        return entities

    def convert_to_biluo(self, training_data):
        """
        Convert training data to BILUO format.
        :param training_data: List of tuples with "text" and "entities".
        :return: List of tuples with "text" and BILUO tags.
        """
        biluo_data = []
        for text, annotations in training_data:
            tokens = self.nlp.tokenizer(text)
            tags = offsets_to_biluo_tags(tokens, annotations["entities"])
            biluo_data.append((tokens.text, {"entities": tags}))
        return biluo_data
    
    def biluo_to_json(self,train_data):
        """[summary]

        Args:
            train_data ([type]): [description]

        Returns:
            [type]: [description]
        """
        corpus = []
        doc = 1
        # print(train_data[0])
        for i, v in train_data:
            paragraph = dict()
            paragraph["paragraphs"] = []
            sentence = dict()
            sentence["sentences"] = []
            tokens = {}
            tokens['tokens'] = []
            token = self.nlp.tokenizer(i)
            ents = v['entities']
            for i in range(len(token)):
                info = {}
                info["orth"] = token[i].text
                info["tag"] = "-"
                info["ner"] = ents[i]
                tokens['tokens'].append(info)
            sentence["sentences"].append(tokens)
            paragraph['id'] = doc
            paragraph["paragraphs"].append(sentence)
            corpus.append(paragraph)
            doc += 1
        return corpus
