from app import app
from app.models import Books, Members


if __name__ == "__main__":
    app.run(host="0.0.0.0")
