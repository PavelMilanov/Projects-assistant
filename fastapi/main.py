from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend import services, auth, database, scheduller, logging
from environs import Env


env = Env()
env.read_env()

app = FastAPI(
    title='Project Assistant',
    version='0.2.0',
    description='Rest API для Trello API и Google Drive API')
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

@app.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends()) -> str:
    """Генерирует персональный токен."""
    login, password = form.username, form.password
    if login != env('LOGIN') or password != env('PASSWORD'):
        logging.logger.error(
            f'Неудачная попытка авторизации: {login} {password}')
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
            logging.logger.info(f'{login} успешно авторизован')
            return access_token
    
@app.get('/generate')
def generate(token: str = Depends(auth_scheme)) -> dict:
    """Генериует google document на основании Trello API и Google Drive API."""
    try:
        services.generate_doc()
        return JSONResponse(
            content='Документ успешно сгенерирован')
    except Exception as e:
        logging.logger.error(f'{e}')
        return JSONResponse(
            content=f'{e}')

@app.get('/clear')  # тестовый режим
def clear(token: str = Depends(auth_scheme)) -> dict:
    """Стирает все данные google document на основании Trello API и Google Drive API."""
    try:
        services.clear_doc()
        return JSONResponse(
            content='Документ успешно отформатирован')
    except Exception as e:
        logging.logger.error(f'{e}')
        return JSONResponse(
            content=f'{e}')

@app.get('/download')
def download(token: str = Depends(auth_scheme)) -> dict:
    """Скачивает google document на сервер на основании Google Drive API."""
    try:
        services.download_doc()
        return JSONResponse(
            content='Документ успешно загружен')
    except Exception as e:
        logging.logger.error(f'{e}')
        return JSONResponse(
            content=f'{e}')

@app.post('/archive')
def archive(token: str = Depends(auth_scheme)) -> dict:
    """Архивирует все карточки в колонке Trello на основании Trello API."""
    try:
        services.archive_cards()
        return JSONResponse(
            content='Карточки заархивированы')
    except Exception as e:
        logging.logger.error(f'{e}')
        return JSONResponse(
            content=f'{e}')
