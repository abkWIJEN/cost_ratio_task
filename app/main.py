from fastapi import FastAPI, HTTPException
from app.service import (
    EquipmentValuationService,
    EquipmentNotFound,
    InvalidModelYear,
)

app = FastAPI()


@app.get("/valuation/{classification_id}/{model_year}")
def get_valuation(classification_id: str, model_year: int):
    try:
        return EquipmentValuationService.get_values(classification_id, model_year)
    except InvalidModelYear as e:
        raise HTTPException(status_code=400, detail=str(e))
    except EquipmentNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))