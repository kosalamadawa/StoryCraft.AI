import pandas as pd
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from skmultilearn.adapt import MLkNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, hamming_loss
from sklearn.feature_extraction.text import CountVectorizer
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.svm import SVC
import re
import pickle
import joblib


def train_model(model_no):
    ps = PorterStemmer()

    tests_col_len = 0
    steps_col_len = 0
    expects_col_len = 0
    col_names = []

    if model_no == "1":
        df = pd.read_csv(
            f"./data/dataset_{model_no}.csv",
            delimiter="|",
            header=None,
            names=["story", "tests"],
        )

        # print(df.head())

        for _, row in df.iterrows():
            split_list = str(row["tests"]).split(",")
            col_split_len = len(split_list)
            if col_split_len == 1 and split_list[0] == "nan":
                col_split_len = 0
            if col_split_len > tests_col_len:
                tests_col_len = col_split_len

        col_names.append("story")
        for i in range(tests_col_len):
            col_names.append("test_" + str(i))

        new_df = pd.DataFrame(columns=col_names)
        new_df["story"] = df["story"]

        for i in range(df.shape[0]):
            tests_split = str(df["tests"][i]).split(",")
            for y in range(tests_col_len):
                if y >= len(tests_split):
                    new_df[f"test_{y}"][i] = 0
                else:
                    new_df[f"test_{y}"][i] = tests_split[y]

        new_df[new_df.columns[1:]] = new_df[new_df.columns[1:]].astype(int)

        # print(new_df.head())

        corpus = []
        for i in range(len(df)):
            usecase = new_df["story"][i]
            usecase = usecase.lower()
            usecase = usecase.split()
            usecase = [
                ps.stem(word)
                for word in usecase
                if not word in set(stopwords.words("english"))
            ]
            usecase = " ".join(usecase)
            usecase = re.sub(r"[.,'-\/:]", " ", usecase)
            corpus.append(usecase)

        # print(corpus)

        cv = CountVectorizer(max_features=None)
        X = cv.fit_transform(corpus).toarray()

        # print(X)

        y = new_df.iloc[:, 1:].values

        X_train = X
        y_train = y

        classifier = BinaryRelevance(classifier=SVC(), require_dense=[False, True])

        classifier.fit(X_train, y_train)

    if model_no == "2":
        df = pd.read_csv(
            f"./data/dataset_{model_no}.csv",
            delimiter="|",
            header=None,
            names=["test", "steps"],
        )

        for _, row in df.iterrows():
            split_list = str(row["steps"]).split(",")
            col_split_len = len(split_list)
            if col_split_len == 1 and split_list[0] == "nan":
                col_split_len = 0
            if col_split_len > steps_col_len:
                steps_col_len = col_split_len

        col_names.append("test")
        for i in range(steps_col_len):
            col_names.append("step_" + str(i))

        new_df = pd.DataFrame(columns=col_names)
        new_df["test"] = df["test"]

        for i in range(df.shape[0]):
            steps_split = str(df["steps"][i]).split(",")
            for y in range(steps_col_len):
                if y >= len(steps_split) or steps_split[0] == "nan":
                    new_df[f"step_{y}"][i] = 0
                else:
                    new_df[f"step_{y}"][i] = steps_split[y]

        new_df[new_df.columns[1:]] = new_df[new_df.columns[1:]].astype(int)

        corpus = []
        for i in range(len(df)):
            usecase = new_df["test"][i]
            usecase = usecase.lower()
            usecase = usecase.split()
            usecase = [
                ps.stem(word)
                for word in usecase
                if not word in set(stopwords.words("english"))
            ]
            usecase = " ".join(usecase)
            usecase = re.sub(r"[.,'-\/:]", " ", usecase)
            corpus.append(usecase)

        cv = CountVectorizer(max_features=None)
        X = cv.fit_transform(corpus).toarray()

        y = new_df.iloc[:, 1:].values

        X_train = X
        y_train = y

        classifier = BinaryRelevance(classifier=SVC(), require_dense=[False, True])

        classifier.fit(X_train, y_train)

    if model_no == "3":
        df = pd.read_csv(
            f"./data/dataset_{model_no}.csv",
            delimiter="|",
            header=None,
            names=["test", "expects"],
        )

        for _, row in df.iterrows():
            split_list = str(row["expects"]).split(",")
            col_split_len = len(split_list)
            if col_split_len == 1 and split_list[0] == "nan":
                col_split_len = 0
            if col_split_len > expects_col_len:
                expects_col_len = col_split_len

        col_names.append("test")
        for i in range(expects_col_len):
            col_names.append("expect_" + str(i))

        new_df = pd.DataFrame(columns=col_names)
        new_df["test"] = df["test"]

        for i in range(df.shape[0]):
            expects_split = str(df["expects"][i]).split(",")
            for y in range(expects_col_len):
                if y >= len(expects_split) or expects_split[0] == "nan":
                    new_df[f"expect_{y}"][i] = 0
                else:
                    new_df[f"expect_{y}"][i] = int(float(expects_split[y]))

        new_df[new_df.columns[1:]] = new_df[new_df.columns[1:]].astype(int)

        corpus = []
        for i in range(len(df)):
            usecase = new_df["test"][i]
            usecase = usecase.lower()
            usecase = usecase.split()
            usecase = [
                ps.stem(word)
                for word in usecase
                if not word in set(stopwords.words("english"))
            ]
            usecase = " ".join(usecase)
            usecase = re.sub(r"[.,'-\/:]", " ", usecase)
            corpus.append(usecase)

        cv = CountVectorizer(max_features=None)
        X = cv.fit_transform(corpus).toarray()

        y = new_df.iloc[:, 1:].values

        X_train = X
        y_train = y

        classifier = BinaryRelevance(classifier=SVC(), require_dense=[False, True])

        classifier.fit(X_train, y_train)

    with open(f"./ml_model/model_{model_no}.pkl", "wb") as file:
        pickle.dump(classifier, file)

    joblib.dump(cv, f"./ml_model/cv_{model_no}.pkl")
