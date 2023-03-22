from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {
        'id': 1,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'year_published': 1951
    },
    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year_published': 1960
    },
    {
        'id': 3,
        'title': '1984',
        'author': 'George Orwell',
        'year_published': 1949
    }
]
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({'book': book})
    return jsonify({'error': 'Book not found'}), 404
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'book': new_book}), 201
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify({'book': book})
    return jsonify({'error': 'Book not found'}), 404
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'result': 'Book deleted'})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
