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

### Chromedriver
Download from official website proper version of chromedriver for your OS: https://chromedriver.chromium.org/downloads
- Update path to `chromedriver` executable in env variable
- Allow `chromedriver` to run on MacOS 
```
xattr -d com.apple.quarantine chromedriver
```
### Run application

Ensure, that `social-network` application is running
```
cd scraping-selenium
python3 app.py
```