from pathlib import Path

from training.constants import (CONFIG_PATH, DEV_CORPUS_FILENAME,
                                MODEL_SAVE_PATH, TRAIN_CORPUS_FILENAME,
                                TRAIN_SPLIT_RATIO, TRAINING_DATA_PATH)
from training.corpus_creator import CorpusCreator
from training.data_utils import DataUtils
from training.factory import TrainingFactory


def main():
    # Initialize utilities
    data_utils = DataUtils()
    corpus_creator = CorpusCreator()
    factory = TrainingFactory(CONFIG_PATH)

    # Load and process training data
    print("Loading and processing training data...")
    training_data = data_utils.load_training_data(TRAINING_DATA_PATH)
    
    # Convert to BILUO format
    print("Converting to BILUO format...")
    biluo_data = data_utils.convert_to_biluo(training_data)
    
    # Convert to BILUO format
    print("Converting to BILUO format...")
    corpus = data_utils.biluo_to_json(biluo_data)

    # Split data into train and dev sets
    train_len = int(len(corpus) * TRAIN_SPLIT_RATIO)
    train_data = corpus[:train_len]
    dev_data = corpus[train_len:]

    # Create corpora
    print("Creating corpora...")
    train_path = corpus_creator.create_corpus(train_data, Path("."), TRAIN_CORPUS_FILENAME)
    dev_path = corpus_creator.create_corpus(dev_data, Path("."), DEV_CORPUS_FILENAME)

    # Initialize and train model
    print("Initializing model...")
    nlp = factory.initialize_model(train_path, dev_path)

    print("Training model...")
    MODEL_SAVE_PATH.mkdir(exist_ok=True)
    factory.train_model(MODEL_SAVE_PATH)
    print("Model training complete. Saved to:", MODEL_SAVE_PATH)
    completion_flag = Path("model/training_complete.flag")
    completion_flag.touch()
    print(f"Training complete. Flag written to {completion_flag}")

if __name__ == "__main__":
    main()
