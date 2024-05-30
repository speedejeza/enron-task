-- Ref: https://stackoverflow.com/questions/9680472/cant-find-fulltext-index-matching-the-column-list-indexes-is-set

ALTER TABLE message ADD FULLTEXT(subject,body);


SELECT  mid, sender, subject, body
FROM message m 
WHERE 
	MATCH (subject,body) AGAINST ('"energy trading" bankruptcy +(lay skilling)' IN NATURAL LANGUAGE MODE);