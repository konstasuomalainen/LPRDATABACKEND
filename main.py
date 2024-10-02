from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import sqlite3
import logging

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application! Sort Data by Year via changing the URL as an example: /data/2020"}

def get_data_for_year(year: int, limit: int = None, skip: int = 0):
    conn = sqlite3.connect('data.db')
    try:
        # Base query to get data for the specified year
        query = "SELECT * FROM data WHERE Year = ? ORDER BY \"Index\" ASC"

        df = pd.read_sql_query(query, conn, params=(year,))

        # Apply pagination
        if limit is not None:
            df = df.iloc[skip:skip + limit]

        if df.empty:
            raise HTTPException(status_code=404, detail=f"No data found for the year {year}")

        return df.to_dict(orient="records")
    finally:
        conn.close()

@app.get("/data/{year}")
def get_data_by_year(year: int, limit: int = Query(None), skip: int = Query(0)):
    if year < 2020 or year > 2023:
        raise HTTPException(status_code=400, detail="Year not supported")
    return get_data_for_year(year, limit, skip)
