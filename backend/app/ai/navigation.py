from pydantic import BaseModel
from typing import List

# Navigation AI module (MVP)
# Future upgrades:
# - Mapbox / Google Maps routing
# - indoor navigation (BLE / Wi-Fi positioning)
# - ARCore/ARKit assistive guidance
# - obstacle-aware path planning

class NavigationRequest(BaseModel):
    start_lat: float
    start_lng: float
    end_lat: float
    end_lng: float
    mode: str = "walking"


class NavigationStep(BaseModel):
    instruction: str
    distance_m: float


class NavigationResponse(BaseModel):
    route_summary: str
    steps: List[NavigationStep]
    danger_zones: List[str]
    estimated_time_min: int


async def plan_route(data: NavigationRequest) -> NavigationResponse:
    """
    MVP navigation planner (stub).
    Later will integrate:
    - OpenStreetMap / Mapbox Directions API
    - safety scoring model
    - obstacle detection fusion from Vision AI
    """

    steps = [
        NavigationStep(instruction="Go straight for 200m", distance_m=200),
        NavigationStep(instruction="Turn right", distance_m=50),
        NavigationStep(instruction="Continue to destination", distance_m=300),
    ]

    return NavigationResponse(
        route_summary="Safe walking route generated",
        steps=steps,
        danger_zones=["construction area"],
        estimated_time_min=8,
    )