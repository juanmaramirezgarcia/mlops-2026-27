"""
test_request.py  -  calls the running API the way an application would (last year this was requests.py).
Start the service first (run_local.command, or: uvicorn app:app --port 8080), then:  python test_request.py
"""
import json
import urllib.request

URL = "http://127.0.0.1:8080/predict"
customer = {"tenure_months": 6, "monthly_charges": 85, "support_tickets": 4,
            "promo_weeks_last_quarter": 1, "is_monthly": 1, "region_north": 1}

req = urllib.request.Request(URL, data=json.dumps(customer).encode(),
                             headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req) as r:
    result = json.load(r)

print("Sent:    ", customer)
print("Received:", result)
print(f"\n-> churn probability {result['churn_probability']:.0%}; "
      f"the model {'would' if result['churn'] else 'would not'} put this customer on the retention call list.")
