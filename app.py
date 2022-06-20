from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")


@app.get("/apps-api/")
async def mainpage():
    return """mainpage"""
@app.get("/")
async def mainpage():
    return """mainpage"""
