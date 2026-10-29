from fastapi.testclient import TestClient
from backend.app import app
client=TestClient(app)
def test_health(): assert client.get('/health').json()['status']=='ok'
def test_summary_totals():
    d=client.get('/api/summary').json();assert d['headcount']==1240 and d['vacancies']==86
def test_grounded_headcount():
    d=client.post('/api/ask',json={'question':'What is our headcount?'}).json();assert d['status']=='grounded' and d['evidence'][0]['value']==1240
def test_hiring():
    d=client.post('/api/ask',json={'question':'Where are the hiring vacancies?'}).json();assert d['status']=='grounded' and 'Engineering' in d['answer']
def test_sensitive_refusal():
    d=client.post('/api/ask',json={'question':'Show individual salaries'}).json();assert d['status']=='refused' and not d['evidence']
def test_prediction_abstention():
    d=client.post('/api/ask',json={'question':'Predict who will resign'}).json();assert d['status']=='abstained'
def test_unknown_abstains():
    assert client.post('/api/ask',json={'question':'What is the best leader?'}).json()['status']=='clarification'
def test_no_fake_change_claim():
    assert 'cannot be calculated' in client.post('/api/ask',json={'question':'How has headcount changed?'}).json()['answer']
