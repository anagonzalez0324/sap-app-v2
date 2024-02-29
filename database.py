from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os
from flask import Flask, jsonify

# Load environment variables from .env file
load_dotenv()

DB_CONNECTION_STRING = os.environ.get('DB_CONNECTION_STRING')

engine = create_engine(
    DB_CONNECTION_STRING,
    connect_args = {
        "ssl": {
            "ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_orders_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from orders"))
        orders = [dict(zip(result.keys(), row)) for row in result]
    return orders

app = Flask(__name__)

def load_order_from_db(id):
    with engine.connect() as conn:
        stmt = text("SELECT * FROM orders WHERE id = :id").params(id=id)
        result = conn.execute(stmt)
        row = result.fetchone()
        if row is None:
            return None
        else:
            # Use keys() method of ResultProxy to get column names
            column_names = result.keys()

            # Convert RowProxy to a dictionary using column names
            order_dict = {column: getattr(row, column) for column in column_names}

            return order_dict

if __name__ == '__main__':
    app.run(debug=True)