from flask import request
from flask_restful import Resource, Api
from models import db, Projects
from parser import project_create_parser

api = Api()

class ProjectCreateView(Resource):
    def get(self):
        # API to get list of projects
        projects = Projects.query.all()
        project_list = [{'id': project.id, 'title': project.title, 'description': project.description,
                        'complete': project.complete, 'created_at': project.created_at.strftime('%Y-%m-%d %H:%M:%S')} for project in projects]
        response = {
                    "data" : project_list,
                    "message":"Project List fetched successfully",
                    "status":200
                }
        return response

    def post(self):
        # API to create new project
        args = project_create_parser.parse_args()
        title = args['title']
        description = args['description']
        complete = args['complete']

        # Check for title
        if not title:
            return {'error': 'Title is required'}, 400

        # Create a new project
        new_project = Projects(title=title, description=description, complete=complete)
        db.session.add(new_project)
        db.session.commit()
        response = {
            "message":"Project Created successfully",
            "status":201
        }
        return response


class ProjectDetailView(Resource):
    def get(self, project_id):
        # API to get project detail
        project = Projects.query.get(project_id)
        if not project:
            return {'error': 'Project not found'}, 404
        data = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'complete': project.complete,
            'created_at': project.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
        }
        response = {
            "data":data,
            "message":"Project detail",
            "status":200
        }
        return response
    
    def put(self, project_id):
        # API to update the project
        project = Projects.query.get(project_id)
        if not project:
            return {'error': 'Project not found'}, 404

        args = project_create_parser.parse_args()
        project.title = args['title']
        project.description = args['description']
        project.complete = args['complete']
        db.session.commit()
        response = {
            "data":args,
            "message":"Project updated successfully",
            "status":200
        }
        return response

    def delete(self, project_id):
        # API to delete a project
        project = Projects.query.get(project_id)
        if not project:
            return {'error': 'Project not found'}, 404

        db.session.delete(project)
        db.session.commit()
        response = {
            "data":[],
            "message":"Project deleted successfully",
            "status":200
        }
        return response
