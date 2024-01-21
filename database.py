from sqlalchemy import create_engine, text
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

db_connection_string = config['db_connection_string']

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