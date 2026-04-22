import json

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

all_data = load_data('books.json')

# Titles with 'Fantasy' genres
fantasy_titles = [b['title'] for b in all_data if b['genre'] == 'Fantasy']
print(fantasy_titles)

# Titles with a rating 4.7 or higher
highly_rated = [b['title'] for b in all_data if b['rating'] >= 4.7]
print(highly_rated)

# Author list
unique_authors = {b['author'] for b in all_data}
print(unique_authors)

# Title-Author
title_author = [f"{b['title']} by {b['author']}" for b in all_data]
print(title_author)

# Title by Author with a 'Sci-Fi' genre
scifi_catalog = [f"{b['title']} by {b['author']}" for b in all_data if b['genre'] == 'Sci-Fi']
print(scifi_catalog)