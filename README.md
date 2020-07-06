A simple app to organize your contacts.

### Packages used:
- Server
    - Flask (easy API creation)
    - Flask-Cors (cross-origin requests during local development)
    - UUID (unique identifiers)
- Client
    - Vue.js, Vue Router (minimal Vue-cli generated project)
    - Vue-Bootstrap (responsiveness out of the box)
    - axios (HTTP requests)

## Installation:
```
 cd server
 virtualenv env
 source env/bin/activate
 pip install -r requirements.txt
 export FLASK_APP=app.py
 export FLASK_ENV=development
 flask run
``` 
Navigate to http://localhost:5000

```
 cd client
 npm install
 npm start
```
Navigate to http://localhost:8080
