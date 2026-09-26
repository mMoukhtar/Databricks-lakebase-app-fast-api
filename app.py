import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Databricks App and Lakebase", debug=True)


@app.get("/")
def healthy():
    return {
        "status": "Healthy",
        "message": "Hello from Databricks APP!",
    }


if __name__ == "__main__":
    host = os.getenv("UVICORN_HOST", "0.0.0.0")
    port = int(os.getenv("UVICORN_PORT", 8000))
    uvicorn.run(app=app, host=host, port=port)
    print(f"FastAPI app running on http://{host}:{port}")
