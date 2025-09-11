# app/crawler.py
import requests
from stem import Signal
from stem.control import Controller
from app.models import SessionLocal, DarkWebURL, ScanResult
import os

# Load keywords from .env
KEYWORDS = os.getenv("KEYWORDS", "password,database,leak").split(",")

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    return session

def crawl_darkweb():
    db = SessionLocal()
    urls = db.query(DarkWebURL).all()
    session = get_tor_session()

    for entry in urls:
        try:
            response = session.get(entry.url, timeout=15)
            content = response.text.lower()
            matched = [kw for kw in KEYWORDS if kw.lower() in content]

            result = ScanResult(
                url=entry.url,
                status="Online" if response.status_code == 200 else f"HTTP {response.status_code}",
                matched_keywords=", ".join(matched) if matched else "None"
            )
            db.add(result)
            db.commit()
        except Exception as e:
            result = ScanResult(url=entry.url, status=f"Error: {str(e)}", matched_keywords="None")
            db.add(result)
            db.commit()

    db.close()
