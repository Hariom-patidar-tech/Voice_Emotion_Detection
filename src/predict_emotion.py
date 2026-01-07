import pickle

def predict_emotion(text):
    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("model/best_model.txt", "r") as f:
        best_model_name = f.read().strip()

    with open(f"model/{best_model_name}.pkl", "rb") as f:
        model = pickle.load(f)

    X = vectorizer.transform([text])
    return model.predict(X)[0]
