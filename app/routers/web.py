from fastapi.templating import Jinja2Templates
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
#import requests
import aiohttp


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="app/templates")

url = "http://localhost:8000"

@router.get("/")
def home (request:Request):
    msj = ""
    return templates.TemplateResponse(
    "home.html", {"request": request, "msj":msj}    
    )

@router.get("/register")
def registration(request: Request):
    msj = "" 
    return templates.TemplateResponse(
    "create_user.html",{"request": request,"msj":msj}
    )


@router.post("/register")
async def Registation(request: Request):
    print("entre")
    form = await request.form()
    usuario = {
        "username" : form.get('username'),
        "password" : form.get('password'),
        "nombre" : form.get('nombre'),
        "apellido" : form.get('apellido'),
        "correo" : form.get('correo'),
        "direccion" : form.get('direccion'),
        "telefono" : form.get('telefono'),
    } 
    print(usuario)
    url_post = f"{url}/user/"
    async with aiohttp.ClientSession() as session:
        response = await session.request(method="post",url=url_post,json=usuario)
        response_json = await response.json()
        print("final ->",response_json)
        if "respuesta" in response_json:
            msj = "usuario creado satisfactoriamente"
            type_alert = "primary"
        else :
            msj ="usuario no fue creado"
            type_alert = "danger"    
        return templates.TemplateResponse(
        "create_user.html",{"request": request,"msj":msj}
    )



@router.get("/Login_web")
def Login_web(request:Request):
    msj = ""
    return templates.TemplateResponse(
    "login.html", {"request": request, "msj":msj}    
    )


@router.post("/Login_web")
async def Login_web(request: Request):
    form = await request.form()

