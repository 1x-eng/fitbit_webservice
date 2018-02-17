# FITBIT WEB SERVICE USING PYTHON

FITBIT Api's are authenticated by oAuth2.0. In here, there is a Python Web Service coded as a wrapper around Fitbit's conventional API's using Python's Falcon Web Services Framework. 

NOTE: THIS CODEBASE USES FALCON & GUNICORN TO  FACILITATE WEB SERVICE. GUNICORN WORKS ONLY ON UNIX/LINUX MACHINES. HENCE, THIS WILL BE OPERATIONAL ONLY ON LINUX DISTRO'S /UNIX MACHINES. WINDOWS IMPLEMENTATION IS WIP.

# Features:
  - oAuth Authorization callable via dedicated endpoint.
  - Fitbit config will be easy and manageable.
  - Multithreaded usage using gunicorn server to build seamless apps using Fitbit data.

# Setup:
- Create a valid fitbit account and setup an App here - https://dev.fitbit.com/apps/new
- Make notes of client ID and client secret.
- clone this repo; ensure to cd into the directory 'firbit_webservice'.
- cd fitbit_webservice/config -> edit file named 'fitbit_wrapper_config.py', add client ID and client secret where its asked to; save.
- pip install all the requirements (Python=3). (NOTE: Always better to create a dedicated virtual environment. Either using Anaconda /Conventional Python)
- To start the web service, type the following command (whilst staying on 'fitbit_webservice' directory):
```sh
    gunicorn -b localhost:8000 fitbit_web_service:app --reload
```
- The above command must start gunicorn server locally and listen on port 8000 (Please feel free to change this to your convinience).
- Go to webserver and check with this endpoint:
```sh
    http://localhost:8000/processFitbitApi?keyword=todays_steps_real_time
```
- When the above request is served for the first time, oAuth will carry on with its magic to create valid token's for usage. Response from these requests will be self-explanatory.

# Support
For any issues write to Pruthvi @ pruthvikumar.123@gmail.com. Ensure to have a valid subject line, detailed message with appropriate stack trace to expect prompt/quick response. 

# License
----
MIT
