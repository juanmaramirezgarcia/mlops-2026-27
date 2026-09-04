"""
test_api.py  -  the CI 'tests' stage: check the API behaves before anything is built or deployed.
Run:  pytest -q      (needs churn_model.pkl, so the pipeline runs train.py first)
"""
from fastapi.testclient import TestClient
import app as m

client = TestClient(m.app)


def test_health():
    assert client.get("/health").json()["status"] == "ok"


def test_high_risk_customer_is_flagged():
    r = client.post("/predict", json={"tenure_months": 6, "monthly_charges": 85, "support_tickets": 4,
                                      "promo_weeks_last_quarter": 1, "is_monthly": 1, "region_north": 1}).json()
    assert 0.0 <= r["churn_probability"] <= 1.0
    assert r["churn"] is True          # this profile must score above the 0.5 threshold


def test_loyal_customer_is_not_flagged():
    r = client.post("/predict", json={"tenure_months": 60, "monthly_charges": 45, "support_tickets": 0,
                                      "promo_weeks_last_quarter": 0, "is_monthly": 0, "region_north": 0}).json()
    assert r["churn"] is False


def test_missing_field_is_rejected():
    assert client.post("/predict", json={"tenure_months": 6}).status_code == 422
