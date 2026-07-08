from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

movies = [ 
    { 
        "id": 1, 
        "title": "3 Idiots", 
        "director": "Rajkumar Hirani", 
        "genre": "Comedy Drama", 
        "language": "Hindi", 
        "release_year": 2009 
    }, 
    { 
        "id": 2, 
        "title": "Baahubali", 
        "director": "S S Rajamouli", 
        "genre": "Action Drama", 
        "language": "Telugu", 
        "release_year": 2015 
    } 
    ]

class Movie_update(BaseModel):
    title: str
    director: str
    genre: str
    language: str
    release_year: int


@app.get("/")
def about():
    return {"message": "Welcome to the Movie API!"}

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for existing_movie in movies:
        if existing_movie["id"]==movie_id:
            return existing_movie
    raise HTTPException(status_code=404, detail="Movie not found !!!")

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int,movie_update: Movie_update):
    for existing_movie in movies:
        if existing_movie["id"]==movie_id:
            existing_movie.update(movie_update.model_dump())
            return {
                "message": "Movie updated successfully",
                "movie": existing_movie
            }
    raise HTTPException(status_code=404, detail="Movie not found !!!")