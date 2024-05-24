# Ref: https://stackoverflow.com/questions/9680472/cant-find-fulltext-index-matching-the-column-list-indexes-is-set

ALTER TABLE message ADD FULLTEXT(subject,body);


SELECT subject, body, MATCH (subject,body)
AGAINST ("billionaire" IN NATURAL LANGUAGE MODE) as score, mid FROM message m 
WHERE MATCH (subject,body)
AGAINST ("billionaire" IN NATURAL LANGUAGE MODE);