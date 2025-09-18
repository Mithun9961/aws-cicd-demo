```markdown
# AWS DevOps Engineer – Demo Assignment

This is a sample **Python Flask Web Application** deployed with **CI/CD on AWS Elastic Beanstalk** using **GitHub Actions**.  
It includes a login page and a simple dashboard to demonstrate deployment automation.

---

## 🚀 Features
- Login page with demo credentials
- Dashboard page (protected, only after login)
- CI/CD pipeline with GitHub Actions
- Deployment on AWS Elastic Beanstalk
- Uses `gunicorn` as production server

---

## 🔑 Demo Credentials
- **Email**: `hire-me@anshumat.org`  
- **Password**: `HireMe@2025!`

---

## 📂 Project Structure
```

/app.py               # Flask application
/requirements.txt     # Python dependencies
/Procfile             # EB startup config
/templates/           # HTML templates
├── login.html
└── dashboard.html

````

---

## 🛠️ Setup Instructions

### 1. Run Locally
Make sure you have Python 3.11+ installed.
```bash
# Clone repo
git clone https://github.com/your-username/demo-flask-app.git
cd demo-flask-app

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
````

App will be available at **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

### 2. Deploy to AWS Elastic Beanstalk

1. Zip the project files (`app.py`, `requirements.txt`, `Procfile`, and `templates/` folder).
2. Create an **Elastic Beanstalk Python environment** on AWS.
3. Upload the zip to deploy.

---

### 3. CI/CD with GitHub Actions

We use a workflow (`.github/workflows/deploy.yml`) that:

* Triggers on push to `main`
* Installs dependencies
* Zips app and deploys to Elastic Beanstalk

Secrets to configure in GitHub:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`
* `EB_APP_NAME`
* `EB_ENV_NAME`

---

## ✅ Demo Login

Once deployed, open the Elastic Beanstalk environment URL and login using:

* Email: **[hire-me@anshumat.org](mailto:hire-me@anshumat.org)**
* Password: **HireMe\@2025!**

---

## 📊 Architecture Diagram

(Include your draw\.io or Lucidchart diagram here showing: GitHub → GitHub Actions → AWS Elastic Beanstalk)

---

## 🔒 Security Best Practices

* No hardcoded credentials (uses GitHub Secrets + AWS IAM)
* Session-based authentication
* Gunicorn for production serving

```
