## Follwing micro course "Creating, Reading, and Writing" from Kaggle
## https://www.kaggle.com/residentmario/creating-reading-and-writing

import pandas as pd

## Dataframes
print(pd.DataFrame({'Yes': [50,21], 'No': [131,2]}))

print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful'], 'Sue': ['Pretty good', 'Bland']}))

print(pd.DataFrame({
    'Bob': ['I liked it', 'It was awful'],
    'Sue': ['Pretty good', 'Bland']},
    index = ['Product A', 'Product B']
))

## Series

print(pd.Series(
    [1,2,3,4,5]
))

print(pd.Series(
    [30,35,40],
    index = ['2015 Sales', '2016 Sales', '2017 Sales'],
    name = 'Product A'
))

## Reading data files
wine_reviews = pd.read_csv('csv/wine_reviews.csv')

print(wine_reviews.shape)

print(wine_reviews.head())

wine_reviews = pd.read_csv('csv/wine_reviews.csv', index_col=0)
print(wine_reviews.head())
