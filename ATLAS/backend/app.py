"""ATLAS Impact Studio: synthetic, deterministic workforce answer API."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
import sqlite3, re, time

DB = Path(__file__).with_name('atlas.db')
app = FastAPI(title='ATLAS Impact Studio API', version='2.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['null','http://localhost:5500','http://127.0.0.1:5500','http://localhost:8000'], allow_methods=['GET','POST'], allow_headers=['Content-Type'])

class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    role: str = 'leader'

class FeedbackRequest(BaseModel):
    question: str = Field(max_length=500)
    rating: str
    reason: str = ''

def connect():
    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    with connect() as db:
        db.executescript('''CREATE TABLE IF NOT EXISTS units(name TEXT PRIMARY KEY, headcount INTEGER NOT NULL, vacancies INTEGER NOT NULL, mobility_events INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, rating TEXT, reason TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);''')
        if not db.execute('SELECT COUNT(*) FROM units').fetchone()[0]:
            db.executemany('INSERT INTO units VALUES (?,?,?,?)', [('Engineering',420,39,24),('Product',260,17,18),('Operations',220,14,12),('Sales',190,10,8),('Corporate',150,6,5)])
init_db()

@app.get('/health')
def health():
    return {'status':'ok','dataset':'synthetic','model':'deterministic retrieval, no LLM'}

@app.get('/api/summary')
def summary():
    with connect() as db:
        rows=[dict(r) for r in db.execute('SELECT * FROM units ORDER BY headcount DESC')]
    return {'units':rows,'headcount':sum(r['headcount'] for r in rows),'vacancies':sum(r['vacancies'] for r in rows),'dataset':'synthetic','snapshot':'2026-Q3','data_source':'sqlite.units'}

@app.post('/api/ask')
def ask(req:AskRequest):
    started=time.perf_counter()
    q=req.question.lower().strip()
    if re.search(r'\b(salary|salaries|medical|diagnos|employee name|individual|personal file|home address)\b',q):
        return make('refused','I cannot provide individual or sensitive workforce information. Please ask for an appropriately scoped aggregate.',[], 'privacy',started)
    if re.search(r'\b(who will resign|predict who|who should be fired|terminate whom|rank employees)\b',q):
        return make('abstained','No validated evidence supports individual personnel predictions or adverse decisions. I will not invent them.',[],'unsupported prediction',started)
    data=summary()
    if re.search(r'\b(headcount|workforce size|how many people|staff count)\b',q):
        return make('grounded',f"The fictional portfolio contains {data['headcount']:,} workers across five units. Engineering has the largest headcount at 420. A change over time cannot be calculated from this single snapshot.",[{'source':'sqlite.units','field':'headcount','operation':'SUM','value':data['headcount']}],None,started)
    if re.search(r'\b(vacanc|hiring|open positions|open roles|recruit)\b',q):
        leader=max(data['units'],key=lambda u:u['vacancies'])
        return make('grounded',f"There are {data['vacancies']} open roles in this synthetic portfolio. {leader['name']} has the most ({leader['vacancies']}). Validate criticality and time to fill before prioritising hiring.",[{'source':'sqlite.units','field':'vacancies','operation':'SUM','value':data['vacancies']},{'source':'sqlite.units','field':'vacancies','operation':'MAX_BY_UNIT','value':leader['vacancies']}],None,started)
    if re.search(r'\b(mobility|internal moves|transfers)\b',q):
        count=sum(r['mobility_events'] for r in data['units'])
        return make('grounded',f"There are {count} recorded internal mobility events in the illustrative snapshot. This is an event count, not a mobility rate; a valid rate requires a defined denominator and time window.",[{'source':'sqlite.units','field':'mobility_events','operation':'SUM','value':count}],None,started)
    return make('clarification','I cannot support that question from the approved synthetic dataset. Try headcount, hiring or mobility, or specify the metric and time period.',[],'no approved evidence',started)

def make(status,answer,evidence,reason,started):
    return {'status':status,'answer':answer,'evidence':evidence,'limitation':reason or 'Illustrative synthetic data; not Ericsson records.','latency_ms':round((time.perf_counter()-started)*1000,2),'model':'deterministic SQL-backed answer; no LLM'}

@app.post('/api/feedback')
def feedback(req:FeedbackRequest):
    if req.rating not in ('helpful','unhelpful'): raise HTTPException(422,'rating must be helpful or unhelpful')
    with connect() as db:
        db.execute('INSERT INTO feedback(question,rating,reason) VALUES (?,?,?)',(req.question,req.rating,req.reason))
    return {'saved':True,'storage':'local SQLite demo'}

@app.get('/api/feedback/summary')
def feedback_summary():
    with connect() as db:
        rows=[dict(r) for r in db.execute('SELECT rating, COUNT(*) as count FROM feedback GROUP BY rating')]
    counts={r['rating']:r['count'] for r in rows}
    return {'responses':sum(counts.values()),'helpful':counts.get('helpful',0),'unhelpful':counts.get('unhelpful',0),'note':'Local demo feedback, not real leader adoption'}
