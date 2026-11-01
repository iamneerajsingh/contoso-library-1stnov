from flask import Flask, jsonify, request
 
from library import Library
 
app = Flask(__name__)
library = Library()
library.add_book("978-0132350884", "Clean Code", "Robert C. Martin")
library.add_book("978-1491950357", "Building Microservices", "Sam Newman")
 
 
@app.get("/health")
def health():
    return jsonify(status="ok")
 
 
@app.get("/books")
def list_books():
    return jsonify([vars(b) for b in library.books.values()])
 
 
@app.post("/loans")
def borrow():
    data = request.get_json()
    try:
        loan = library.borrow(data["isbn"], data["member_id"])
    except (KeyError, ValueError) as err:
        return jsonify(error=str(err)), 400
    return jsonify(isbn=loan.isbn, due_on=loan.due_on.isoformat()), 201
 
 
if __name__ == "__main__":
    app.run(debug=False)
 
