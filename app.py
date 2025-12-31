from flask import Flask, render_template, send_file, abort, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "Authors_Library.db")

def get_db():
    return sqlite3.connect(DB)

@app.route("/")
def index():
    search_query = request.args.get("query", "").strip()

    con = get_db()
    cur = con.cursor()

    if search_query:
        cur.execute("""
            SELECT book_id, title, author, language
            FROM free_books
            WHERE (
                LOWER(title) LIKE LOWER(?) OR
                LOWER(author) LIKE LOWER(?)
            )
            AND pdf_path IS NOT NULL
            ORDER BY book_id
        """, (f"%{search_query}%", f"%{search_query}%"))
    else:
        cur.execute("""
            SELECT book_id, title, author, language
            FROM free_books
            WHERE pdf_path IS NOT NULL
            ORDER BY book_id
            LIMIT 20
        """)

    books = cur.fetchall()
    con.close()
    return render_template("index.html", books=books, query=search_query)

@app.route("/read/<int:book_id>")
def read_book(book_id):
    con = get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT title, pdf_path FROM free_books WHERE book_id = ?",
        (book_id,)
    )
    row = cur.fetchone()
    con.close()

    if not row or row[1] is None:
        abort(404)

    title, pdf_path = row
    return render_template("reader.html", title=title, pdf_path=pdf_path)

@app.route("/pdf/<path:filename>")
def serve_pdf(filename):
    file_path = os.path.join(BASE_DIR, "pdfs", filename)
    if not os.path.exists(file_path):
        abort(404)
    return send_file(file_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)

