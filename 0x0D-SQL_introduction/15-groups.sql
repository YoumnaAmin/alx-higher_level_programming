--  Lists the number of records
--  in the table second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
