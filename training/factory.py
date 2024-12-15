from spacy.lang.en import English
from spacy.schemas import ConfigSchemaTraining
from spacy.training.initialize import get_sourced_components
from spacy.training.loop import train
from spacy.util import (load_config, load_model_from_config, registry,
                        resolve_dot_names)
from thinc.api import fix_random_seed


class TrainingFactory:
    """
    Factory class to handle model initialization and training.
    """

    def __init__(self, config_path):
        self.config_path = config_path
        self.nlp = English()

    def initialize_model(self, train_path, dev_path):
        """
        Initialize a spaCy model from a configuration file.
        :param train_path: Path to the training corpus.
        :param dev_path: Path to the development corpus.
        :return: Initialized spaCy model.
        """
        config = load_config(self.config_path)
        config["paths"]["train"] = str(train_path)
        config["paths"]["dev"] = str(dev_path)
        raw_config = config
        config = raw_config.interpolate()
        fix_random_seed(config["training"]["seed"])
        allocator = config["training"]["gpu_allocator"]
        sourced_components = get_sourced_components(config)
        self.nlp  = load_model_from_config(raw_config, auto_fill=True)
        config = self.nlp.config.interpolate()
        T = registry.resolve(config["training"], schema=ConfigSchemaTraining)
        dot_names = [T["train_corpus"], T["dev_corpus"]]
        train_corpus, dev_corpus = resolve_dot_names(config, dot_names)
        optimizer = T["optimizer"]
        frozen_components = T["frozen_components"]
        resume_components = [p for p in sourced_components if p not in frozen_components]
        with self.nlp.select_pipes(disable=[*frozen_components, *resume_components]):
            self.nlp.initialize(lambda: train_corpus(self.nlp), sgd=optimizer)
            
        

    def train_model(self, output_dir):
        """
        Train the initialized spaCy model.
        :param output_dir: Directory to save the trained model.
        """
        if not self.nlp:
            raise ValueError("Model not initialized. Call `initialize_model` first.")
        train(self.nlp, output_dir)
