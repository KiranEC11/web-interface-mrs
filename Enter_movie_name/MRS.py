#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# import os


# In[5]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# In[10]:


import pickle


# In[46]:


class Movie_recommender():
    def __init__(self):
        # print(os.getcwd())
        # print("=="*10, "\n")
        self.df_cleaned = pd.read_csv('cleaned_data.csv')
        self.titles = self.df_cleaned.original_title
        self.indices = pd.Series( self.titles.index, index = self.titles)
        
        # Specify the file path where you saved the cosine_sim variable
        file_path = 'linear_ker.pkl'

        # Load the variable from the file using pickle
        with open(file_path, 'rb') as file:
            self.linear_ker = pickle.load(file)

            
    def recommender(self,title):

        if self.df_cleaned.original_title.str.contains(title).value_counts().shape[0]==1:
            return 'The Movie is not in the data set'

        else:
            #find index of the given movie
            idx = self.indices[title]

            #find pairwise cosine similarity values
            cosine_sim_scores = list(enumerate(self.linear_ker[idx]))

            #sort based on the cosine similarity scores
            cosine_sim_scores_sorted = sorted(cosine_sim_scores , key = lambda x: x[1] , reverse = True)

            #select top 10  movies similar to given movie
            cosine_sim_scores_sorted_top_10 = cosine_sim_scores_sorted[1:11]

            #find indices of the top 10 movies
            cosine_top_10_indices = [i[0] for i in cosine_sim_scores_sorted_top_10 ]

            #find the top 10 most similar movies
            cosine_movie_list = self.df_cleaned['original_title'].iloc[cosine_top_10_indices]

            # take out the description about that movies
            description_list = self.df_cleaned['description'].iloc[cosine_top_10_indices]

            movies_rec = pd.DataFrame({'Recommended movies': cosine_movie_list.values, 'Overview':description_list })


            return movies_rec

