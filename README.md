# Digital Library

based on Django REST Framework, running in Docker Compose

Application stores titles (with additional data) of games, books and videos in our <i>digital library</i>. You can add, modify, delete and search a record.

### How to start:
1. In root of project create .env file. Fill it with following values:

- DB_USER=<db_user>
- DB_PASS=<db_pass>
- DB_NAME=<db_name>
- API_KEY=<api_key>

2. Run in project's root catalog: docker-compose up --build

### Endpoints:
- /games/
- /books/
- /videos/
- /search/ - for each of above endpoint you can use search, providing name of field as "key" and name of searched value as "value", e.g.:
    
    <i>/games/search?key=title&value=Cyberpunk 2077</i>