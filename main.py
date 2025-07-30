
from fastapi import FastAPI
from routers import authentication, blog
from database.database import Base, engine
from routers import user

app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
