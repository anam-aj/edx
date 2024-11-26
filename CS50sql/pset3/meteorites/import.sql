-- Temporary table
.import --csv meteorites.csv temp;

-- Create new temporary table with proper id column
CREATE TABLE temp2 (
    id INTEGER,
    name TEXT DEFAULT NULL,
    class TEXT DEFAULT NULL,
    mass NUMERIC DEFAULT NULL,
    discovery TEXT DEFAULT NULL,
    year NUMERIC DEFAULT NULL,
    lat NUMERIC DEFAULT NULL,
    long NUMERIC DEFAULT NULL,
);

-- 
