## Codon Optimization Application
This app generates a resume from a provided LinkedIn profile URL. 
The api is a Flask application that by default starts at port `5555` and uses code from  [linked_scrapper](https://github.com/joeyism/linkedin_scraper) to scrape a given linkedIn URL.  



## Pre-Req - Must provide LinkedIn credentials for login
1. Python3
2. Chrome Browser

Make sure you have added your linkedIn email and password to the `config.ini` file inside the `api folder`. Otherwise, you will be asked to enter email and password in the terminal. 
# Note: 
You can also add the linkedIn cookie in the config.ini file. The advantage is that you won't be asked to reverify (capcha) for too many requests. To get the cookie follow these steps 
1.  Open LinkedIn in Chrome browser and login
3.  Open `developer tools` under the `Application tab` click cookies -> `wwww.linkedin.com` 
4.  Look for the key `li_at`, copy the `value` from the value column -> paste it in the `config.ini file` in front of `cookie = `

### Local Development
To start the backend service 

1.  `cd api`
3.  `pip install -r requirements.txt`
4.  `python app.py`

To start the frontend service

1.  `cd app`
2.  `npm install`
3.  `npm start`
