from FlaskBlog import app, db, User
# from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

# Ensure the app context is available
with app.app_context():
    try:
        # Create users with hashed passwords
        # user_1 = User(username='Richik', email='richikraj30@gmail.com', password = 'password')
        user_2 = User(username='Zeher_Gulshan', email='zehergulshan@gmail.com', password = 'password')

        # Add users to the session
        # db.session.add(user_1)
        db.session.add(user_2)

        # Commit the changes to the database
        db.session.commit()

        print("Users added successfully!")

    except IntegrityError as e:
        db.session.rollback()  # Rollback in case of error
        print(f"Failed to add users: {str(e)}")
