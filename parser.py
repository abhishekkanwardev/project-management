from flask_restful import reqparse


project_create_parser = reqparse.RequestParser()
project_create_parser.add_argument('title', type=str, required=True, help='Title is required')
project_create_parser.add_argument('description', type=str)
project_create_parser.add_argument('complete', type=bool, default=False)
