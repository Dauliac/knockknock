CREATE TABLE IF NOT EXISTS ringtones (
  id INTEGER NOT NULL AUTO_INCREMENT,
  status INTEGER,
  replay_url VARCHAR(255),
  timestamp DATE,
  PRIMARY KEY (id)
);
