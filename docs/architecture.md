# Architecture

The application uses a layered approach:

Routes -> Services -> Repositories -> Database

- Routes handle requests and responses
- Services handle application logic and coordinate interactions between routes and repositories
- Repositories execute SQL queries
- Models represent application entities
