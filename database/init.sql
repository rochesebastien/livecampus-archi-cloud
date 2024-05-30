-- Table Blog
CREATE TABLE Blog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);

-- Table Article
CREATE TABLE Article (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    Ranking INT NOT NULL,
    blog_id INTEGER,
    FOREIGN KEY (blog_id) REFERENCES Blogs(id)
);