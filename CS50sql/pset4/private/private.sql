-- Create temporary view with id and phrase
CREATE VIEW "temp message" AS
SELECT "id", TRIM(substr("sentence", 98, 4)) AS "phrase"
FROM "sentences"
WHERE id = 14
UNION
SELECT "id", TRIM(substr("sentence", 3, 5))
FROM "sentences"
WHERE id = 114
UNION
SELECT "id", TRIM(substr("sentence", 72, 9))
FROM "sentences"
WHERE id = 618
UNION
SELECT "id", TRIM(substr("sentence", 7, 3))
FROM "sentences"
WHERE id = 630
UNION
SELECT "id", TRIM(substr("sentence", 12, 5))
FROM "sentences"
WHERE id = 932
UNION
SELECT "id", TRIM(substr("sentence", 50, 7))
FROM "sentences"
WHERE id = 2230
UNION
SELECT "id", TRIM(substr("sentence", 44, 10))
FROM "sentences"
WHERE id = 2346
UNION
SELECT "id", TRIM(substr("sentence", 14, 5))
FROM "sentences"
WHERE id = 3041;

-- Creates the required view "message"
CREATE VIEW "message" AS
SELECT "phrase"
FROM "temp message"
ORDER BY "id";
