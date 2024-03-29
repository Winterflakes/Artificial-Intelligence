# WAP to implement Naive Bayers classification on play tennis dataset

import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probabilities = {}
        self.feature_probabilities = {}
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        
        # Calculate class probabilities
        for c in self.classes:
            self.class_probabilities[c] = np.sum(y == c) / float(n_samples)
        
        # Calculate feature probabilities
        self.feature_probabilities = {}
        for c in self.classes:
            self.feature_probabilities[c] = {}
            for i in range(n_features):
                self.feature_probabilities[c][i] = {}
                unique_feature_values = np.unique(X[:, i])
                for val in unique_feature_values:
                    self.feature_probabilities[c][i][val] = \
                        np.sum(X[y == c][:, i] == val) / float(np.sum(y == c))
    
    def predict(self, X):
        predictions = []
        for sample in X:
            probabilities = {}
            for c in self.classes:
                probabilities[c] = self.class_probabilities[c]
                for i, value in enumerate(sample):
                    probabilities[c] *= self.feature_probabilities[c][i].get(value, 0)
            predicted_class = max(probabilities, key=probabilities.get)
            predictions.append(predicted_class)
        return predictions

# Define the dataset
X = np.array([
    ['Sunny', 'Hot', 'High', 'Weak'],
    ['Sunny', 'Hot', 'High', 'Strong'],
    ['Overcast', 'Hot', 'High', 'Weak'],
    ['Rain', 'Mild', 'High', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Strong'],
    ['Overcast', 'Cool', 'Normal', 'Strong'],
    ['Sunny', 'Mild', 'High', 'Weak'],
    ['Sunny', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'Normal', 'Weak'],
    ['Sunny', 'Mild', 'Normal', 'Strong'],
    ['Overcast', 'Mild', 'High', 'Strong'],
    ['Overcast', 'Hot', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'High', 'Strong']
])

y = np.array(['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'])

# Create Naive Bayes Classifier instance
nb_classifier = NaiveBayesClassifier()

# Train the classifier
nb_classifier.fit(X, y)

# Test data
test_data = np.array([
    ['Sunny', 'Hot', 'Normal', 'Weak'],
    ['Overcast', 'Hot', 'High', 'Strong'],
    ['Rain', 'Mild', 'Normal', 'Strong']
])

# Make predictions
predictions = nb_classifier.predict(test_data)

# Print predictions
for i, prediction in enumerate(predictions):
    print("Sample {}: {}".format(i+1, prediction))
