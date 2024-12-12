# Task Management System API

This is  a simple Task Management System built with FastAPI.

## Setup and Installation

1. Clone the github repository: https://github.com/Kushagradheer/fast_api.git


2. Create a virtual environment and activate it:  
    =>python -m venv venv
    =>source venv/bin/activate # On Windows, use venv\Scripts\activate.bat

3. Install Dependencies :
    => pip install -r requirements.txt
    => pip install fastapi[all]

4. Install & Setup DB Dependencies :pip install SQLAlchemy fastapi-utils : pip install sqlalchemy


5. Run the application:
   => uvicorn app.main:app --reload

6. Access the API documentation at:
   => Swagger UI: `http://127.0.0.1:8000/docs`






## Testing
1. Install Pytest: pip install pytest
   
2. Run tests: python -m pytest
