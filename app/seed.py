from app import db, app
from app.models import Reservations, Members, Books, create_all_tables, drop_all_tables


members_data = [
    {"name": 'Leehaney', "debt": 0, "email": 'leeahney@gmail.com', "phone_number": '+254'},
    {"name": 'Mike', "debt": 0, "email": 'mike@gmail.com', "phone_number": '+254'},
    {"name": 'Sarah', "debt": 0, "email": 'sarah@gmail.com', "phone_number": '+254'} 
]

books_data = [
    {
        "title": 'The 48 Laws of power', 
        "author": 'Robert Greene', "genre": 'Personal Growth',
        "publisher": 'Penguine Books', "publication_date": '12/05/2004', 
        "description": 'A very good book', 
        "image": 'https://nuriakenya.com/product/the-art-of-seduction-by-robert-greene/'
    },
    {
        "title": 'Art of Seduction', "author": 'Robert Greene', 
        "genre": 'Personal Growth', "publisher": 'Penguine Books',
        "publication_date": '12/05/2004', "description": 'A very good book',
        "image": 'https://nuriakenya.com/product/the-art-of-seduction-by-robert-greene/'
    },
    {
        "title": 'Who moved my cheese', "author": 'Spencer Johnson',
        "genre": 'Personal Growth', "publisher": 'Penguine Books',
        "publication_date": '8/09/1998', 
        "description": 'Who Moved My Cheese? is a simple parable that reveals profound truths. It is an amusing and enlightening story of four characters who live in a "Maze" and look for "Cheese" to nourish them and make them happy.', 
        "image": 'https://kibangabooks.com/product/who-moved-my-cheese-by-dr-spencer-johnson/'
    },
]

reservations_data = [
    {'book_id': 1, 'member_id': 1, 'returned': False}, 
    {'book_id': 2, 'member_id': 2, 'returned': False},
    {'book_id': 3, 'member_id': 1, 'return_date': '2023-07-07', 'returned': False},
]

def seed_data():
    #bring the app to context
    app.app_context().push()
    
    #Uncomment only if you have already created tables
    drop_all_tables()

    # To create new tables
    create_all_tables()

    # Create members
    members = [Members(**data) for data in members_data]

    # Create books
    books = [Books(**data) for data in books_data]

    # Create reservations
    reservations = [Reservations(**data) for data in reservations_data]

    # Add members and reservations to the session
    db.session.add_all(members)
    db.session.add_all(books)
    db.session.add_all(reservations)

    # Commit the session
    db.session.commit()
