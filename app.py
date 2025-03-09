from flask import Blueprint
from config import db, create_app


main = Blueprint('main', __name__)

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created if they don't exist
    app.run(debug=True)
    # True: Run this app on debug mode
