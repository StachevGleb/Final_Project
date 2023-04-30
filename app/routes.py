from app import flask_app
from app.models import Book
from app import db


@flask_app.route('/insert/<int:book_id>')
def main_page(book_id):
    my_book = Book(book_id=book_id, title="my book", author="Bob", price=10)
    db.session.add(my_book)
    db.session.commit()

    return "hello"

@flask_app.route('/')
def get_all_books():
    return [{"book_id": book.book_id, "title": book.title} for book in Book.query.all()]


@flask_app.route('/health')
def health():
    return "ok"

@flask_app.shell_context_processor
def make_shell_context():
    return {
        "all_books": get_all_books()
    }
