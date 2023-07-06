import pytest
import requests

# Test for creating a book
def test_create_book():
    url = 'http://localhost:5000/books'
    headers = {'Content-Type': 'application/json'}
    data = {
        'title': 'Title test',
        'author': 'Author test',
        'genre': 'Genre test',
        'publisher': 'Publisher test',
        'publication_date': '2023-07-05',
        'description': 'Description tetst',
        'image': 'Image test'
    }
    
    # We check the status code, if id was created, if there is a book
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    assert 'book' in response.json()
    assert 'id' in response.json()['book']