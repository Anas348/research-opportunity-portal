from flask import Flask
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Research Opportunity Portal API is running"}

@app.route('/test-db')
def test_db():
    conn = get_connection()
    conn.close()
    return {"message": "Database connection successful"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)