# 🏥 Health Records Management System — Secure Web Application

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Security](https://img.shields.io/badge/Security-Auth%20%7C%20RBAC-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

**Health Records Management System** is a full-stack web application for securely managing patient health records. It implements robust **authentication, role-based access control, data confidentiality, and integrity verification** — the four core pillars of healthcare data security — through a web interface with HTML templates and static assets.

---

## 🛡️ Security Architecture

| Module | Purpose |
|--------|---------|
| `authentication.py` | Secure login & user session management |
| `access_control.py` | Role-based permissions (read/write per role) |
| `confidentiality.py` | Encryption of sensitive patient data |
| `integrity.py` | Hash-based data integrity verification |
| `db_setup.py` | Database schema and initialisation |

---

## 🎯 Features

- 🔐 **Secure Authentication** — Username/password with hashed credentials
- 👥 **Role-Based Access Control** — Different views for doctors, nurses, admins
- 🔒 **Data Encryption** — Patient records encrypted at rest
- ✅ **Integrity Checking** — SHA hashes verify data hasn't been tampered with
- 🌐 **Web Interface** — HTML/CSS templates with a clean clinical UI
- 🗄️ **Database Backend** — SQLite for local data storage

---

## 📁 Project Structure

```
healthrecords/
│
├── health_records/
│   ├── main.py              # Application entry point
│   ├── authentication.py    # Login & session logic
│   ├── access_control.py    # RBAC enforcement
│   ├── confidentiality.py   # Encryption/decryption
│   ├── integrity.py         # Hash verification
│   ├── db_setup.py          # Database schema setup
│   ├── requirements.txt     # Dependencies
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML Jinja2 templates
│
├── template.py              # Project scaffolding helper
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/homeshwarnelakurthi/healthrecords.git
cd healthrecords/health_records
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialise the database
```bash
python db_setup.py
```

### 4. Run the application
```bash
python main.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Flask | Web framework |
| SQLite | Database |
| Jinja2 | HTML templating |
| hashlib | Data integrity hashing |
| cryptography | Patient data encryption |

---

## 👨‍💻 Author

**Homeswar Rao Nelakurthi**
[![GitHub](https://img.shields.io/badge/GitHub-homeshwarnelakurthi-181717?style=flat&logo=github)](https://github.com/homeshwarnelakurthi)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
