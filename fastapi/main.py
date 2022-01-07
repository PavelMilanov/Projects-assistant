from fastapi import FastAPI
import services


app = FastAPI(title='Project Assistant', version='0.1.0')

@app.get('/generate')  # тестовый режим
async def generate():
    await services.generate_doc()
    return {'message': 'generate doc'}

@app.get('/clear')  # тестовый режим
async def clear():
    await services.clear_doc()
    return {'message': 'clear doc'}

@app.get('/download')  # тестовый режим
async def download():
    await services.download_doc()
    return {'message': 'download doc'}

@app.post('/archive')  # тестовый режим
async def archive():
    await services.archive_cards()
    return {'message': 'archive card'}
