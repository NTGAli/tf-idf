import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import numpy as np
import csv
import json


def getList(q):
    #len : 4654
    global res
    data = pd.read_csv("digiato.csv")
    titleList = []
    urlList = []
    txtList = []
    cosinList = []

    print(data["title"][:10])

    #tf-idf
    vectorizer = TfidfVectorizer()
    # tfidf_docs = vectorizer.fit_transform(data['text'].values.astype('U'))
    tfidf_docs = vectorizer.fit_transform(data['title'])

    # print(list(vectorizer.vocabulary_.keys())[:10])

    query = q

    tfidf_query = vectorizer.transform([query])[0]

    cosines = []
    for d in tqdm(tfidf_docs):
        cosines.append(float(cosine_similarity(d, tfidf_query)))
    k = 10
    # print(data['title'][0])
    sorted_ids = np.argsort(cosines)
    for i in range(k):
        cur_id = sorted_ids[-i-1]
        # qList.append(data['title'][cur_id])
        #res = data.loc[[cur_id]]
        # print(data.loc[[cur_id]])
        titleList.append(data['title'][cur_id])
        urlList.append(data['url'][cur_id])
        txtList.append(data['text'][cur_id])
        cosinList.append(cosines[cur_id])
        #qList = [cosines[cur_id], data['title'][cur_id]]
        #print(cosines[cur_id], data['title'][cur_id])

    return titleList, urlList, txtList, cosinList

if __name__ == '__main__':
    ## important : if you want to observe UI, run MainWindow
    print("important : if you want to observe UI, run MainWindow")
    myList = getList("متاورس")
    # for i in myList:
    #     print(i)



