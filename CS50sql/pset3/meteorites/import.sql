-- Temporary table
.import --csv meteorites.csv temp

-- Create new temporary table with proper id column
CREATE TABLE temp2 (
    id INTEGER,
    name TEXT,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC,
    PRIMARY KEY(id)
);

-- Insert data into temp2 table
INSERT INTO temp2 (name, class, mass, discovery, year, lat, long)
SELECT name, class, mass, discovery, year, lat, long
FROM temp;
