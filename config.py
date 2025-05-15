import os
from dotenv import load_dotenv
from pathlib import Path

# Load env variables from .env
load_dotenv()

# Project root
BASE_DIR = Path(__file__).resolve().parent


# File paths (from .env)
RAW_AIRLINE_DELAY_CAUSE = os.getenv("RAW_AIRLINE_DELAY_CAUSE", BASE_DIR / "data/Airline_Delay_Cause.csv")
RAW_AIRLINE_REVIEW = os.getenv("RAW_AIRLINE_REVIEW", BASE_DIR / "data/Airline_review.csv")
RAW_AIRLINES = os.getenv("RAW_AIRLINES", BASE_DIR / "data/airlines.csv")
RAW_AIRPORTS = os.getenv("RAW_AIRPORTS", BASE_DIR / "data/airlines.csv")
RAW_DATA_FYYTg = os.getenv("RAW_DATA_FYYTg", BASE_DIR / "data/data-FYYTg.csv")
RAW_FLIGHTS = os.getenv("RAW_FLIGHTS", BASE_DIR / "data/flights.cvs")
RAW_PLANES = os.getenv("RAW_PLANES", BASE_DIR / "data/df_planes_cleaned.csv")
CLEANED_PLANES = os.getenv("CLEANED_PLANES", BASE_DIR / "data/Airline_review.csv")
CLEANED_AIRCRAFT_DATA = os.getenv("CLEANED_AIRCRAFT_DATA", BASE_DIR / "data/Cleaned_Aircraft_Data.csv")
CLEANED_AIRPORTS = os.getenv("CLEANED_AIRPORTS", BASE_DIR / "data/cleaned_airports.csv")
MASTER_AIRPORTS = os.getenv("MASTER_AIRPORTS", BASE_DIR / "data/T_MASTER_CORD.csv")





