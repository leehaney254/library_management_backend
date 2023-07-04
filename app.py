from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7711@localhost/libraryManagement'
db = SQLAlchemy(app)

#Create the models
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    publication_date = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"Books:{self.title, self.author, self.genre, self.publisher, self.publication_date, self.description}"
    
    def __init__(self, title, author, genre, publisher, publication_date, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.publication_date = publication_date
        self.description = description

def format_book(book):
    return{
        "id": book.id,
        "title": book.title, 
        "author": book.author, 
        "genre": book.genre, 
        "publisher": book.publisher, 
        "publication_date": book.publication_date, 
        "description": book.description,
    }

# Create the database tables within the Flask application context
def create_all_tables():
    with app.app_context():
        db.create_all()


# Create Book
@app.route('/books', methods = ['POST'])
def create_book():
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

#Get all books
@app.route('/books', methods = ['GET'])
def get_books():
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
        book.update(title = title, author = author, genre = genre, publisher = publisher, publication_date = publication_date, description = description)
        db.session.commit()
        return {'book': format_book(book.one())}

if __name__ == '__main__':
    app.run