from app import app, request, db
from app.models import Books, format_book

# Create Book and get all books
@app.route('/books', methods = ['POST', 'GET'])
def create_book():
    if request.method == 'POST':
      title = request.json['title']
      author = request.json['author']
      genre = request.json['genre']
      publisher = request.json['publisher']
      publication_date = request.json['publication_date']
      description = request.json['description']
      book = Books(title, author, genre, publisher, publication_date, description)
      db.session.add(book)
      db.session.commit()
      return format_book(book)
    elif request.method == 'GET':
        books = Books.query.order_by(Books.id.asc()).all()
        book_list = []
        for book in books:
            book_list.append(format_book(book))
        return {'book': book_list}

# One book
@app.route('/books/<id>', methods = ['GET', 'DELETE', 'PUT'])
def modify_book(id):
    if request.method == 'GET':
        book = Books.query.filter_by(id=id).one()
        formated_book = format_book(book)
        return {"book": formated_book}
    elif request.method == 'DELETE':
        book = Books.query.filter_by(id=id).one()
        db.session.delete(book)
        db.session.commit()
        return f'Book (id: {id}) deleted'
    elif request.method == 'PUT':
        book = Books.query.filter_by(id=id)
        title = request.json['title']
        author = request.json['author']
        genre = request.json['genre']
        publisher = request.json['publisher']
        publication_date = request.json['publication_date']
        description = request.json['description']
        book.update(dict(title = title, author = author, genre = genre, publisher = publisher, publication_date = publication_date, description = description))
        db.session.commit()
        return {'book': format_book(book.one())}