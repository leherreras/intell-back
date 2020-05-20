from flask import request, jsonify
from flask_classy import FlaskView, route

from .controller import get_comments, create_comment_platform, get_books, get_book, create_book_platform


class BookView(FlaskView):

    def index(self):
        books = get_books()
        return jsonify(books)

    def get(self, bookname):
        book = get_book(bookname)
        return jsonify(book)

    def post(self):
        data = request.form.to_dict()
        message = create_book_platform(data)
        return jsonify(message)

    @route('/comment/', methods=['POST', 'GET'])
    def comment(self):
        if request.method == 'POST':
            data = request.form.to_dict()
            message = create_comment_platform(data)
            return jsonify(message)
        if request.method == 'GET':
            comments = get_comments()
            return jsonify(comments)
