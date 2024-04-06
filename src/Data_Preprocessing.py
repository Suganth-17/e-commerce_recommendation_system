import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
from nltk.stem.wordnet import WordNetLemmatizer


class DataPreProcessing:

    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame
    def drop_duplicates(self) -> pd.DataFrame:
        data_frame = self.data_frame.drop_duplicates(subset ="product_name", 
                     keep = "first")
        return data_frame
    
class MetaCreation:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame
        self.lem = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english')) 
        self.exclude = set(string.punctuation)
    
    def filter_keywords(self, doc) -> list:
        doc=doc.lower()
        stop_free = " ".join([i for i in doc.split() if i not in self.stop_words])
        punc_free = "".join(ch for ch in stop_free if ch not in self.exclude)
        word_tokens = word_tokenize(punc_free)
        filtered_sentence = [(self.lem.lemmatize(w, "v")) for w in word_tokens]
        return filtered_sentence
                
    def create_meta(self) -> pd.DataFrame:
        data_frame_copy = self.data_frame.copy()
        data_frame_copy['product'] = data_frame_copy['product_name'].apply(self.filter_keywords)
        data_frame_copy['main_category'] = data_frame_copy['main_category'].astype("str").apply(self.filter_keywords)
        data_frame_copy['sub_category'] = data_frame_copy['sub_category'].astype("str").apply(self.filter_keywords)
        data_frame_copy["all_meta"]=data_frame_copy['product']+data_frame_copy['main_category'] + data_frame_copy['sub_category']
        data_frame_copy["all_meta"] = data_frame_copy["all_meta"].apply(lambda x: ' '.join(x))
        self.data_frame.loc[:, 'all_meta'] = list(data_frame_copy['all_meta'])
        return self.data_frame