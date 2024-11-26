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
FROM temp
WHERE nametype != 'Relict'
ORDER BY year, name;

-- Delete table 'temp'
DROP TABLE temp;

-- Rename 'temp2' to 'meteorites'
ALTER TABLE temp2
RENAME TO meteorites;

-- Round the value to 2 decimal places
UPDATE meteorites
SET mass = ROUND(mass, 2),
    lat = ROUND(lat, 2),
    long = ROUND(long, 2);
