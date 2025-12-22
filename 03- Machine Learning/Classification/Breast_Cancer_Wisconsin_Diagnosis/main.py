from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

from src.utils.inference import predict_new
from src.utils.config import APP_NAME, API_SECRET_KEY, VERSION, preprocessor, log_clf_model
from src.utils.PatiantData import PatiantData


app = FastAPI(title=APP_NAME, version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', tags=['General'])
async def home():
    return {
         "message": f"Welcome to {APP_NAME} API v{VERSION}"
    }


api_key_header = APIKeyHeader(name='X-API-Key')

async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key



@app.post('/prdict/Logistic_clf', tags=['models'])
async def predict_log_clf (data: PatiantData, api_key: str=Depends(verify_api_key)) -> dict:
    try:
        result = predict_new(data=data, preprocessor=preprocessor, model=log_clf_model)
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


