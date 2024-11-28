CREATE VIEW "message" AS
SELECT substr("sentence", 98, 4)
FROM "sentences"
WHERE id = 14;
