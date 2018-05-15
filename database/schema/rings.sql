CREATE TABLE IF NOT EXISTS rings (
  id INTEGER NOT NULL AUTO_INCREMENT,
  status INTEGER,
  stream_url VARCHAR(255),
  replay_url VARCHAR(255),
  timestamp DATE,
  PRIMARY KEY (id)
);
