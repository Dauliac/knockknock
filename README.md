# Knockknock

How to run the project:

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
