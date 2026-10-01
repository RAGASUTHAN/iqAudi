"""iqAudi Render viewer entrypoint.

The Strix engine itself remains a local/worker process because it needs Docker
sandbox execution. This service exposes the rebranded viewer for completed runs.
Set IQAUDI_RUN_DIR to a directory containing a Strix run when using a worker
that shares storage; otherwise the service boots with a safe demo run.
"""
from pathlib import Path
import os
from strix.interface.viewer.server import serve, authorized_url

BASE = Path(os.getenv("IQAUDI_RUN_DIR", "/data/strix_runs"))
BASE.mkdir(parents=True, exist_ok=True)
run = BASE / "demo"
run.mkdir(parents=True, exist_ok=True)
record = run / "run.json"
if not record.exists():
    record.write_text('{"run_name":"iqAudi demo","target":"No scan loaded","finished":true,"status":"finished","start_time":null,"end_time":null}')

port = int(os.getenv("PORT", "10000"))
httpd, url, token = serve(run, host="0.0.0.0", port=port, open_browser=False)
print(authorized_url(url, token), flush=True)
httpd.serve_forever()
