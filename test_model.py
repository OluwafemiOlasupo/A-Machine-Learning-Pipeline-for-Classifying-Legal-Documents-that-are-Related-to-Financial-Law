import unittest
import pickle
import numpy as np
from sklearn.metrics import accuracy_score


class TestSVMModel(unittest.TestCase):
    def setUp(self):
        # Load the model
        with open('../svm_model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        # Load the vectorizer
        with open('../vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)

        # Load a small sample of your test data
        # Replace this with actual loading of your test data
        self.test_texts = ["This is a sample document", "Another sample document"]
        self.test_labels = [1, 0]  # Replace with actual labels

    def test_model_accuracy(self):
        # Vectorize the test texts
        X_test = self.vectorizer.transform(self.test_texts)

        # Make predictions
        y_pred = self.model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(self.test_labels, y_pred)

        # Assert that accuracy is above a threshold
        self.assertGreater(accuracy, 0.7, "Model accuracy should be greater than 0.7")


if __name__ == '__main__':
    unittest.main()