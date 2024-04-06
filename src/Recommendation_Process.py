import pandas as pd
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
from nltk.stem.wordnet import WordNetLemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Vectorizer:
    def __init__(self, entire_data_frame: pd.DataFrame, customer_data_frame: pd.DataFrame) -> None:
        self.lem = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english')) 
        self.exclude = set(string.punctuation)
        self.entire_data_frame = entire_data_frame
        self.customer_data_frame = customer_data_frame

    def tf_idf_vectorizer(self, recommended_nodes: list):
        tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
        recommended_data_frame = self.entire_data_frame[self.entire_data_frame['sub_category'].isin(recommended_nodes)]
        tfidf_recommended_matrix = tf.fit_transform(recommended_data_frame['all_meta'])
        cosine_sim = cosine_similarity(tfidf_recommended_matrix, tfidf_recommended_matrix)
        return cosine_sim, tfidf_recommended_matrix
    
    def top_recommendations(self, cosine_sim_matrix, meta, top_n= 15):
        indx = self.entire_data_frame.index[self.entire_data_frame['all_meta'] == meta][0]
        sim_scores = list(enumerate(cosine_sim_matrix[indx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1] 
        product_similarity_dict = {}
        product_indices = [i[0] for i in sim_scores]
        for idx in range(top_n):
            key = self.entire_data_frame['product_name'].iloc[product_indices[idx]]
            product_similarity_dict[key]= sim_scores[idx][1]
        return product_similarity_dict

    def get_recommendations(self, cosine_sim, product_meta_list)-> list:
        recommended_products_list = []
        for indx in range(len(product_meta_list)):
            recommended_products_list.append(self.top_recommendations(cosine_sim, product_meta_list[indx]))
        return recommended_products_list
    
    def get_recommendations_1(self, cosine_sim, product_meta_list, tfidf_recommended_matrix)-> list:
        index_list = []
        for indx in range(len(product_meta_list)):
            index = self.entire_data_frame.index[self.entire_data_frame['all_meta'] == product_meta_list[indx]][0]
            index_list.append(index)
        user_vector = tfidf_recommended_matrix[index_list].mean(axis=0)
        similarity_scores = cosine_similarity(np.asarray(user_vector), tfidf_recommended_matrix).flatten()
        recommended_item_indices = similarity_scores.argsort()[::-1]
        
        index_score_pairs = list(zip(recommended_item_indices, similarity_scores))

        sorted_pairs = sorted(index_score_pairs, key=lambda x: x[1], reverse=True)

        sorted_indices, sorted_scores = zip(*sorted_pairs)
        recommended_products_list = []

        for index, score in zip(sorted_indices, sorted_scores):
            if index not in index_list:
                product_similarity_dict = {}
                product_similarity_dict[self.entire_data_frame['product_name'][index]] = [score, self.entire_data_frame['sub_category'][index]]
                recommended_products_list.append(product_similarity_dict)
        return recommended_products_list