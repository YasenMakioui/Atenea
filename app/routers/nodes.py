from fastapi import APIRouter

router = APIRouter()


@router.get("/nodes/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/nodes/{node_id}", tags=["nodes"])
async def read_user(username: str):
    return {"username": username}
