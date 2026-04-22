import json

# List
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "rating": 4.2},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "rating": 4.8},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "rating": 4.9},
    {"id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "rating": 4.7},
    {"id": 5, "title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy", "rating": 4.9},
    {"id": 6, "title": "Dune", "author": "Frank Herbert", "genre": "Sci-Fi", "rating": 4.5},
    {"id": 7, "title": "Foundation", "author": "Isaac Asimov", "genre": "Sci-Fi", "rating": 4.3},
    {"id": 8, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "rating": 4.1},
    {"id": 9, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "rating": 3.9},
    {"id": 10, "title": "The Shining", "author": "Stephen King", "genre": "Horror", "rating": 4.4},
    {"id": 11, "title": "It", "author": "Stephen King", "genre": "Horror", "rating": 4.2},
    {"id": 12, "title": "Neuromancer", "author": "William Gibson", "genre": "Sci-Fi", "rating": 4.0},
    {"id": 13, "title": "Snow Crash", "author": "Neal Stephenson", "genre": "Sci-Fi", "rating": 4.1},
    {"id": 14, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Classic", "rating": 4.6},
    {"id": 15, "title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "genre": "Fantasy", "rating": 4.8},
    {"id": 16, "title": "A Game of Thrones", "author": "George R.R. Martin", "genre": "Fantasy", "rating": 4.6},
    {"id": 17, "title": "Neuromancer", "author": "William Gibson", "genre": "Sci-Fi", "rating": 3.9},
    {"id": 18, "title": "The Road", "author": "Cormac McCarthy", "genre": "Dystopian", "rating": 4.0},
    {"id": 19, "title": "Fahrenheit 451", "author": "Ray Bradbury", "genre": "Dystopian", "rating": 4.5},
    {"id": 20, "title": "The Martian", "author": "Andy Weir", "genre": "Sci-Fi", "rating": 4.7},
    {"id": 21, "title": "Project Hail Mary", "author": "Andy Weir", "genre": "Sci-Fi", "rating": 4.9},
    {"id": 22, "title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fantasy", "rating": 3.8},
    {"id": 23, "title": "The Da Vinci Code", "author": "Dan Brown", "genre": "Thriller", "rating": 3.9},
    {"id": 24, "title": "Gone Girl", "author": "Gillian Flynn", "genre": "Thriller", "rating": 4.1},
    {"id": 25, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "genre": "Thriller", "rating": 4.3},
    {"id": 26, "title": "Dracula", "author": "Bram Stoker", "genre": "Horror", "rating": 4.0},
    {"id": 27, "title": "Frankenstein", "author": "Mary Shelley", "genre": "Horror", "rating": 4.1},
    {"id": 28, "title": "The Odyssey", "author": "Homer", "genre": "Classic", "rating": 4.3},
    {"id": 29, "title": "The Iliad", "author": "Homer", "genre": "Classic", "rating": 4.0},
    {"id": 30, "title": "The Catch-22", "author": "Joseph Heller", "genre": "Classic", "rating": 4.4}
]

with open('books.json', 'w') as f:
    json.dump(books, f, indent=4)