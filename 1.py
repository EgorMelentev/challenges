import pandas as pd

def filter_by_rating(d, rating):
    result = {}
    for item, star in d.items():
        if (star == rating):
            result[item] = star
    return result

dictionary = pd.read_csv('rating.csv', header=None, index_col=0, squeeze=True).to_dict()

rated = filter_by_rating(dictionary, "******")
if rated == {}:
    print("No results found")
else:
    print(rated)