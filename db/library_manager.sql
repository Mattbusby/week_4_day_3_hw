DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  age INT
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  author_id INT REFERENCES authors(id) ON DELETE CASCADE
);








-- INSERT INTO authors (full_name, age) VALUES ('Terry Pratchett', 78);
-- INSERT INTO authors (full_name, age) VALUES ('J.R.R. Tolkein', 99);


-- INSERT INTO books (title, author) VALUES ('The colour of magic', 'Terry Pratchett');
-- INSERT INTO books (title, author) VALUES ('The light fantastic', 'Terry Pratchett');
-- INSERT INTO books (title, author) VALUES ('The Hobbit', 'J.R.R. Tolkein');

