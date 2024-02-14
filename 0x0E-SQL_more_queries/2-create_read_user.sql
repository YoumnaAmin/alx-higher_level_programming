-- t
-- u
CREATE USER 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT SELECT on *.* to 'user_0d_1'@'localhost';
