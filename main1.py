from fastapi import FastAPI
from controller.index_controller import router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)