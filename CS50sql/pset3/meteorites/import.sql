-- Temporary table
.import --csv meteorites.csv temp

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
    PRIMARY KEY(id)
);

-- Insert data into temp2 table
INSERT INTO temp2 (
    name,
    class,
    mass,
    discovery,
    year,
    lat,
    long
)
SELECT
    NULLIF(name, ''),
    NULLIF(class, ''),
    NULLIF(mass, ''),
    NULLIF(discovery, ''),
    NULLIF(year, ''),
    NULLIF(lat, ''),
    NULLIF(long, '')
FROM temp;
