<<<<<<< HEAD
# Numerology-Automation

A multi-platform numerology intelligence system integrating Python, Bash, PostgreSQL, Azure SQL, Hyper-V infrastructure, VB.NET, Power BI, and GitHub CI/CD automation.

This project automates numerology calculations, stores reports, visualizes trends, and simulates enterprise-grade deployment architecture using on-premises and cloud tools.

---
## Overview 

The **Numerology Automation Project** is a Python-based backend system designed to calculate advanced numerology reports from a user's name, birthdate, and location. Built with Flask and PostgreSQL, it generates unique, fingerprinted reports and supports scalable deployment with Docker and script automation. 


---
## Features

- **Calculates multiple numerology values**, including:
 - Life Path Number
 - Expression Number
 - Soul Urge Number
 - Personality Number
 - Destiny Number
 - Pinnacle Cycles
 - Personal Year/Month/Day Cycles


- Numerology Calculation Engine (`numerology.py`)
- Flask API (`app.py`) to serve results to web and desktop clients
- PostgreSQL + SQLite backend for persistent report storage
- VB.NET WinForms App (in development) for user interaction
- Azure SQL integration for scalable cloud analytics
- Power BI dashboards and Apache Superset visualizations
- Bitwarden for secure credential management
- GitHub Actions for continuous integration & automated builds
- Unit tested with 'pytest' and 'test_utils.py'
**Normalized geographic storage** with PostgreSQL foreign keys: Country, State, City
**Uniqueness detection** via SHA-256 fingerprinting
- Python Virtual Environment & 'requirements.txt' integration
- Docker-ready containerization with 'Dockerfile' included
- Bash automation scripts and Docker-ready environment
- Optional tool support:
 - Microsoft ODBC (future MS SQL expansion)
 - MariaDB / MySQL (multi-database flexibility)
 - MongoDB (planned for NoSQL use cases) 
- pfSense firewall VM for network simulation
- Hyper-V lab with Ubuntu, Bitwarden, Solr, Superset, and pfSense

---

## Technologies Used

- **Languages**: Python 3.11, Bash, VB.NET, T-SQL
- **Backend Framework**: Flask
- **Databases**: PostgreSQL, SQLite, Azure SQL
- **DevOps**: GitHub Actions, Docker (future)
- **Visualization**: Power BI, Apache Superset
- **VM/Infra**: Hyper-V, pfSense, Ubuntu 24.04, Bitwarden
- **Security**: Bitwarden, pfSense firewall
- **CI/CD**: GitHub Workflows
- **Search & Indexing**: Apache Solr (future) 

---

## Architecture Overview

```plaintext
             +------------------+          
             |   VB.NET Client  |  ← Windows App (.NET Framework)
             +------------------+          
                     |
                     ▼
          +----------------------+
          |     Flask API        |  ← app.py
          +----------------------+
                 ▲        ▼
     +----------------+   +--------------------+
     | PostgreSQL DB  |   | numerology.py logic|
     +----------------+   +--------------------+
                 ▲
                 ▼
     +--------------------------+
     | Azure SQL / Apache Solr |
     +--------------------------+
                 ▼
        +---------------------+
        | Power BI / Superset |
        +---------------------+

=======

## 📁 Directory Structure

```
numerology-backend/
├── app.py                 # Main Flask app
├── install.sh             # Automated environment and dependency setup
├── fix_psycopg2_and_sources.sh # Optional fix script
├── utils.py               # Numerology logic and helper functions
├── test_utils.py          # Unit tests for numerology functions
├── test_app.py            # API route tests
├── requirements.txt       # Python dependencies
├── .env                   # Environment variable config (not committed)
├── Dockerfile             # Docker container config
├── README.md              # Project overview
├── numerology.db          # (Optional) Local SQLite or export file
└── venv/                  # Python virtual environment (local only)
```

## 🚀 Quick Start

### 🔧 Installation (Manual)
```bash
git clone https://github.com/yourusername/Numerology-Automation.git
cd Numerology-Automation
bash install.sh
```

### 🐳 Run with Docker
```bash
docker build -t numerology-backend .
docker run -p 5000:5000 --env-file .env numerology-backend
```

### 🔬 Run Tests
```bash
pytest test_utils.py
pytest test_app.py
```

## 📌 TODO / Roadmap

- [ ] Add authentication (JWT-based)
- [ ] Integrate MongoDB for report history
- [ ] Enable frontend dashboard (React / Vue)
- [ ] Export reports to PDF
- [ ] Graphical report generation via Power BI

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your proposed modifications.

## ⚠️ Disclaimer

This is an educational and personal development project. Numerology results are not scientific and should not be used as a substitute for professional advice.
>>>>>>> master
