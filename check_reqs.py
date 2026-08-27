import sys
import io
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

token = 'eyJraWQiOiI3ZWE2MjJmNC03YTBhLTQyNDEtYjBjZS0yOWQwNzcwZDEwMGUiLCJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIyZDc0NDQ3ZC1jNmU1LTQ2NDgtOGYzMC04ZjI0ODU3MjkwZmUiLCJpc3MiOiJodHRwczovL2F1dGgtZGV2cG9zdC5jb20iLCJzdWIiOiIxMDU1MjY5NiIsImF1ZCI6Imh0dHBzOi8vZGV2cG9zdC5jb20vbWNwIiwiaWF0IjoxNzg3NzMzMTgxLCJleHAiOjE3OTAzMjUxODMsInNjb3BlIjoibWNwOnJlYWQgbWNwOndyaXRlIG1jcDp0b29scyIsImNsaWVudF9pZCI6InBlcnNvbmFsX2FjY2Vzc190b2tlbnMifQ.aPyHTfhsAA_QushFsmyNxQ6JZE_ZaEeXnn_AEhBZOoogkuwgr1pqAhCSIXxVjflKg6nDEtIR-OgsWMz-ABM3M0zmmY2DZtNQW0vCWHr5VRxwghkkkXjGsmvHvXdd5U0Rvp3zGGla87HErnbUcptkkgnlfDNxBoQ_G89u2FaNiJqFCWDW6J366RrZGPmXo2tTbWP8L_CacSPxtC0EjXIFoEdzWFKA8HrTAuQ0eEfDUsX5AGWOJTuIimJikFcL7mJAWOBOhR8ZQ_n6QQNhCDu_9MdNVJR8Kk9wh4C-OJy6zXQ9MxjeEcz8uf42ZnB-qi_lHjG1ANVrxfhuXdXEVulPtw'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

payload = {
    'jsonrpc': '2.0',
    'id': 1,
    'method': 'tools/call',
    'params': {
        'name': 'get_submission_requirements',
        'arguments': {
            'hackathon_subdomain': 'allthingsagentichackathon'
        }
    }
}

res = requests.post('https://devpost.com/mcp', headers=headers, json=payload)
data = res.json().get('result', {}).get('structuredContent', {})
print("Deliverables:", json.dumps(data.get('deliverable_rules'), indent=2))
print("\nCustom Questions:")
for q in data.get('custom_questions', []):
    print(f"- ID: {q.get('id')} | Required: {q.get('required')} | Type: {q.get('type')} | Label: {q.get('label')}")
    if q.get('options'):
        print(f"  Options: {q.get('options')}")
