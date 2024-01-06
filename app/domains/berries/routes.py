# app/domains/berries/routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.domains.berries.service import Berries

router = APIRouter()

@router.get("/allBerryStats")
def get_berries_stats_route():
    berries_service = Berries()
    try:
        berry_info, headers = berries_service.get_berries_stats()
        # Create a JSONResponse with the result and headers
        response = JSONResponse(content=berry_info, headers=headers)

        return response
    except HTTPException as e:
        # Catch and re-raise HTTP exceptions
        raise e
