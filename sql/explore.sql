# Ref: https://stackoverflow.com/questions/9680472/cant-find-fulltext-index-matching-the-column-list-indexes-is-set

ALTER TABLE message ADD FULLTEXT(subject,body);


SELECT  mid, subject, body,
	MATCH (subject,body) AGAINST ('"I love committing fraud. No one will ever find out"' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION) as score 
FROM message m 
WHERE 
	MATCH (subject,body) AGAINST ('"I love committing fraud. No one will ever find out"' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION);