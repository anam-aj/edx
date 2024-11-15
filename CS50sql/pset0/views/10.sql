SELECT entropy AS 'Highest 3 Entropy'
FROM views
WHERE artist = 'Hokusai'
ORDER BY entropy
LIMIT 3;
