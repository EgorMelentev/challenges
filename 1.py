import csv

def csv_dict(variables_file: str):
    reader = csv.reader(open(variables_file, 'r'))
    result = {}
    for row in reader:
        key = row[0]
        result[key] = row[1]
    return result

def filter_by_rating(d: dict, rating: str):
    result = {}
    for item, star in d.items():
        if (star == rating):
            result[item] = star
    return result

csv_file_name = "rating.csv"
dictionary = csv_dict(csv_file_name)

rated = filter_by_rating(dictionary, "*****")

if rated == {}:
    print("No results found")
else:
    print(rated)