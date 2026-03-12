# SonarQube Python Demo Project

This project demonstrates integrating **Python testing, coverage, and SonarQube static code analysis** in a DevOps workflow.

## Project Structure


Sonar-project/
│
├── app.py
├── test_app.py
├── sonar-project.properties
├── coverage.xml
├── README.md
└── .gitignore


## Tools Used

- Python
- Pytest
- Coverage.py
- SonarScanner
- SonarQube Community Edition
- Git

## Setup

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies
pip install pytest pytest-cov coverage

3. Run tests with coverage
pytest --cov=. --cov-report=xml

This generates:
coverage.xml

4. Run SonarQube analysis
sonar-scanner
SonarQube Dashboard

After successful analysis, open:

http://localhost:9000

or (WSL networking)

http://<windows-host-ip>:9000

Example:

http://172.25.112.1:9000
DevOps Workflow
Code → Tests (pytest) → Coverage → SonarScanner → SonarQube Dashboard

This setup simulates a basic CI code quality pipeline.

Author
Jay Gupta
