from fastapi import FastAPI
from controller.index_controller import router
app = FastAPI()
app.include_router(router)