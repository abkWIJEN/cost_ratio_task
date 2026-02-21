# cost_ratio_task
Overview
  This service calculates Market Value (FMV) and Auction Value (FLV) for a piece of equipment based on:
      Classification ID
      Model Year

  The calculation is based on:
      Market Value  = Cost × Market Ratio
      Auction Value = Cost × Auction Ratio

  For Given Classification ID.
      Ratios vary by Model Year and Value Type (Market or Auction).
      If a Model Year does not exist in the depreciation schedule, default ratios are used.
      The service only supports Model Years between 2006 and 2020 (inclusive)
  Example
    Request GET /valuation/87390/2016
    Response {
      "classificationId": "87390",
      "modelYear": 2016,
      "marketValue": 30008,
      "auctionValue": 20426
}


Architecture
app/
├── main.py        # API Layer (FastAPI)
├── service.py     # Business Logic
└──  data.py        # Static JSON Data

tests/
└── test_service.py


Design Principles

Separation of API and business logic
Fully unit-testable service layer
Custom domain exceptions
Deterministic, pure calculation logic
Easily extendable to DB or external API source

Business Rules
1. Valid Model Year Range
2006 ≤ Model Year ≤ 2020

   If   outside range:
        Returns HTTP 400
        Friendly error message

2. Ratio Selection Logic
If year exists in schedule → use year-specific ratios
If year does not exist → use default ratios

3. Rounding
Values are rounded using standard rounding: round(cost × ratio)


Installation
1. Clone Repository
    git clone <repository-url>
    cd equipment_service

2. Create Virtual Environment
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows

3. Install Dependencies
       pip install -r requirements.txt
       If building manually: pip install fastapi uvicorn pytest
          

Running the Service: uvicorn app.main:app --reload
Service will run at: http://127.0.0.1:8000
Interactive Swagger UI available at: http://127.0.0.1:8000/docs
Running Tests: pytest
Expected output: 5 passed in 0.xx seconds


Test Coverage
The unit tests cover:
  Correct Market & Auction calculation
  Default ratio fallback
  Invalid Model Year (below range)
  Invalid Model Year (above range)
  Invalid Classification ID
The service layer is fully isolated and testable without running the API.

Error Handling
Invalid Model Year
Response

{
  "detail": "Model Year must be between 2006 and 2020."
}
HTTP Status: 400

Invalid Classification ID
{
  "detail": "Classification ID not found."
}
HTTP Status: 404


Assumptions
  Book Cost does not change by Model Year.
  If a year is not explicitly listed, default ratios apply.
  Data is static (in-memory JSON) for this implementation.
  Service is stateless.

Possible Enhancements
  Replace static JSON with database or external API
  Add caching layer
  Add logging & monitoring
  Add Docker support
  Add CI/CD pipeline
  Add integration/API tests
  Add OpenAPI schema validation

Tech Stack
  Python 3.x
  FastAPI
  Pytest


Author Notes
  This implementation prioritizes:
      Clean architecture
      Maintainability
      Testability
      Clear separation of responsibilities

  The business logic is independent of the API layer, making it easy to extend to:
      CLI application
      Serverless function
      Batch processing job
      Different web framework



