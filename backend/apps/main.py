from fastapi import FastAPI
from apps.routes import students
from apps.db.session import init_db
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.include_router(students.router, tags=["students"])



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup():
        await init_db()