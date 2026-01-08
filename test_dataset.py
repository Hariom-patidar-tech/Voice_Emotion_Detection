                             # test_dataset.py
import pickle
from sklearn.metrics import accuracy_score

test_texts = [
    "I am feeling happy",
    "I am very sad",
    "I am angry today",
    "I am good",
    "I am shock",
    "I am scared"
    
]

test_labels = [
    "happy",
    "sad",
    "angry",
    "nuetral",
    "surprise",
    "fear"
]

                                   # Load vectorizer
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

X_test = vectorizer.transform(test_texts)

models = [
    "GradientBoosting"
]

for name in models:
    with open(f"model/{name}.pkl", "rb") as f:
        model = pickle.load(f)

    preds = model.predict(X_test)
    acc = accuracy_score(test_labels, preds)

    print(f"{name} Test Accuracy = {acc:.4f}")
