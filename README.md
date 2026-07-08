# 🛡️ Mini SIEM Dashboard

A lightweight **Security Information and Event Management (SIEM)** dashboard built using **Flask** and **SQLite**. This project parses Linux authentication logs, stores them in a database, and displays them through a web dashboard. It is being developed as a cybersecurity portfolio project.

---

## 📌 Features

### ✅ Current Features
- Flask web application
- SQLite database integration
- Linux authentication log parser
- Stores parsed logs into SQLite
- Project structured using modular folders
- Git version control

### 🚧 Upcoming Features
- Dashboard statistics
- Failed SSH login detection
- Brute-force attack detection
- Suspicious sudo command detection
- Search and filter logs
- Interactive charts using Plotly
- Alert severity levels
- User authentication
- PDF/CSV report generation
- Real-time log monitoring
- Deployment on Render

---

## 🛠️ Tech Stack

- Python 3.11
- Flask
- SQLite
- HTML5
- CSS3
- Git & GitHub

---

## 📂 Project Structure

```
SIEM-DASHBOARD/
│
├── alerts/
│   └── detection.py
│
├── database/
│   └── db.py
│
├── logs/
│   └── auth.log
│
├── parser/
│   └── parser.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── database.db
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/SIEM-DASHBOARD.git
```

Move into the project

```bash
cd SIEM-DASHBOARD
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Initialize the database

```bash
python database/db.py
```

Parse sample logs

```bash
python parser/parser.py
```

Start Flask server

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📊 Workflow

```
Linux Logs
      │
      ▼
Log Parser
      │
      ▼
SQLite Database
      │
      ▼
Flask Backend
      │
      ▼
SIEM Dashboard
```

---

## 🎯 Learning Objectives

- Log Parsing
- Security Event Monitoring
- Database Management
- Flask Backend Development
- Cybersecurity Dashboard Design
- Detection Rule Development
- Secure Coding Practices

---

## 📸 Screenshots

Screenshots will be added after the dashboard UI is completed.

---

## 🚀 Future Improvements

- [ ] Bootstrap UI
- [ ] Plotly Charts
- [ ] Alert Dashboard
- [ ] Login Authentication
- [ ] CSV Export
- [ ] PDF Reports
- [ ] REST API
- [ ] Real-time Log Monitoring
- [ ] Docker Support
- [ ] Deploy on Render

---

## 👨‍💻 Author

**Himanshu Gidwani**

B.Tech CSE (Cyber Security)

GitHub: https://github.com/HGidwani2005

---

## ⭐ Project Status

🚧 Currently under active development.