from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import motor.motor_asyncio

app=FastAPI()

MONGO_USER= os.getenv("MONGO_USER","admin")
MONGO_PASSWORD= os.getenv("MONGO_PASSWORD","password")
MONGO_HOST= os.getenv("MONGO_HOST","localhost")
MONGO_PORT= os.getenv("MONGO_PORT","27017")
MONGO_DBNAME= os.getenv("MONGO_DBNAME","userdb")

MONGO_URI= f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"

client= motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db=client[MONGO_DBNAME]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class User(BaseModel):
    username: str
    email: str

users = [
{"username":"alice", "email":"alice@example.com"},
{"username":"bob", "email":"bob@example.com"}
]

@app.get("/")
def root():
    return {"message":"User service is running"}

@app.get("/users")
async def get_users():
    users=[]
    cursor=db.users.find()
    async for document in cursor:
        users.append(document)
    return {"users":users}

@app.post("/users")
async def create_user(user: User):
    user_dict=user.dict()
    result=await db.users.insert_one(user_dict)
    return {"message":"user created","id": str(result.inserted_id)}

