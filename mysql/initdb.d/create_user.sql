CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(30) NOT NULL,
    email VARCHAR(128) NOT NULL,
    birthday DATE NULL,
    PRIMARY KEY (id)
);