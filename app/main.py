# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models import init_db, SessionLocal, DarkWebURL, ScanResult
from app.crawler import crawl_darkweb

app = FastAPI()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    init_db()

@app.post("/add_url/")
def add_url(url: str, description: str, db: Session = Depends(get_db)):
    new_url = DarkWebURL(url=url, description=description)
    db.add(new_url)
    db.commit()
    return {"message": "URL added", "url": url}

@app.get("/urls/")
def list_urls(db: Session = Depends(get_db)):
    return db.query(DarkWebURL).all()

@app.get("/crawl/")
def crawl_now():
    crawl_darkweb()
    return {"message": "Crawl completed"}

@app.get("/results/")
def list_results(db: Session = Depends(get_db)):
    return db.query(ScanResult).order_by(ScanResult.timestamp.desc()).all()
 