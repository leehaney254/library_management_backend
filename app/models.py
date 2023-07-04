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


# Create the members model
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    debt = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Books:{self.id, self.name, self.email, self.debt, self.phone_number}"
    
    def __init__(self, name, email, debt, phone_number):
        self.name = name
        self.email = email
        self.debt = debt
        self.phone_number = phone_number

def format_member(member):
    return{
        "id": member.id,
        "name": member.name, 
        "debt": member.debt, 
        "email": member.email, 
        "phone_number": member.phone_number, 
    }

# Create the reservations model
class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, nullable=False)
    return_date = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Books:{self.id, self.book_id, self.member_id, self.return_date}"
    
    def __init__(self, book_id, member_id, return_date):
        self.book_id = book_id
        self.member_id = member_id
        self.return_date = return_date


# Create the database tables within the Flask application context
def create_all_tables():
    with app.app_context():
        db.create_all()