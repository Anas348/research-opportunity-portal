from flask import Flask, jsonify
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

@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM opportunities")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)