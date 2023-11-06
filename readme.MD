## Project Files
```
config.py- This file contains database configuration information.
api.py - This file contains the api which perform CRUD opperation on Projects model.
parser.py - This file contains the validation
models.py - This file contains Project model description
app.py -  This is the main file which run the server. 
```
## Installation

Create Virtual Environment
```bash
python -m venv env
```

## Activate Virtual Environment

```python
source env/bin/activate
```

## Install Requirements
```python
pip install -r requirements.txt
```

## Run the Applicaton
```python 
python app.py
```

## API Entpoints
This project contain two entpoints listed below:-

http://127.0.0.1:5000/api/projects
http://127.0.0.1:5000/api/projects/<project_id>
