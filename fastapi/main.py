from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from backend import services, auth, database
from environs import Env


env = Env()
env.read_env()
app = FastAPI(title='Project Assistant', version='0.1.1')
auth_scheme = OAuth2PasswordBearer(tokenUrl='/login')

@app.post('/login')  # тестовый режим
async def login(form: OAuth2PasswordRequestForm = Depends()):
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
async def generate(token: str = Depends(auth_scheme)):
    await services.generate_doc()
    return {'message': 'generate doc'}

@app.get('/clear')  # тестовый режим
async def clear(token: str = Depends(auth_scheme)):
    await services.clear_doc()
    return {'message': 'clear doc'}

@app.get('/download')  # тестовый режим
async def download(token: str = Depends(auth_scheme)):
    await services.download_doc()
    return {'message': 'download doc'}

@app.post('/archive')  # тестовый режим
async def archive(token: str = Depends(auth_scheme)):
    await services.archive_cards()
    return {'message': 'archive card'}
