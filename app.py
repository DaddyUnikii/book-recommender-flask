from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Data buku dummy
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fantasy"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help"},
    {"id": 3, "title": "Dune", "author": "Frank Herbert", "genre": "Sci-Fi"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Classic"},
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    recommended = [b for b in books if b['genre'] == genre]
    if not recommended:
        recommended = random.sample(books, 2)
    return render_template('recommendations.html', books=recommended, genre=genre)

if __name__ == '__main__':
    app.run(debug=True)
