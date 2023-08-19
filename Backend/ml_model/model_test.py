import numpy as np
import pandas as pd

# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from skmultilearn.adapt import MLkNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, hamming_loss
from sklearn.feature_extraction.text import CountVectorizer
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.svm import SVC
import re

ps = PorterStemmer()

max_test_cases = 0
try:
    with open('./data/dataset.tsv', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            col_len = len(line.split('#'))
            if col_len > max_test_cases:
                max_test_cases = col_len
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")

col_names = []
for i in range(max_test_cases):
    col_names.append('col'+str(i))

df = pd.read_csv("./data/dataset.tsv", delimiter="#", header=None, names=col_names)
# print(df)

df = df.fillna(0)
df[df.columns[1:]] = df[df.columns[1:]].astype(int)
# print(df)

corpus = []


def format_text(df):
    corpus = []
    for i in range(len(df)):
        usecase = df['col0'][i]
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
    return corpus


corpus = format_text(df)
# print(corpus)

cv = CountVectorizer(max_features=None)
X = cv.fit_transform(corpus).toarray()
# print(X)

y = df.iloc[:, 1:].values
print(y.shape)
print(y)
import numpy as np
unique_classes = np.unique(y)
num_unique_classes = len(unique_classes)
print("Number of unique classes:", num_unique_classes)

# Split the dataset into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
X_train = X
y_train = y

# Setup the classifier
classifier = BinaryRelevance(classifier=SVC(), require_dense=[False, True])

# Train
classifier.fit(X_train, y_train)


def get_prediction(text):
    text = text.lower()
    text = text.split()
    text = [
        ps.stem(word) for word in text if not word in set(stopwords.words("english"))
    ]
    text = " ".join(text)
    text = re.sub(r"[.,'-\/:]", " ", text)
    text = cv.transform([text]).toarray()
    return text


# Predict
# y_pred = classifier.predict(cv.transform(['user login']).toarray())
# y_pred = classifier.predict(get_prediction("employee"))
# print(y_pred)

# # print(X_train)

# # Make predictions on the test set
# # y_pred = mlknn_classifier.predict(cv.transform(['save']).toarray())
# # print(y_pred)

# # Calculate accuracy and hamming loss
# # accuracy = accuracy_score(y_test, y_pred)
# # hamming_loss_value = hamming_loss(y_test, y_pred)

# # print("Accuracy:", accuracy)
# # print("Hamming Loss:", hamming_loss_value)