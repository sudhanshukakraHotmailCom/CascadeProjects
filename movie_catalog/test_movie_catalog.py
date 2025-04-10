import unittest
from movie_catalog import MovieCatalog, Movie

class TestMovieCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = MovieCatalog("movies_formatted.csv")

    def test_get_movies_comedy_2001_2003(self):
        result = self.catalog.get_movies("Comedy", 2001, 2003)
        expected = [
            Movie(id=131256, title="Feuer Eis & Dosenbier", publication_year=2002, genres=["Comedy"])
        ]
        self.assertEqual(list(result), expected)

    def test_get_movies_uncategorized(self):
        result = self.catalog.get_movies("Uncategorized", 1900, 2100)
        expected = [
            Movie(id=131260, title="Rentun Ruusu", publication_year=2001, genres=["Uncategorized"])
        ]
        self.assertEqual(list(result), expected)

    def test_get_movies_fantasy_1995(self):
        result = self.catalog.get_movies("Fantasy", 1995, 1995)
        expected = [
            Movie(id=1, title="Toy Story", publication_year=1995, genres=["Adventure", "Animation", "Children", "Comedy", "Fantasy"]),
            Movie(id=2, title="Jumanji", publication_year=1995, genres=["Adventure", "Children", "Fantasy"])
        ]
        self.assertEqual(list(result), expected)

if __name__ == '__main__':
    unittest.main()
