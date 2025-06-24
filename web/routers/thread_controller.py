from http import HTTPStatus
from fastapi import APIRouter
from application.services.thread_service import ThreadService
router = APIRouter()

@router.get("/ping")
def root():
    return "threads it's Working"

@router.get("/threads",status_code=HTTPStatus.OK)
def get_all_threads(page_number:int=1,quantity:int=20):
    service = ThreadService()
    content = service.get_all_threads(page_number,quantity)
    return content

@router.post("/threads",status_code=HTTPStatus.CREATED)
def create_thread(data:dict) -> dict:
    service = ThreadService()
    service.create_thread(data)
    return {"message": "Thread created successfully"}
        

@router.get("/threads/{id}")
def get_thread_by_id(id:int):
    service = ThreadService()
    thread = service.get_thread_by_id(id)
    return thread



