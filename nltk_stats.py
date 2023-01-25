import pandas as pd
import numpy as np

df = pd.read_csv('./new_dataset2.csv')

ing_lens = []
word_count = []
count = 0
nonEnglish = []


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


for index, row in df.iterrows():
    count += 1
    if not isEnglish(row['name']):
        nonEnglish.append(row['name'])
    ing_lens.append(len(row['name']))
    word_count.append(len(row['name'].split(' ')))

print(f'Number of rows {count}')
print(f'Non english count: {len(nonEnglish)}')
print('Number of words')
print(f'word count {len(word_count)}')
print(f'max word count {max(word_count)}')
print(f'min word count {min(word_count)}')
print(f'avg word count {sum(word_count)/len(word_count)}')
print('-----')

print(max(ing_lens))
print(min(ing_lens))

print(sum(ing_lens) / len(ing_lens))

# print('---repeated values---')
# print(df['name'].value_counts())

# df1 = pd.Series(ing_lens).value_counts()
# print(df1)

print('---- more complex stuff ----')
wordCountAvg = sum(word_count)/len(word_count)

biggerWords = 0
for index, row in df.iterrows():
    if len(row['name']) > wordCountAvg:
        biggerWords += 1

print(f'{biggerWords} words longer than average')

print('---- new stuff ----')

vocab = set()
ingsPerFood = []
totalWords = 0
totalIngCount = 0
totalIngs = []

for index, row in df.iterrows():
    food_name = row['name']
    ings = row['value'].split(',')

    totalIngCount += len(ings)
    totalIngs.extend(ings)

    ingsPerFood.append(len(ings))

    vocab.update(ings)

    totalWords += len(food_name.split(' '))
    totalWords += len(ings)

print(len(vocab))
print(f"Total ingredients: {totalIngCount}")

totalIngCharCount = 0

for i in totalIngs:
    # print(i)
    totalIngCharCount += len(i)

print(f"Avg chars in ings: {totalIngCharCount/totalIngCount}")


print(f'max ings per food: {max(ingsPerFood)}')
print(f'min ings per food: {min(ingsPerFood)}')
print(f'avg ings per food: {sum(ingsPerFood)/len(ingsPerFood)}')
print(f'Total word count: {totalWords}')
