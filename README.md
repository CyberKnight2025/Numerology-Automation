# Numerology-Automation

A multi-platform numerology intelligence system integrating Python, Bash, PostgreSQL, Azure SQL, Hyper-V infrastructure, VB.NET, Power BI, and GitHub CI/CD automation.

This project automates numerology calculations, stores reports, visualizes trends, and simulates enterprise-grade deployment architecture using on-premises and cloud tools.

---

## Features

- Numerology Calculation Engine (`numerology.py`)
- Flask API (`app.py`) to serve results to web and desktop clients
- PostgreSQL + SQLite backend for persistent report storage
- VB.NET WinForms App (in development) for user interaction
- Azure SQL integration for scalable cloud analytics
- Power BI dashboards and Apache Superset visualizations
- ⚙Bash automation scripts and Docker-ready environment
- Bitwarden for secure credential management
- pfSense firewall VM for network simulation
- Hyper-V virtual lab with Ubuntu, Bitwarden, Solr, Superset, and pfSense
- GitHub Actions for continuous integration & automated builds

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

