# EHAX In-Memory Database

A simple command-line in-memory key-value database built using Python.

## Features

- SET - Store a key-value pair
- GET - Retrieve the value of a key
- DEL - Delete a key
- EXISTS - Check whether a key exists
- SAVE - Save the database to a file
- LOAD - Load the database from a file
- EXIT - Exit the program
- Input validation and missing-key error handling

## Example Commands

SET name Vrinda
GET name
EXISTS name
DEL name
SAVE data.txt
LOAD data.txt
EXIT

## Technologies Used

- Python
- Python standard library (`ast`)
- Dictionary-based in-memory storage

## How to Run

Run the program using:

python database.py

Then enter commands at the `DB >` prompt.

## Example

DB > SET college DTU
OK

DB > GET college
DTU

DB > SAVE data.txt
Database saved successfully
