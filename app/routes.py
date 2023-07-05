from app import app, request, db
from app.models import Books, format_book, Members, format_member, Reservations, format_reservation

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
      image = request.json['image']
      book = Books(title, author, genre, publisher, publication_date, description, image)
      db.session.add(book)
      db.session.commit()
      formated_book = format_book(book)
      return {"book": formated_book}
    elif request.method == 'GET':
        books = Books.query.order_by(Books.id.asc()).all()
        book_list = []
        for book in books:
            book_list.append(format_book(book))
        return {'books': book_list}

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
        image = request.json['image']

        # Update the book object
        book.update(dict(title = title, author = author, genre = genre, publisher = publisher, publication_date = publication_date, description = description, image = image))
        db.session.commit()
        return {'books': format_book(book.one())}


# Create Member and get all members
@app.route('/members', methods = ['POST', 'GET'])
def create_member():
    if request.method == 'POST':
      name = request.json['name']
      email = request.json['email']
      debt = request.json['debt']
      phone_number = request.json['phone_number']
      member = Members(name, email, debt, phone_number)
      db.session.add(member)
      db.session.commit()
      return format_member(member)
    elif request.method == 'GET':
        members = Members.query.order_by(Members.id.asc()).all()
        members_list = []
        for member in members:
            members_list.append(format_member(member))
        return {'members': members_list}
    
# One member
@app.route('/members/<id>', methods = ['GET', 'DELETE', 'PUT'])
def modify_member(id):
    if request.method == 'GET':
        member = Members.query.filter_by(id=id).one()
        formated_member = format_member(member)
        return {"book": formated_member}
    elif request.method == 'DELETE':
        member = Members.query.filter_by(id=id).one()
        db.session.delete(member)
        db.session.commit()
        return f'Member (id: {id}) deleted'
    elif request.method == 'PUT':
        member = Members.query.filter_by(id=id)
        name = request.json['name']
        email = request.json['email']
        debt = request.json['debt']
        phone_number = request.json['phone_number']
        member.update(dict(name = name, email = email, debt = debt, phone_number = phone_number))
        db.session.commit()
        return {'member': format_member(member.one())}
    
# Create Reservation and get all reservation
@app.route('/reservations', methods = ['POST', 'GET'])
def create_reservation():
    if request.method == 'POST':
      book_id = request.json['book_id']
      member_id = request.json['member_id']
      if 'return_date' in request.json:
         return_date = request.json['return_date']
      else:
        return_date = None
      returned = request.json['returned']
      reservation = Reservations(book_id, member_id, returned, return_date)
      db.session.add(reservation)
      db.session.commit()

      formatted_reservation = combine_reservation(reservation)
      return formatted_reservation
    elif request.method == 'GET':
        reservations = Reservations.query.order_by(Reservations.id.asc()).all()
        reservation_list = []
        for reservation in reservations:
          reservation_list.append(combine_reservation(reservation))
        return {'reservations': reservation_list}
    
# One reservation
@app.route('/reservations/<id>', methods = ['GET', 'DELETE', 'PUT'])
def modify_reservation(id):
    if request.method == 'GET':
        reservation = Reservations.query.filter_by(id=id).one()
        formatted_reservation = combine_reservation(reservation)
        return {"reservation": formatted_reservation}
    elif request.method == 'DELETE':
        member = Members.query.filter_by(id=id).one()
        db.session.delete(member)
        db.session.commit()
        return f'Member (id: {id}) deleted'
    elif request.method == 'PUT':
        member = Members.query.filter_by(id=id)
        name = request.json['name']
        email = request.json['email']
        debt = request.json['debt']
        phone_number = request.json['phone_number']
        member.update(dict(name = name, email = email, debt = debt, phone_number = phone_number))
        db.session.commit()
        return {'member': format_member(member.one())}
    
# Creates a combination of book, member and reservation
def combine_reservation(reservation):
    # Retrieve the book and member objects
            book = Books.query.get(reservation.book_id)
            member = Members.query.get(reservation.member_id)
            # Format data for frontend
            formatted_member = format_member(member)
            formatted_book = format_book(book)
            return format_reservation(reservation, formatted_book, formatted_member)