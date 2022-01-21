# Define class with "class"
class Movie:
    # Define attributes of class
    mName = ""
    genre = ""
    mRating = ""
    setIn = ""
    budget = 0

# Inherit parent class attributes by referencing the class in parentheses
class Actor(Movie):
    fName = ""
    lName = ""
    age = 0
    bornIn = ""

class Director(Movie):
    fName = ""
    lName = ""
    moviesDirected = 0
    salary = 0
