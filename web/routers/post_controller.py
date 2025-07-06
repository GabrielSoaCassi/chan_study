from http import HTTPStatus
from fastapi import APIRouter
from application.services.post_service import AsyncPostService, PostService
from packages.models.post import Post

router = APIRouter()


@router.get("/pong")
async def root():
    return "Post it's Working"


@router.post("/posts", status_code=HTTPStatus.CREATED)
def create_post(post: dict) -> dict:
    service = PostService()
    result = service.create_post(post)
    return {"message": "Post created successfully", "post": result}


@router.get("/posts")
async def get_posts(thread_id: int, page_number: int = 1, quantity: int = 20):
    service = PostService()
    result = service.get_posts(thread_id, page_number, quantity)
    return result


@router.get("/async/posts")
async def get_posts_async(thread_id: int, page_number: int = 1, quantity: int = 20):
    service = AsyncPostService()
    result = await service.get_posts(thread_id, page_number, quantity)
    return result


@router.post("/async/posts", status_code=HTTPStatus.CREATED)
async def create_post_async(post: dict) -> dict:
    service = AsyncPostService()
    result = await service.create_post(post)
    return {"message": "Post created successfully", "post": result}
