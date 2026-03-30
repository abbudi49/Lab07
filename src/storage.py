import os
import json
from dataclasses import asdict
from src.models import Destination, TripCollection

# Base directory for the project (trip_notes/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "trips.json")

def load_trips() -> TripCollection:
    """Loads trips from data/trips.json into a TripCollection."""
    collection = TripCollection()
    if not os.path.exists(DATA_PATH):
        return collection
    
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for d in data:
                collection.add(Destination(**d))
    except (json.JSONDecodeError, FileNotFoundError):
        return collection
    
    return collection

def save_trips(collection: TripCollection) -> None:
    """Saves a TripCollection to data/trips.json."""
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    data = [asdict(d) for d in collection.get_all()]
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
