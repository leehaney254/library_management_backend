from flask import Flask
app = Flask(__name__)

# Books route
@app.route("/books")
def books():
    return {"books": ["book1", "book2", "book3"]}

if __name__ == "__main__":
    app.run(debug=True)