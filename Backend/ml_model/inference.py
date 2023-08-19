import joblib
import pickle
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re


class Inference:
    def __init__(self, model_no) -> None:
        self.model = None
        self.cv = None
        with open(f"./ml_model/model_{model_no}.pkl", "rb") as file:
            self.model = pickle.load(file)
        self.cv = joblib.load(f"./ml_model/cv_{model_no}.pkl")
        self.ps = PorterStemmer()

    def predict(self, text):
        text = text.lower()
        text = text.split()
        text = [
            self.ps.stem(word)
            for word in text
            if not word in set(stopwords.words("english"))
        ]
        text = " ".join(text)
        text = re.sub(r"[.,'-\/:]", " ", text)
        text = self.cv.transform([text]).toarray()
        return self.model.predict(text)
