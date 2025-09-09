from fastapi import FastAPI
import database
from database import engine
import router

# Create DB tables
database.Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI(title="FastAPI with PostgreSQL")

# Include router
app.include_router(router.Router)

@app.get("/")
async def greeting():
    return {"message": "Welcome all"}
