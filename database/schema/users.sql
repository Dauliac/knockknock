CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT,
  email VARCHAR(255),
  password VARCHAR(255),
  auth_token VARCHAR(255),
  admin_level INTEGER,
  last_login DATE,
  created_at DATE,
  PRIMARY KEY (id)
);

