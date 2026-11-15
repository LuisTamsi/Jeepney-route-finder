# Jeepney route finder

A small Flask API for managing jeepney routes.

## Run

```powershell
python -m pip install -r requirements.txt
python main.py
```

The local development server listens at http://127.0.0.1:5000.
Use `/api/v1/routes` to list routes; the root URL has no page.

## Endpoints

| Method | URL | Result |
| --- | --- | --- |
| GET | `/api/v1/routes` | List routes |
| GET | `/api/v1/routes/<route_number>` | Get one route |
| POST | `/api/v1/routes/create/` | Create a route |
| PUT | `/api/v1/routes/update/<route_number>` | Update supplied fields |
| DELETE | `/api/v1/routes/<route_number>` | Delete a route |

The existing PUT URL `/routes/update/<route_number>` also works.

Create requests require a JSON object with `route_number`, `origin`,
`destination`, and `fare`. Updates accept any non-empty subset of these fields.
Route numbers must be unique, non-empty strings or integers; integers are
stored as strings. Origin and destination must be non-empty strings, and fare
must be a finite number greater than or equal to zero. Unknown fields are rejected.
Invalid payloads return JSON errors with HTTP 400, and missing routes return 404.

```json
{"route_number": "16", "origin": "Terminal", "destination": "Market", "fare": 15}
```

## Current limitations

Route data lives in memory and resets when the server restarts. This project
provides CRUD endpoints; it does not calculate journeys or transfers. It has no
authentication and uses Flask's development server for local use.
