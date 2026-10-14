# Quick start

## Frontend
cd frontend && npm install && npm run dev   # http://localhost:5173

## Backend
cd backend
py -m venv venv
source venv/Scripts/activate    # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload       # http://localhost:8000/docs

## Keys
Copy .env.example to .env in BOTH frontend/ and backend/, then fill in the values from the team chat.