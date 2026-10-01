# iqAudi — Render deployment

## What this deployment provides

The Render service hosts the rebranded iqAudi web viewer and persistent run storage.
The underlying security engine uses Docker sandboxes, so the recommended architecture is:

**iqAudi Web (Render) → iqAudi Worker (Docker-capable host) → run data → iqAudi Web**

The included `render.yaml` deploys the viewer safely. It does **not** pretend that a
normal Render web service can replace the Docker execution worker.

## Deploy

1. Push this repository to your GitHub account.
2. In Render, choose **New → Blueprint** and select the repository.
3. Render reads `render.yaml`.
4. Keep telemetry disabled unless you intentionally configure it.

Render gives the web service an `onrender.com` URL. The service binds to `PORT`/`0.0.0.0`.

## Full live scanning

For live scans, run the iqAudi/Strix engine on a Docker-capable worker and expose a
small authenticated job API. The worker can write its `strix_runs` directory to shared
storage or send completed run artifacts to the web service.
