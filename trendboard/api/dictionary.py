from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import requests
import json
import pandas as pd
import numpy as np
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

raw_df = pd.read_json(os.path.join(os.path.dirname(__file__), "..", "..", "data", "News_Category_Dataset_v3.json"), lines=True)

df = raw_df[['headline', 'category']].head(100)

# Generate embeddings, store in a dictionary so we can search for labels afterwards

top_n_dict = {}

def update_dictionary():
    embeddings = {}

    for i, x in df.iterrows():
        embeddings[tuple(model.encode(x['headline']))] = x['headline']


    vectors = [np.array(x) for x in embeddings.keys()] 

    dbscan = DBSCAN(eps = 1.0, min_samples = 2).fit(vectors)
    results = DBSCAN(eps = 1.0, min_samples = 2).fit_predict(vectors)

    grouped = {}

    # Group results into dictionary based on labels

    for v in dbscan.core_sample_indices_:
        if results[v] not in grouped:
            grouped[results[v]] = []
        grouped[results[v]].append(vectors[v])

    # Find representative point for each group

    reps = {}

    for key in grouped:
        elems = grouped[key]
        centroid = np.mean(elems, axis=0)
        
        min_dist = np.linalg.norm(elems[0] - centroid)
        min_i = 0

        for i, val in enumerate(elems[1:]):
            dist = np.linalg.norm(val - centroid)
            if dist < min_dist:
                min_dist = dist
                min_i = i

        reps[embeddings[tuple(elems[min_i])]] = len(elems)
        
    top_n_items = sorted(reps.items(), key=lambda item: item[1], reverse=True)[:min(5, len(reps))]

    for key, val in top_n_items:
        top_n_dict[key] = val

    # Convert the list of tuples back to a dictionary

def get_dictionary():
    return top_n_dict

update_dictionary()
print(get_dictionary())