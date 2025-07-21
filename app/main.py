import subprocess
import threading
import time
from dotenv import load_dotenv


from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

load_dotenv()


def run_backend():
    try:
        logger.info("Starting Backend Process")
        subprocess.run(
            ["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"]
        )
    except Exception as e:
        logger.error("Backend error", e)
        raise str(CustomException(f"The backend error due to {e}"))


def run_frontend():
    try:
        logger.info("Starting Frontend Process")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)
    except Exception as e:
        logger.error("Frontend error", e)
        raise (CustomException(f"The Frontend error due to {e}"))


if __name__ == "__main__":
    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)
        run_frontend()
    except Exception as e:
        logger.error("Error", e)
        raise (CustomException(f"The error due to {e}"))
