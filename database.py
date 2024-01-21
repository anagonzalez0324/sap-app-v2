from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

# Load environment variables from .env file
load_dotenv()

db_connection_string = os.environ.get('DB_CONNECTION_STRING')

engine = create_engine(
    db_connection_string,
    connect_args = {
        "ssl": {
            "ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [dict(zip(result.keys(), row)) for row in result]
    return jobs