from pathlib import Path

import spacy


class ModelFactory:
    """
    Factory to load the trained spaCy model and handle predictions.
    """

    def __init__(self, model_path):
        """
        Initialize the factory with the model path.
        :param model_path: Path to the trained spaCy model.
        """
        self.model_path = Path(model_path)
        self.nlp = None

    def load_model(self):
        """
        Load the trained spaCy model from disk.
        Raises:
            FileNotFoundError: If the model does not exist at the specified path.
        """
        
        if not self.model_path.exists():
            raise FileNotFoundError(f"Error: Model path '{self.model_path}' does not exist. Please train the model.")
        try:
            self.nlp = spacy.load(self.model_path)
            print("Model loaded successfully!")
        except Exception as e:
            raise ValueError(f"Error while loading the model: {e}")
        return self.nlp

    def predict(self, text):
        """
        Redact PII entities in the input text.
        :param text: Input text to process.
        :return: Redacted text with entities replaced by labels.
        Raises:
            ValueError: If the model is not loaded.
        """
        if self.nlp is None:
            raise ValueError("Error: Model not loaded. Please load the model using 'load_model()' first.")
        doc = self.nlp(text)
        redacted_text = text
        for ent in doc.ents:
            redacted_text = redacted_text.replace(ent.text, f"[{ent.label_}]")
        return redacted_text
