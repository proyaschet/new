from pathlib import Path

# File paths
TRAINING_DATA_PATH = Path("training/pii_data.json")
CONFIG_PATH = Path("training/config.cfg")
MODEL_SAVE_PATH = Path("model")
TRAIN_CORPUS_FILENAME = "training/train.spacy"
DEV_CORPUS_FILENAME = "training/dev.spacy"

# Corpus split ratio
TRAIN_SPLIT_RATIO = 0.8
