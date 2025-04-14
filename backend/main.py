from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from schemas import *
from google import genai  # Using Gemini API 

app = FastAPI()

## Adding middleware to prevent CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

# Load dummy data
with open("../dummyData.json", "r") as f:
    DUMMY_DATA = json.load(f)

@app.get("/api/data")
def get_data():
    """
    Returns dummy data (e.g., list of users).
    """
    return {"users":DUMMY_DATA['salesReps']}


@app.get("/api/users")
async def get_list_all_users() -> list[User]:
    """
    Returns list users data (e.g., users).
    """
    return [
        User(**u) for u in DUMMY_DATA['salesReps']
    ]
    

@app.get("/api/user/{id}")
async def get_user_by_id(id: int) -> User:
    """
    Returns user data (e.g., user by id).
    """
    user = next((User(**u) for u in DUMMY_DATA['salesReps'] if u["id"] == id ), None)
    
    if(user == None):
        raise HTTPException(status_code=404, detail="User not found")
    return user



@app.post("/api/ai")
async def ai_endpoint(request: Request):
    """
    Accepts a user question and returns a placeholder AI response.
    (Optionally integrate a real AI model or external service here.)
    """
    body = await request.json()
    user_question = body.get("question", "")
    
    # Placeholder logic: echo the question or generate a simple response
    if(user_question == ""):
        return {"answer":"Please ask the AI somthing!"}
    
    client = genai.Client(api_key="API_KEY_FROM_GOOGLE_GEMINI_AI")      # REDACTED for me [ Please provide a new one ]

    # Replace with real AI logic as desired (e.g., call to an LLM).
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{user_question}"
    )

    
    return {
        "question": f"{user_question}",
        "answer": f"{response.text}"
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)