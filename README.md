# SonarQube Python Demo Project

> Demonstrates integrating **Python testing**, **coverage reporting**, and **SonarQube static analysis** in a DevOps workflow.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Tools Used](#tools-used)
- [Setup](#setup)
- [Running Tests & Coverage](#running-tests--coverage)
- [SonarQube Analysis](#sonarqube-analysis)
- [DevOps Workflow](#devops-workflow)
- [Author](#author)

---

## Project Structure

```
Sonar-project/
│
├── app.py                     # Application source code
├── test_app.py                # Pytest test suite
├── sonar-project.properties   # SonarScanner configuration
├── coverage.xml               # Coverage report (generated)
├── README.md
└── .gitignore
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python | Application language |
| Pytest | Unit testing framework |
| Coverage.py | Code coverage measurement |
| SonarScanner | Sends analysis to SonarQube |
| SonarQube Community Edition | Static code analysis dashboard |
| Git | Version control |

---

## Setup

### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install pytest pytest-cov coverage
```

---

## Running Tests & Coverage

Run tests and generate the XML coverage report:

```bash
pytest --cov=. --cov-report=xml
```

This produces `coverage.xml`, which SonarQube uses to display coverage metrics.

---

## SonarQube Analysis

### Run the scanner

```bash
sonar-scanner
```

### View the dashboard

After a successful scan, open SonarQube in your browser:

| Environment | URL |
|-------------|-----|
| Local | http://localhost:9000 |
| WSL (via Windows host) | http://\<windows-host-ip\>:9000 |
| Example | http://172.25.112.1:9000 |

---

## DevOps Workflow

```
Code  →  Tests (pytest)  →  Coverage Report  →  SonarScanner  →  SonarQube Dashboard
```

This setup simulates a basic CI/CD code quality pipeline — catching bugs and coverage gaps before they reach production.

---

## Author

**Jay Gupta**
