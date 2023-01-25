# allergen-free-dataset

A project demonstrating the creation of an allergen-free dataset and recommendation engine.


## Features

- Creation of a dataset of allergen-free food items
- Corpus statistics of the created dataset
- Allergen-free product recommendations
- Performance comparison of popular algorithms

We aim to generate a dataset of food items and their corresponding ingredients that are free from allergens. To achieve this, we have a base dataset obtained [from Kaggle](https://www.kaggle.com/datasets/datafiniti/food-ingredient-lists) of popular food items from which we filter away the main allergen causing ingredients. 

To generate the performance comparison, we include `perf_comparison.py` which contains the benchmark for popular algorithms such as

- Normalized Levenshtein
- Cosine Similarity
- Jaro Winkler
- Damerau Levenshtein
- Metric LCS

We record and compare their runtimes and recommendations for the following search strings

```
Corn Nuts Ranch Bag
Jolly Time Popcorn
Roasted Turkey Gravy
Simply Organic Seasoning
M & b Curry
Potato French Fries with Sauce
Biscuits and Tea
Kidney Beans with Mango Juice and Water
Chocolate Ice Cream
Choco Chip Cookies with Nuts
Cheese Popcorn with Sprinkles
Cheese Sandwich
Gelatin Free Cookies
Jam and Butter
Organic Olive Oil for cooking
```

## Installation

The following python packages must be installed on your system

- pandas
- numpy
- strsimpy

```bash
    pip3 install pandas numpy strsimpy
```