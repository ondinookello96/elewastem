import requests, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

token = 'eyJraWQiOiI3ZWE2MjJmNC03YTBhLTQyNDEtYjBjZS0yOWQwNzcwZDEwMGUiLCJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIyZDc0NDQ3ZC1jNmU1LTQ2NDgtOGYzMC04ZjI0ODU3MjkwZmUiLCJpc3MiOiJodHRwczovL2F1dGgtZGV2cG9zdC5jb20iLCJzdWIiOiIxMDU1MjY5NiIsImF1ZCI6Imh0dHBzOi8vZGV2cG9zdC5jb20vbWNwIiwiaWF0IjoxNzg3NzMzMTgxLCJleHAiOjE3OTAzMjUxODMsInNjb3BlIjoibWNwOnJlYWQgbWNwOndyaXRlIG1jcDp0b29scyIsImNsaWVudF9pZCI6InBlcnNvbmFsX2FjY2Vzc190b2tlbnMifQ.aPyHTfhsAA_QushFsmyNxQ6JZE_ZaEeXnn_AEhBZOoogkuwgr1pqAhCSIXxVjflKg6nDEtIR-OgsWMz-ABM3M0zmmY2DZtNQW0vCWHr5VRxwghkkkXjGsmvHvXdd5U0Rvp3zGGla87HErnbUcptkkgnlfDNxBoQ_G89u2FaNiJqFCWDW6J366RrZGPmXo2tTbWP8L_CacSPxtC0EjXIFoEdzWFKA8HrTAuQ0eEfDUsX5AGWOJTuIimJikFcL7mJAWOBOhR8ZQ_n6QQNhCDu_9MdNVJR8Kk9wh4C-OJy6zXQ9MxjeEcz8uf42ZnB-qi_lHjG1ANVrxfhuXdXEVulPtw'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def call_tool(name, args):
    payload = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'tools/call',
        'params': {
            'name': name,
            'arguments': args
        }
    }
    r = requests.post('https://devpost.com/mcp', headers=headers, json=payload)
    res = r.json().get('result', {})
    text = res.get('content', [{}])[0].get('text', '')
    try:
        return json.loads(text)
    except:
        return text

overview = call_tool('get_hackathon_overview', {'hackathon_subdomain': 'allthingsagentichackathon'})
print("=== OVERVIEW ===")
print(json.dumps(overview, indent=2, ensure_ascii=False)[:1500])

criteria = call_tool('get_judging_criteria', {'hackathon_subdomain': 'allthingsagentichackathon'})
print("\n=== JUDGING CRITERIA ===")
print(json.dumps(criteria, indent=2, ensure_ascii=False)[:1500])

rules = call_tool('get_hackathon_rules', {'hackathon_subdomain': 'allthingsagentichackathon'})
print("\n=== RULES ===")
print(json.dumps(rules, indent=2, ensure_ascii=False)[:1500])
