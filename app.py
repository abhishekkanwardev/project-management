from flask import Flask
from models import db
from api import api, ProjectDetailView, ProjectCreateView

app = Flask(__name__)
# Database configuration settings
app.config.from_pyfile('config.py')

db.init_app(app)

with app.app_context():
    db.create_all()

# API endpoints
api.add_resource(ProjectDetailView, '/api/projects/<int:project_id>', endpoint='project')
api.add_resource(ProjectCreateView, '/api/projects', endpoint='projects')

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

