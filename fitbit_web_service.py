__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: February 17, 2018

This is the entry point file for Gunicorn. This file contains all the routes to respectrive fitbit webservices.
"""

import falcon
from falcon_cors import CORS

from apiLayer.fitbitStore import FitbitWebServiceInit as defaultRoute
from apiLayer.fitbitStore import AuthorizeFitbitApi as authFitbit
from apiLayer.fitbitStore import FitbitAcknowledgeAuthorization as acknowledgeFitbitAuth
from apiLayer.fitbitStore import FitbitApiAnalytics as processFitbitApi
from apiLayer.fitbitStore import ValidateAuthorizationStatus as validateAuthStatus

cors = CORS(allow_all_origins=['http://localhost:8000']) #Allow CORS for this endpoint.
app = falcon.API(middleware=[cors.middleware,])

app.add_route('/', defaultRoute())
app.add_route('/authorizeFitbitApi', authFitbit())
app.add_route('/fitbitAuthCallback', acknowledgeFitbitAuth())
app.add_route('/validateFitbitAuthStatus', validateAuthStatus())
app.add_route('/processFitbitApi', processFitbitApi())



