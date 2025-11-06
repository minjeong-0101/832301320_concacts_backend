from flask import Flask
from flask_cors import CORS
import models
from routes import contact_bp

# Create Flask app
app = Flask(__name__)

# Enable CORS to allow cross-origin requests
CORS(app)

# Register blueprints
app.register_blueprint(contact_bp)

# Initialize database
models.init_db()

if __name__ == '__main__':
    app.run(debug=True)