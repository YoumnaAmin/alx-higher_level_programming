-- t
-- u
SELECT cities.id, cities.name, states.name
FROM states NATURAL JOIN cities
ORDER BY cities.id ASC;
