import os

from fastapi import FastAPI
import uvicorn

from app.domains.berries.routes import router as berries_router

app = FastAPI()


# Include routes from the berries domain
app.include_router(berries_router, prefix="/berries", tags=["berries"])

if __name__ == "__main__":
    # Get host and port from environment variables, or use default values
    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", 8000))

    # Run the app using uvicorn
    uvicorn.run(app, host=host, port=port, reload=True)