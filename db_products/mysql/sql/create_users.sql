-- テーブルの作成
CREATE TABLE if not exists work.user (
    uid INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(255),
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- データの挿入
INSERT INTO user (nickname) VALUES
    ('John Doe'),
    ('Alice Smith'),
    ('Bob Johnson');