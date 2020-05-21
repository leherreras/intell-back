from datetime import datetime

from entities import Session
from entities.books import Book, BookSchema
from entities.comments import CommentSchema, Comment


def get_comments():
    session = Session()
    comments_objects = session.query(Comment).all()

    schema = CommentSchema(many=True)
    comments = schema.dump(comments_objects)
    session.close()
    return comments


def create_comment_platform(data):
    posted_comment = CommentSchema(only=('text', 'id_book', 'id_user')) \
        .load(data)

    comment = Comment(**posted_comment)

    session = Session()
    session.add(comment)
    session.commit()

    new_comment = CommentSchema().dump(comment)
    session.close()

    return {'info': 'Save comment in DB'}


def get_books():
    session = Session()
    books_objects = session.query(Book).all()

    schema = BookSchema(many=True)
    books = schema.dump(books_objects)
    session.close()
    return books


def get_book(title):
    session = Session()
    book_objects = session.query(Book).filter_by(title=title)

    schema = BookSchema(many=True)
    books = schema.dump(book_objects)
    session.close()
    return books


def create_book_platform(data):
    data['publication_date'] = str(datetime.strptime(data['publication_date'], "%Y-%m-%d"))
    posted_book = BookSchema(only=('title', 'publication_date')) \
        .load(data)

    book = Book(**posted_book)

    session = Session()
    session.add(book)
    session.commit()

    new_book = BookSchema().dump(book)
    session.close()

    return {'info': 'Save book in DB'}
