-- a script that will list all the cities of California that can be found in the database hbtn_0d_usa.

SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name like '%California%'
ORDER BY cities.id ASC;
