from http import HTTPStatus
from fastapi import APIRouter
from application.services.post_service import PostService
from packages.models.post import Post

router = APIRouter()


@router.get("/pong")
def root():
    return "Post it's Working"


@router.post("/posts", status_code=HTTPStatus.CREATED)
def create_post(post: dict) -> dict:
    result = PostService.create_post(post)
    return {"message": "Post created successfully", "post": result}


@router.get("/posts")
def get_posts(thread_id: int, page_number: int = 1, quantity: int = 20):
    result = PostService.get_posts(thread_id, page_number, quantity)
    return result
