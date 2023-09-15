SELECT title, rating FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2012
ORDER BY rating DESC, title ASC;