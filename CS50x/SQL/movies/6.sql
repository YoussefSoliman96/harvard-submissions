SELECT AVG(rating) FROM movies JOIN ratings ON movies.id = (SELECT id FROM movies WHERE year = 2012);