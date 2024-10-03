# Lappeenranta Purchasing Receipts API (FastAPI Back End)

This is the back end of the **Lappeenranta Purchasing Receipts Viewer** project, built with **FastAPI** and powered by an **SQLite3** database. The back end reads purchasing receipt data from Excel files (downloaded from Avoin Data), stores it in an SQLite3 database, and exposes a REST API to serve this data to the front-end client.

## Features
- **FastAPI** for creating a RESTful API.
- Reads and parses purchasing receipt data from Excel files.
- Stores data in an **SQLite3** database for easy retrieval.
- Provides endpoints to fetch and sort purchasing receipt data.

## Tech Stack
- **Back End Framework**: FastAPI (Python)
- **Database**: SQLite3
- **Data Source**: Excel files (2020-2023 Lappeenranta purchasing receipts from Avoin Data)

## Installation

1. Clone the repository:

   ```bash
   https://github.com/your-username/LPRDATABACKEND.git
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```


4. Run the FastAPI development server:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000/data/2020`.


