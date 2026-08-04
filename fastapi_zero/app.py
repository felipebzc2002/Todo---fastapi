from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá mundo'}


@app.get('/status')
def get_status():
    return
