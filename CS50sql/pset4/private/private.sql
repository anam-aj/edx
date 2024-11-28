CREATE VIEW "message" AS
SELECT substr("sentence", 1, 2)
FROM "sentences";
