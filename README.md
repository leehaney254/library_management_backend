# library_management
This is the backend application for the library management system

https://www.youtube.com/watch?v=DlNIXC9SaF4

drawSQL
https://drawsql.app/teams/leehaneys-team/diagrams/library-management

tut
https://www.youtube.com/watch?v=RcQwcyyCOmM


from app import db, app
from app.models import Reservations, Members, create_all_tables, drop_all_tables

app.app_context().push()
lee = Members(name='Leehaney', debt=0, email='leeahney@gmail.com', phone_number='+254')
mike = Members(name='Mike', debt=0, email='mike@gmail.com', phone_number='+254')
sarah = Members(name='Sarah', debt=0, email='sarah@gmail.com', phone_number='+254') 
db.session.add_all([lee, mike, sarah])
db.session.commit()

reservation1 = Reservations(member_id=lee.id, returned=False) 
reservation2 = Reservations(member_id=mike.id, returned=False)
reservation3 = Reservations(member_id=lee.id, return_date="2023-07-07", returned=False)
db.session.add_all([reservation1, reservation2, reservation3])
db.session.commit() 
