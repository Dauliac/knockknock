CREATE TABLE IF NOT EXISTS ringtones (
  id INTEGER NOT NULL AUTO_INCREMENT,
  status INTEGER,
  replay_url VARCHAR(255),
  timestamp DATETIME,
  PRIMARY KEY (id)
);

INSERT INTO ringtones(status, replay_url, timestamp) VALUES(1, '0.0.0.0:8080/stream', NOW());
INSERT INTO ringtones(status, replay_url, timestamp) VALUES(2, '0.0.0.0:8080/stream', NOW());
INSERT INTO ringtones(status, replay_url, timestamp) VALUES(1, '0.0.0.0:8080/stream', NOW());
INSERT INTO ringtones(status, replay_url, timestamp) VALUES(1, '0.0.0.0:8080/stream', NOW());
INSERT INTO ringtones(status, replay_url, timestamp) VALUES(3, '0.0.0.0:8080/stream', NOW());
INSERT INTO ringtones(status, replay_url, timestamp) VALUES(1, '0.0.0.0:8080/stream', NOW());

