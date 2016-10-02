# API Documentation

## List cinema halls

- Definition: `GET /halls`

- Example: `$ curl http://localhost:5000/halls`

## List movies

- Definition: `GET /movies`
- Example: `$ curl http://localhost:5000/movies`

## Retrieve a movie

- Definition: `GET /movies/<movieID>`
- Example: `$ curl http://localhost:5000/movies/1`

## Retrieve a movie's showtime

- Definition: `GET /movies/<movieID>/<showtime>`
- Example: `$ curl http://localhost:5000/movies/1/1140`

## Purchase a movie ticket

- Definition: `POST /movies/<movieID>/<showtime>`
- Example: `$ curl -u "admin:password" -H "Content-Type:application/json" -X POST http://localhost:5000/movies/1/1140 -d '{"name": "Aragorn II Elessar"}'`
