import pandas as pd

df = pd.read_csv(r'dataset.csv')

c = 0
d = 0
toDrop = []
allergens = ['milk', 'egg', 'nut', 'almond', 'pecan', 'soy', 'wheat', 'fish']

for i in df['features.value']:
    if isinstance(i, float):
        toDrop.append(c)
    elif(any(list(map(lambda x: i.lower().find(x) != -1, allergens)))):
        toDrop.append(c)
    c = c + 1

df.drop(toDrop, inplace=True)


df.to_csv('new_dataset4.csv')

print(toDrop)
