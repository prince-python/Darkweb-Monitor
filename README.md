# 🌐 Dark Web Monitor

## 🚀 Features
- ✅ **Add & Manage Onion URLs** – Database me store hoti hai  
- 🔄 **Periodic Crawling** – Tor + Stem library se secure crawling  
- 📝 **Keyword Detection** – Specific keywords (e.g. company name, credentials) detect hoti hai  
- ⚠ **Alert System** – Console / Email alert (future feature)  
- 📊 **API Endpoints** – Easy REST API for integration  

---

## 🛠 Tech Stack
- **Backend:** FastAPI (Python)
- **Crawling:** Tor + Stem library
- **Database:** SQLite
- **Scheduler:** APScheduler (Background tasks)

---

## 📂 Project Structure
```
darkweb-monitor/
├── main.py              # FastAPI entry point
├── models.py            # SQLite database models
├── crawler.py           # Tor + Stem crawler logic
├── scheduler.py         # Periodic job scheduler
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/darkweb-monitor.git
cd darkweb-monitor
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows -> venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install & Configure Tor
- **Linux/Mac:**  
  ```bash
  sudo apt install tor
  ```
- **Windows:**  
  - Download Tor Browser → [https://www.torproject.org/download/](https://www.torproject.org/download/)  
  - Run Tor → set `ControlPort` in `torrc` file (default: 9051)

### 5️⃣ Run FastAPI Server
```bash
uvicorn main:app --reload
```
Server chalega:  
🔗 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔥 API Endpoints
| Method | Endpoint       | Description             |
|-------|---------------|-----------------------|
| POST  | `/add_url`     | Onion URL add karega |
| GET   | `/scan`        | Manual scan trigger   |
| GET   | `/results`     | Scan results fetch    |

---

## 🧠 Future Improvements
- [ ] Telegram/Email Alerts  
- [ ] Web Dashboard for Monitoring  
- [ ] AI-based Content Classification  

---

## 🤝 Contribution
PRs are welcome!

---

## 📜 License
MIT License – free to use & modify.

---

## 👤 Author
**Prince Chaudhary**  
🔗 [GitHub](https://github.com/prince-python) | [LinkedIn](https://www.linkedin.com/in/prince-chaudhary-253b36350/)
