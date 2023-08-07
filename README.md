# FITBIT WEB SERVICE USING PYTHON

Python wrapper; a RESTful wrapper over FITBIT.

NOTE: uses gunicorn (https://docs.gunicorn.org/en/stable/index.html) which is WSGI HTTP server for `*nix` systems. On windows, you might want to swap gunicorn with uWSGI or other alternatives.

# Features:
  - oAuth via dedicated endpoint.
  - config is simpler.
  - leverages concurrency & threading - so its decently fast.

# Getting Started:
- Create a valid fitbit account and setup an `App` here - https://dev.fitbit.com/apps/new
- Grab your `client ID` and `client secret`.
- Clone &  `cd fitbit_webservice`
- Edit `fitbit_wrapper_config.py` > add client ID and client secret > save.
- `pip install -r requirements.txt` in venv of your choice.
```sh
gunicorn -b localhost:8000 fitbit_web_service:app --reload
```
- Interact with your webservice with dedicated #Keywords:
```sh
http://localhost:8000/processFitbitApi?keyword=todays_steps_real_time
```

# Keywords
- todays_steps_realtime: Get Real time steps (Until last sync with the device) from fitbit.
- last_7_days_steps: Get total steps covered for last 7 days.
- todays_calories_realtime: Get calories burned for for current day.
- last_7_days_calories: Get calories burned data for last 7 days.
- todays_sedentary_minutes_realtime: Get sedentary minutes for current day.
- last_7_days_sedentary_minutes: Get sedentary minutes for last 7 days.
- todays_lightly_active_minutes_realtime: Get lightly active minutes for current day.
- todays_fairly_active_minutes_realtime: Get fairly active minutes for current day.
- todays_very_active_minutes_realtime: Get very active minutes for current day.
- last_7_days_lightly_active_minutes: Get lightly active minutes for last 7 days.
- last_7_days_fairly_active_minutes: Get fairly active minutes for last 7 days.
- last_7_days_very_active_minutes: Get very active minutes for last 7 days.
- todays_realtime_distance_covered: Get distance covered for current day.
- last_7_days_distance_covered: Get distnace covered for last 7 days.
- lifetime_activities_details: Get fitbit lifetime activities details. 
- get_friends_leader_board: Get friends leader board details. 
- todays_sleep_details: Get sleep details for current day.
- todays_heart_details: Get heart details for current day.

# License
----
MIT License

Copyright (c) 2018 Pruthvi Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
