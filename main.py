from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web.routers import thread_controller,post_controller

app = FastAPI()

app.include_router(thread_controller.router)
app.include_router(post_controller.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)