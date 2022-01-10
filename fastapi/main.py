from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend import services, auth, database, scheduller, logging
from environs import Env


env = Env()
env.read_env()

app = FastAPI(title='Project Assistant', version='0.1.3')
auth_scheme = OAuth2PasswordBearer(tokenUrl='/login')

scheduller.scheduler_init()  # start jobs

origins = ['http://localhost:8080']  # Vue

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/login')  # тестовый режим
def login(form: OAuth2PasswordRequestForm = Depends()) -> str:
    """Генерирует персональный токен."""
    login, password = form.username, form.password
    if login != env('LOGIN') or password != env('PASSWORD'):
        return JSONResponse(
            content='Неверные данные')
    else:
        authorize = database.Database.find({
            'login': login,
            'password': password
        })
        if authorize:
            return authorize['access_token']
        else:
            access_token = auth.Auth().create_token(login, password)
            database.Database.insert({
                'login': login,
                'password': password,
                'access_token': access_token})
            return access_token
    
@app.get('/generate')  # тестовый режим
def generate(token: str = Depends(auth_scheme)) -> dict:
    """Генериует google document на основании Trello API и Google Drive API."""
    services.generate_doc()
    return {'message': 'generate doc'}

@app.get('/clear')  # тестовый режим
def clear(token: str = Depends(auth_scheme)) -> dict:
    """Стирает все данные google document на основании Trello API и Google Drive API."""
    services.clear_doc()
    return {'message': 'clear doc'}

@app.get('/download')  # тестовый режим
def download(token: str = Depends(auth_scheme)) -> dict:
    """Скачивает google document на сервер на основании Google Drive API."""
    services.download_doc()
    return {'message': 'download doc'}

@app.post('/archive')  # тестовый режим
def archive(token: str = Depends(auth_scheme)) -> dict:
    """Архивирует все карточки в колонке Trello на основании Trello API."""
    services.archive_cards()
    return {'message': 'archive card'}
