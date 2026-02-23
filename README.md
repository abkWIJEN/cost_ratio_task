# 📊 Cost Ratio Task

A lightweight valuation service that calculates:

- **Market Value (FMV)**
- **Auction Value (FLV)**

Based on:

- Classification ID
- Model Year

---

## 📌 Overview

The service calculates equipment values using predefined depreciation ratios.

### 📐 Formula

```python
Market Value  = Cost × Market Ratio
Auction Value = Cost × Auction Ratio
```

- Ratios vary by **Model Year** and **Value Type**
- If a Model Year does not exist in the schedule → **default ratios** are used
- Supported Model Years: **2006 – 2020 (inclusive)**

---

## 🚀 Example

### Request

```http
GET /valuation/87390/2016
```

### Response

```json
{
  "classificationId": "87390",
  "modelYear": 2016,
  "marketValue": 30008,
  "auctionValue": 20426
}
```

---

# 🏗 Architecture

```
app/
├── main.py        # API Layer (FastAPI)
├── service.py     # Business Logic
└── data.py        # Static JSON Data

tests/
└── test_service.py
```

---

# 🧠 Design Principles

- Separation of API and business logic  
- Fully unit-testable service layer  
- Custom domain exceptions  
- Deterministic calculation logic  
- Easily extendable to DB or external API  

---

# 📋 Business Rules

## 1️⃣ Valid Model Year Range

```
2006 ≤ Model Year ≤ 2020
```

If outside range:

- Returns HTTP 400
- Friendly error message

---

## 2️⃣ Ratio Selection Logic

- If year exists in schedule → use year-specific ratios  
- If year does not exist → use default ratios  

---

## 3️⃣ Rounding

```python
round(cost * ratio)
```

Standard rounding is applied.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd equipment_service
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Mac / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn pytest
```

---

# ▶️ Running the Service

```bash
uvicorn app.main:app --reload
```

Service URL:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Running Tests

```bash
pytest
```

Expected:

```
5 passed in 0.xx seconds
```

---

# ❗ Error Handling

## Invalid Model Year

```json
{
  "detail": "Model Year must be between 2006 and 2020."
}
```

HTTP Status: `400`

---

## Invalid Classification ID

```json
{
  "detail": "Classification ID not found."
}
```

HTTP Status: `404`

---

# 📝 Assumptions

- Book Cost does not change by Model Year  
- If year not listed → default ratios apply  
- Data stored in-memory (static JSON)  
- Service is stateless  

---

# 🚀 Possible Enhancements

- Replace static JSON with database or external API  
- Add caching layer  
- Add logging & monitoring  
- Add Docker support  
- Add CI/CD pipeline  
- Add integration/API tests  
- Add OpenAPI schema validation  

---

# 🛠 Tech Stack

- Python 3.x  
- FastAPI  
- Pytest  

---

# 👨‍💻 Author Notes

This implementation prioritizes:

- Clean architecture  
- Maintainability  
- Testability  
- Clear separation of responsibilities  

The business logic is independent of the API layer, making it easy to extend to:

- CLI application  
- Serverless function  
- Batch processing job  
- Different web framework  

---
