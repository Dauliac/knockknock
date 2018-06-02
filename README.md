# Knockknock

Build only tested on Linux

How to run the project:

## Requirements
- virtualenv + python35 (optional)
- docker

## API + Front in Production
- with docker (recommended)
```
# Clean
./init remove

# Build
./init build

# Run
./init run

# Clean & Build & Run
./init up
```

## API Dev + Front Dev
Go to http://localhost:8080

- without docker (development)
```
## ./webui
npm install
npm run dev
## ./api
source $(./pyenv)
pip install -r requirement.txt
./main.py
```
DevAPI: http://localhost:5000/api
DevFront: http://localhost:8080

## Database
- with docker
```
# Start mariadb container
./database/init.sh
# Import tables
mysql -h0.0.0.0 -uadmin -ppassword knockknock < database/users.sql
mysql -h0.0.0.0 -uadmin -ppassword knockknock < database/events.sql

# Connect to database
mysql -h0.0.0.0 -uadmin -ppassword knockknock
```
