# Readme

## How to run

```bash
docker build . -t reportback
docker run -it -p 8000:8000 reportback
```

The initial build is pretty slow, but incremental code changes should be pretty quick.

You can visit the docs at

```
http://localhost:8000/docs
```

For now, you have to log in to Auth0 as James to get a token. I will fix that.

## Architecture

You may need to get a Mermaid (mmd) renderer to see this rendered into a nice sequece Diagram

### Adventure workflow

```mermaid
sequenceDiagram
  Frontend->>Backend: Create Adventure (POST)
  Backend->>DB: Create Adventure
  Backend->>Frontend: ack (200) w/ created Adventure
  Frontend->>Frontend: Human goes on adventure
  Frontend->>Backend: Adventure ___ is completed (PUT)
  Backend-->>Frontend: ack (200 response code)
  Backend->>DB: Mark adventure completed
  Backend->>Twilio: Send these texts
  Twilio-->>Backend: ack (200 response code)
  Twilio->>Backend: Text sent sucessfully
  Backend-->>Twilio: ack (some TwiML)
  Backend->>DB: Text sent
  Frontend->>Backend: Adventure status? (GET)
  Backend->>DB: Adventure status?
  DB->>Backend: Adventure status
  Backend->>Frontend: Adventure  status

```
Notes:
- Frontend creates the UUID for idempotency
