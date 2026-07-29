from fastapi import FastAPI
app=FastAPI(title='VMAI Labs API')
@app.get('/')
def root(): return {'status':'ok'}
