#Beginner    B B A A  
"""Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again."""
#Intermediate 

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf.append(tf[word][doc_index] * math.log(1/df[word],10)) 

        print(tfidf)

main(text)


#Advanced


import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def find_tfidf(text):
    docs = [line.lower().split() for line in text.split('\n')]
    vocabulary = list(set(text.lower().split()))
    N = len(docs)
    tf = {}
    df = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    data = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # if df[word] == 0:
            #     df[word] = 1
            tfidf.append(tf[word][doc_index] * math.log(1/df[word],10))
        data.append(tfidf)
    # print("data:\n",data)
    return data
    
def distance(row1, row2):
    total = 0
    for i in range(len(row1)):
        total = total + abs(row1[i] - row2[i])
    return np.sqrt(total)
    
def find_nearest_pair(data):
    n = len(data)
    dist = np.empty((n, n), dtype=float)
    # dist = np.array([[distance(sent1, sent2) for sent1 in data] for sent2 in data])
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = np.inf  # assign the value np.inf (the maximum possible floating point value)
            else:
                dist[i][j] = distance(data[i],data[j])
    nearest_index = np.unravel_index(np.argmin(dist),(n,n))
    print(nearest_index)
    return nearest_index
    

find_nearest_pair(find_tfidf(text))


