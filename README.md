# Knockknock

Build only tested on Linux

How to run the project:

## Requirements
- virtualenv + python35 (optional)
- docker

## API + Front in Production
- with docker-compose (recommended)
```
# In dev
docker-compose up -d --build
docker-compose logs -f

# In prodcution on the raspberry pi
# Edit the file config.py
docker-compose -f prod.yml up -d --build
dokcer-compose logs -f
```

## API Dev + Front Dev
Go to http://localhost:8080

- without docker (development)
```
## ./webui
npm install
npm run dev
## ./api
source $(./pyenv create)
./pyenv export
./app.py
```
- DevAPI: http://localhost:5000/api
- DevFront: http://localhost:8080

## Database
- with docker
```
# Start mariadb container
cd database/
docker build -t testdb . && docker run -it -p 3306:3306
./create.sh

# Connect to database
mysql -h0.0.0.0 -uadmin -ppassword knockknock
```
