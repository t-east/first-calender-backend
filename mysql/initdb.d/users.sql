CREATE TABLE IF NOT EXISTS calendar.users (
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(30) NOT NULL,
    email VARCHAR(128) NOT NULL,
    password_hash VARCHAR(1024) NOT NULL,
    registered_at DATETIME NOT NULL, 
    last_login_at DATETIME NULL,
    updated_at DATETIME NULL,
    
    PRIMARY KEY (user_id)
);

birthday DATE NULL,