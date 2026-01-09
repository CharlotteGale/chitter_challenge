DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id PRIMARY KEY SERIAL,
    author VARCHAR(255) NOT NULL,
    peep TEXT NOT NULL,
    time_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO peeps (author, peep) VALUES (
    ('test author_1', 'this is a test peep'),
    ('test author_2', 'this is another test peep')
);