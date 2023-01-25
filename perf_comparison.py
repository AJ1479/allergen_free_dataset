# import time
# from sklearn.metrics.pairwise import euclidean_distances
import time
from strsimpy.cosine import Cosine
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from strsimpy.damerau import Damerau
from strsimpy.jaro_winkler import JaroWinkler
from strsimpy.metric_lcs import MetricLCS
import pandas as pd
import numpy as np
# import nltk
# import sklearn
# from numpy import argmax
# # nltk.download('punkt')

df = pd.read_csv('./new_dataset2.csv')


search_strings = [
    'Corn Nuts Ranch Bag'.lower(),
    'Jolly Time Popcorn'.lower(),
    'Roasted Turkey Gravy'.lower(),
    'Simply Organic Seasoning'.lower(),
    'M&b Curry'.lower(),
    'French Fries with Sauce'.lower(),
    'Biscuits and Tea'.lower(),
    'Potato Chips'.lower(),
    'Chocolate Ice Cream'.lower(),
    'Choco Chip Cookies with Nuts'.lower(),
    'Cheese Popcorn'.lower(),
    'Cheese Sandwich'.lower(),
    'Gelatin Free Cookies'.lower(),
    'Jam and Butter'.lower(),
    'Organic Olive Oil for cooking'.lower(),
]

normalized_levenshtein = NormalizedLevenshtein()
cosine = Cosine(2)
damerau = Damerau()
jarowinkler = JaroWinkler()
metric_lcs = MetricLCS()
time_values = []
# print(df.head())

# print(normalized_levenshtein.distance("ABCDE", "ABCE"))


def calNL(inputString):
    ans = []
    t1 = time.perf_counter()
    for index, row in df.iterrows():
        ans.append([normalized_levenshtein.distance(
            inputString, row['name'].lower()), row['name']])
    t2 = time.perf_counter()
    ans.sort()
    print(f'Normalized Levenshtein: {ans[:3]}\n')
    timeCount = int(round((t2 - t1)*1000))
    return timeCount
    # print(f"Normalized Levenshtein took: {timeCount}ms")
    # time_values['NormalizedLevenshtein'] = timeCount


def calCo(inputString):
    ans = []
    t1 = time.perf_counter()
    for index, row in df.iterrows():
        p0 = cosine.get_profile(inputString)
        p1 = cosine.get_profile(row['name'].lower())
        ans.append([cosine.similarity_profiles(p0, p1), row['name']])
    t2 = time.perf_counter()
    ans.sort(reverse=True)
    print(f'Cosine Similarity: {ans[:3]}\n')

    timeCount = int(round((t2 - t1)*1000))
    # print(f"Cosine Similarity took: {timeCount}ms")
    # time_values['CosineSimilarity'] = timeCount
    return timeCount


def calJW(inputString):
    ans = []
    t1 = time.perf_counter()
    for index, row in df.iterrows():
        ans.append([jarowinkler.similarity(
            inputString, row['name'].lower()), row['name']])
    t2 = time.perf_counter()
    ans.sort(reverse=True)
    print(f'Jaro Winkler: {ans[:3]}\n')
    timeCount = int(round((t2 - t1)*1000))
    # print(f"Jaro Winkler took: {timeCount}ms")
    # time_values['JaroWinkler'] = timeCount
    return timeCount


def calDA(inputString):
    ans = []
    t1 = time.perf_counter()
    for index, row in df.iterrows():
        ans.append(
            [damerau.distance(inputString, row['name'].lower()), row['name']])
    t2 = time.perf_counter()
    ans.sort()
    print(f'Damerau Lev: {ans[:3]}\n')
    timeCount = int(round((t2 - t1)*1000))
    # print(f"Damerau took: {timeCount}ms")
    # time_values['Damerau'] = timeCount
    return timeCount


def calMLCS(inputString):
    ans = []
    t1 = time.perf_counter()
    for index, row in df.iterrows():
        ans.append([metric_lcs.distance(inputString, row['name']), row['name']])
    t2 = time.perf_counter()
    ans.sort()
    print(f'Metric LCS: {ans[:3]}\n')
    timeCount = int(round((t2 - t1)*1000))
    # print(f"Metric LCS took: {timeCount}ms")
    # time_values['MetricLCS'] = timeCount
    return timeCount


for i in search_strings:
    print(f'\n{i}----------------\n')
    time_values.append(
        [i,
         calNL(i),
         calCo(i),
         calJW(i),
         calDA(i),
         calMLCS(i)
         ])

print('-------runtimes in order-----')

for i in time_values:
    print(i)
