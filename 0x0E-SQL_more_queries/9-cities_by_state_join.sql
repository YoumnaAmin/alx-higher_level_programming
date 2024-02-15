-- t
-- u
SELECT cities.id, cities.name, states.name
FROM states INNER JOIN cities on cities.state_id = states.id
ORDER BY cities.id ASC;
