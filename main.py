from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import authentication, blog
from database.database import Base, engine
from routers import user

app = FastAPI(
    title="FastAPI",
    description="blogs and users management",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.exception_handler(Exception) # async is used since it aligns with FastAPI design but sync will also work.
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )   

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
