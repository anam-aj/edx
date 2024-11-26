-- Temporary table
.import --csv meteorites.csv temp;

-- Create new temporary table with proper id column
CREATE TABLE temp2 (
    id INTEGER,
    name TEXT NOT NULL,

)
