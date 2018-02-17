__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: February 17, 2018

This file contains web service response for Fitbit Activities.This file leverages of business
functionality from fitbit_webservice_core module.
"""

import falcon
import json
from coreSrc.fitbit_web_service_core import FitbitAnalytics


class FitbitWebServiceInit(object):

    def __init__(self):
        super(FitbitWebServiceInit, self).__init__()

    def on_get(self, req, resp):
        resp.body = json.dumps({'Message': 'Fitbit Webservice is successfully Initialized. This is successful '
                                           'route to default message. Please continue to use valid endpoints '
                                           'to get the desired results. For any support, please reach out to PK @'
                                           'pruthvikumar.123@gmail.com with detailed message.'})
        resp.status = falcon.HTTP_200

class VerifyAuthorizationCompletion(object):

    authorizationCompleted = False

    def __init__(self):
        super(VerifyAuthorizationCompletion, self).__init__()


class ValidateAuthorizationStatus(object):

    def __init__(self):
        super(ValidateAuthorizationStatus, self).__init__()

    def on_get(self, req, resp):
        resp.body = json.dumps({'AuthorizationStatus': VerifyAuthorizationCompletion.authorizationCompleted})


class AuthorizeFitbitApi(FitbitAnalytics):

    def __init__(self):
        super(AuthorizeFitbitApi, self).__init__()

    def on_get(self, req, resp):

        resp.body = json.dumps(self.authoriseAccess())
        resp.status = falcon.HTTP_200

class FitbitAcknowledgeAuthorization(FitbitAnalytics):

    def __init__(self):
        super(FitbitAcknowledgeAuthorization, self).__init__()

    def on_get(self, req, resp):
        #todo: More promising defensive programming here.
        access_code = req.get_param('code') or None

        if (access_code != None):
            tokens = self.generateTokens(access_code)
            self.storeTokens(tokens)

            if self.checkPickleExistence() == True:
                authorizationFlag = 'success'
                VerifyAuthorizationCompletion.authorizationCompleted = True
                print("&&&&&&&&& LOG:[FitbitStore]: FitbitAuth completed successfully.")

            else:
                authorizationFlag = 'failure'

            resp.body = json.dumps({'authorization': authorizationFlag,
                                    'message': 'You may close this tab. Fitbit oAuth acknowledgement is completed. '
                                               'If authorization is tagged under failure, please contact PK @ '
                                               'pruthvikumar.123@gmail.com with clear message. Do note to include subject '
                                               'as "Fitbit oAuth Failure" to get prompt response ASAP.'})
            resp.status = falcon.HTTP_200
        else:
            resp.body = json.dumps({'message': 'Authorization has not been successful! Please ensure a valid ' \
                                              'token/code is provided for the request to succeed'})
            resp.status = falcon.HTTP_400

class FitbitApiAnalytics(FitbitAnalytics):

    def __init__(self):
        super(FitbitApiAnalytics, self).__init__()

    def on_get(self, req, resp):

        keyword = req.get_param('keyword') or None

        if (keyword != None):
            #check if pickle containing accessTokens exist
            activitiesResults = json.dumps(self.getFitbitDetails(keyword))
            if (self.checkPickleExistence() == True):
                resp.body = activitiesResults
                resp.status = falcon.HTTP_200
            else:
                resp.body = json.dumps(self.authoriseAccess())
                resp.status = falcon.HTTP_428
        else:
            resp.body = json.dumps({'message': 'A valid keyword is required for fitbit web service wrapper to function'
                                               ' seamlessly. Please refer to allowed keywords to pass a valid one.'})
            resp.status = falcon.HTTP_400



