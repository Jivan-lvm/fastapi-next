from fastapi import Fastapi
import uvicorn
from app.users.router import router as router_users


app = Fastapi()

app.include_router(router_users)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
