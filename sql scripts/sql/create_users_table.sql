CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    email NVARCHAR(255) UNIQUE NOT NULL,
    username NVARCHAR(255) UNIQUE NOT NULL,
    first_name NVARCHAR(255),
    last_name NVARCHAR(255),
    hashed_password NVARCHAR(255),
    is_active BIT DEFAULT 1,
    INDEX idx_email (email),
    INDEX idx_username (username)
);
