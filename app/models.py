from app import db, app

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

    