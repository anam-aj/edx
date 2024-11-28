CREATE VIEW "message" AS
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14
UNION
SELECT substr("sentence", 3, 5)
FROM "sentences"
WHERE id = 114
UNION
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14
UNION
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14
UNION
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14
UNION
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14
UNION;
