# app/domains/berries/routes.py

from fastapi import APIRouter
from app.domains.berries.service import Berries

router = APIRouter()

@router.get("/allBerryStats")
def get_berries_stats_route():
    berries_service = Berries()
    return berries_service.get_berries_stats()