"""File responsible for to run the application."""
import uvicorn

from app.main import get_application
from app.utils.config import settings


app = get_application()


def run():
    """This function acts as a utility to run the app in development mode."""
    uvicorn.run("run:app", host="0.0.0.0", reload=True, port=5000,
                debug=settings.DEBUG, workers=3,
                timeout_keep_alive=300)


if __name__ == "__main__":
    # Running the application
    run()
