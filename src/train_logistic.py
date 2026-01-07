import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from preprocess import text_to_features


os.makedirs("model", exist_ok=True)

import pandas as pd

df = pd.read_csv("data/emotion_dataset.csv")

texts = df["text"].tolist()
labels = df["emotion"].tolist()

print("Loaded emotions:", set(labels))
print("Total samples:", len(labels))


                    # Train–Test Split
X_train_text, X_test_text, y_train, y_test = train_test_split(
    texts, labels,
    test_size=0.4,
    random_state=42,
    stratify=labels
)


                      # Feature Extraction
X_train, X_test, vectorizer = text_to_features(X_train_text, X_test_text)

                      # Save vectorizer
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


                     # Models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "SVM": SVC(),
    "NaiveBayes": MultinomialNB(),
    "DecisionTree": DecisionTreeClassifier(),
    "RandomForest": RandomForestClassifier(n_estimators=100),
    "KNN": KNeighborsClassifier(n_neighbors=1), 
    "GradientBoosting": GradientBoostingClassifier()
}


                           # Train + Accuracy
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    results[name] = acc

    print(f"{name} Accuracy = {acc:.4f}")

    with open(f"model/{name}.pkl", "wb") as f:
        pickle.dump(model, f)


                         # Best Model
best_model = max(results, key=results.get)
print("\n Best Model:", best_model)
print(" Best Accuracy:", results[best_model])

                          # Save best model name
with open("model/best_model.txt", "w") as f:
    f.write(best_model)
