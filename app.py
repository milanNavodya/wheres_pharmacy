from flask import Blueprint
from config import db, create_app


main = Blueprint('main', __name__)

app = create_app()

if __name__ == '__main__':
    # db.create_all(app=create_app())
    app.run(debug=True)
    # True: Run this app on debug mode
