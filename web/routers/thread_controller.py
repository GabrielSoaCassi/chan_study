from http import HTTPStatus
from fastapi import APIRouter
from application.services.thread_service import ThreadService
from packages.models.thread import Thread
router = APIRouter()

@router.get("/ping")
def root():
    return "threads it's Working"

@router.get("/threads",status_code=HTTPStatus.OK)
def get_all_threads(page_number:int=1,quantity:int=20):
    content = ThreadService.get_all_threads(page_number,quantity)
    return content

@router.post("/threads",status_code=HTTPStatus.CREATED)
def create_thread(data:Thread) -> dict:
    ThreadService.create_thread(data)
    return {"message": "Thread created successfully"}
        

@router.get("/threads/{id}")
def get_thread_by_id(id:int):
    thread = ThreadService.get_thread_by_id(id)
    return thread
