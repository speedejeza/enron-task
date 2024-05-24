ALTER TABLE message ADD FULLTEXT(subject,body); 
-- Add a fulltext index to the subject and body columns of the message table.