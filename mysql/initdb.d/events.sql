CREATE TABLE IF NOT EXISTS calendar.events (
    event_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(128) NOT NULL,
    description_text VARCHAR(1024) NULL,
    from_date DATETIME NOT NULL,
    to_date DATETIME NOT NULL,
    is_all_day BOOLEAN NULL,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    created_at DATETIME NOT NULL,
    
    PRIMARY KEY (event_id)
);
