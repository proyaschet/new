import os
import unittest

from training.data_utils import DataUtils


class TestDataUtils(unittest.TestCase):
    def setUp(self):
        self.utils = DataUtils()
        self.sample_data = [
            {
                "text": "Maria Garcia is the new CEO.",
                "redacted_text": "[NAME] is the new CEO."
            }
        ]

    def test_load_training_data(self):
        # Prepare sample file
        sample_file = "test_pii_data.json"
        with open(sample_file, "w") as f:
            f.write('[{"text": "John Doe works at Google.", "redacted_text": "[NAME] works at [ORGANIZATION]."}]')

        # Test
        data = self.utils.load_training_data(sample_file)
        os.remove(sample_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1]["entities"], [(0, 8, "NAME"), (18, 24, "ORGANIZATION")])

    def test_extract_entities(self):
        text = "Maria Garcia is the new CEO."
        redacted_text = "[NAME] is the new CEO."
        entities = self.utils.extract_entities(text, redacted_text)
        self.assertEqual(entities, [(0, 12, "NAME")])

    def test_convert_to_biluo(self):
        training_data = [("Maria Garcia is the new CEO.", {"entities": [(0, 12, "NAME")]})]
        biluo_data = self.utils.convert_to_biluo(training_data)
        self.assertEqual(len(biluo_data), 1)
        self.assertIn("B-NAME", biluo_data[0][1]["entities"])

if __name__ == "__main__":
    unittest.main()
