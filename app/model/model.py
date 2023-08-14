import pickle
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords 
from nltk.stem.snowball import SnowballStemmer
from pathlib import Path
import re

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
    "Normal Comment",
    "Toxic Comment",
    
]






def predict_pipeline(text):
    snowball = SnowballStemmer(language="english")
    stop_words = set(stopwords.words('english')) 
    text = text.lower()
    text = re.sub("[^a-zA-Z]", " ", text)
    text = word_tokenize(text)
    text = [i for i in text if i not in stop_words]
    text = [snowball.stem(i) for i in text]
    text = ' '.join(text)
    prediction = model.predict([text])
   
    return classes[prediction[0]]