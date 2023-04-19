# scaping-selenium

## Installation

Clone repository
```
git clone https://github.com/akushyn/scraping-selenium.git
```

Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt 
```

Create `.env` from `env.example` file and update as needed
```
cp env.example .env
```

### Run application

Ensure, that `social-network` application is running
```
cd scraping-selenium
python3 app.py
```