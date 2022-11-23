
## Development

```
cd app
docker-compose up -d --build
```

### Load Fixtures

```
docker-compose exec events python manage.py loaddata events.json
```


### Run Tests

```
docker-compose exec events
```
#### Run tests with coverage report
```
docker-compose exec events pytest -p no:warnings --cov=. --cov-report html
```

### Code formatting
```
docker-compose exec events black --exclude=migrations .
docker-compose exec events isort .
docker-compose exec events flake8 .
```


### Using the app

To test the app go to http://localhost:8009/

You can login with this credentials for the test user

```
username: test@email.com
password: Password123$
```

You can see the api documentaction on http://localhost:8009/swagger-docs/