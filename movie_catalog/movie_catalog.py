from dataclasses import dataclass
from typing import List, Iterable
import csv
from collections import defaultdict

@dataclass
class Movie:
    id: int
    title: str
    publication_year: int
    genres: List[str]

class MovieCatalog:
    def __init__(self, data_file_path: str):
        # Store movies by genre for efficient lookup
        self.movies_by_genre = defaultdict(list)
        
        # Parse the CSV file
        with open(data_file_path, 'r') as file:
            # Skip header line that starts with #
            next(file)
            
            reader = csv.reader(file)
            for row in reader:
                movie_id, title, year, genres = row
                movie = Movie(
                    id=int(movie_id),
                    title=title,
                    publication_year=int(year),
                    genres=genres.split('|')
                )
                
                # Add movie to each of its genres
                for genre in movie.genres:
                    self.movies_by_genre[genre].append(movie)
                    
        # Sort movies in each genre by id for consistent output
        for movies in self.movies_by_genre.values():
            movies.sort(key=lambda x: x.id)

    def get_movies(self, genre: str, start_year: int, end_year: int) -> Iterable[Movie]:
        """
        Returns movies matching the given genre and year range (inclusive).
        """
        # Get all movies for the requested genre
        matching_movies = self.movies_by_genre.get(genre, [])
        
        # Filter by year range
        return [
            movie for movie in matching_movies
            if start_year <= movie.publication_year <= end_year
        ]
