from flask import Flask, request, jsonify
from flask_cors import CORS
import database.db as db


app = Flask(__name__)
CORS(app)









if __name__ == '__main__':
  db.init_db()
  app.run(debug=False, host='0.0.0.0', port=5000)