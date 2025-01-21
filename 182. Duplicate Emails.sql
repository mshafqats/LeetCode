-- Implemented this query in PostgrSQL

SELECT email FROM person GROUP BY email HAVING COUNT(*) > 1;