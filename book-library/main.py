from fastapi import FastAPI
from schemas import Book 

app = FastAPI()
database = {}

# Assignment: Create a Book Library API using FastAPI

# Problem Statement:

# Design and implement a REST API for a Book Library using FastAPI. This API should be capable of performing basic CRUD operations (Create, Retrieve, Update, and Delete).

# Book Model:

# Each book should have the following attributes:

# id: a unique identifier for the book.
# title: the title of the book.
# author: the author of the book.
# year: the year the book was published.
# Tasks:

# Create a new book:

# Implement a POST request at the /books/ endpoint that takes the title, author, and year in the request body and returns the created book with its assigned id.
# Retrieve all books:
@app.post("/books/")
def addBook(id:int, book:Book):
    database[id] = book
    return database

# Implement a GET request at the /books/ endpoint that returns a list of all books.
@app.get("/books/")
def getBooks():
    return database
# Retrieve a book by id:


# Implement a GET request at the /books/{id} endpoint that returns the details of a specific book by id.
@app.get("/books/{id}")
def getBooks(id:int):
    return database[id]
# Update a book:


# Implement a PUT request at the /books/{id} endpoint that takes the id in the URL and the updated book details in the request body. It should update the book details for the given id.
@app.put("/books/{id}")
def getBooks(id:int, book:Book):
    database[id]= book
    return database
# Delete a book:

# Implement a DELETE request at the /books/{id} endpoint that deletes the specified book by id.
@app.delete("/books/{id}")
def delBook(id:int):
    del database[id]
    return database