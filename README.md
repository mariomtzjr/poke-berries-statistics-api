# poke-berries-statistics-api
Poke-berries statistics API  

This FastAPI project fetches information about berries from the PokeAPI and provides a human-readable response. The data is obtained by consuming the PokeAPI, and the project is configured using environment variables. Additionally, the project includes test cases using pytest.

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- FastAPI
- Requests
- python-dotenv
- pytest

Setup
1. Clone the Repository:  
   ```
    git clone https://github.com/mariomtzjr/poke-berries-statistics-api.git
    cd poke-berries-statistics-api
   ```
2. Install Dependencies:
   ```pip install -r requirements.txt```
3. Run the FastAPI App:
   ```uvicorn app.main:app --reload```

## Usage
Access the API endpoint by making a GET request to http://localhost:8000/berries/allBerryStats

## Running Tests
Execute the following command:  
```pytest tests/poke_tests.py```