__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: September 26, 2017

This is a modification from awesome work of https://github.com/magnific0. His work has been a foundation for this web
service wrapper. I extend my sincere thanks to magnific0.

A Python library for accessing the FitBit API.

This library provides a wrapper to the FitBit API and does not provide storage of tokens or caching if that is required.

Most of the code has been adapted from: https://groups.google.com/group/fitbit-api/browse_thread/thread/0a45d0ebed3ebccb

5/22/2012 - JCF - Updated to work with python-oauth2 https://github.com/dgouldin/python-oauth2
10/22/2015 - JG - Removed use of oauth2 library (singing is not necessary anymore),
                  updated to use /oauth2/ authentication infrastructure to get access to more stats.
"""
import base64
import requests
import urllib
from config.fitbit_wrapper_config import Fitbit_Config

class Fitbit(Fitbit_Config):

    def __init__(self):
        super(Fitbit, self).__init__()
        self.static_config = self.get_static_config()
        self.dynamic_config = self.get_dynamic_config()

    def GetAuthorizationUri(self):

        params = {
            'client_id': self.dynamic_config['client_id'],
            'response_type':  'code',
            'scope': ' '.join(self.dynamic_config['api_scopes']),
            'redirect_uri': self.dynamic_config['redirect_uri']
        }

        # Encode parameters and construct authorization url to be returned to user.
        urlparams = urllib.parse.urlencode(params)
        return "%s?%s" % (self.static_config['authorization_url'], urlparams)

    # Tokes are requested based on access code. Access code must be fresh (10 minutes)
    def GetAccessToken(self, access_code):

        # Construct the authentication header
        auth_header = base64.b64encode(self.dynamic_config['client_id'] + ':' + self.dynamic_config['client_secret'])
        headers = {
            'Authorization': 'Basic %s' % auth_header,
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        # Paramaters for requesting tokens (auth + refresh)
        params = {
            'code': access_code,
            'grant_type': 'authorization_code',
            'client_id': self.dynamic_config['client_id'],
            'redirect_uri': self.dynamic_config['redirect_uri']
        }

        # Place request
        resp = requests.post(self.static_config['token_url'], data=params, headers=headers)
        status_code = resp.status_code
        resp = resp.json()

        if status_code != 200:
            raise Exception("Something went wrong exchanging code for "
                            "token (%s): %s" % (resp['errors'][0]['errorType'], resp['errors'][0]['message']))

        # Strip the goodies
        token = dict()
        token['access_token']  = resp['access_token']
        token['refresh_token'] = resp['refresh_token']

        return token

    # Get new tokens based if authentication token is expired
    def RefAccessToken(self, token):

        # Construct the authentication header
        auth_header = base64.b64encode(self.dynamic_config['client_id'] + ':' + self.dynamic_config['client_secret'])
        headers = {
            'Authorization': 'Basic %s' % auth_header,
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        # Set up parameters for refresh request
        params = {
            'grant_type': 'refresh_token',
            'refresh_token': token['refresh_token']
        }

        # Place request
        resp = requests.post(self.static_config['token_url'], data=params, headers=headers)

        status_code = resp.status_code
        resp = resp.json()

        if status_code != 200:
            raise Exception("Something went wrong refreshing "
                            "(%s): %s" % (resp['errors'][0]['errorType'], resp['errors'][0]['message']))

        # Distil
        token['access_token']  = resp['access_token']
        token['refresh_token'] = resp['refresh_token']
        print("&&&&&&&&& LOG:[fitbitPyWrapper] Token refresh is successful!")
        return token

    # Place api call to retrieve data
    def ApiCall(self, token, apiCall='/1/user/-/activities/log/steps/date/today/1d.json'):
        # Other API Calls possible, or read the FitBit documentation for the full list
        # (https://dev.fitbit.com/docs/), e.g.:
        # apiCall = '/1/user/-/devices.json'
        # apiCall = '/1/user/-/profile.json'
        # apiCall = '/1/user/-/activities/date/2015-10-22.json'

        headers = {
            'Authorization': 'Bearer %s' % token['access_token']
        }

        final_url = 'https://' + self.static_config['api_server'] + apiCall

        resp = requests.get(final_url, headers=headers)

        status_code = resp.status_code

        resp = resp.json()
        resp['token'] = token
        if status_code == 200:
            return resp
        elif status_code == 401:
            print("&&&&&&&&& LOG:[fitbitPyWrapper] The access token you provided has been expired let me "
                  "refresh that for you.")
            try:
                # Refresh the access token with the refresh token if expired. Access tokens should be good for 1 hour.
                token = self.RefAccessToken(token)
                print("&&&&&&&&& LOG:[fitbitPyWrapper] Making another API call with new refreshed tokens. "
                      "EndPoint is: {}".format(apiCall))
                # important to return here. This ensures valid return is returned to the context which asked for it.
                # Else, return will be triggered to the line 145 as that is invoking the function recursively.
                # That way, the results to original context will become none!
                return self.ApiCall(token, apiCall)

            except Exception as e:
                print("&&&&&&&&& LOG:[fitbitPyWrapper] Error refreshing token; pickle if already exists; will be "
                      "replaced with new contents. Notifying client for fresh oAuth authorization")
                return {'uri': self.GetAuthorizationUri(), 'status': 'Fitbit oAuth to be performed',
                'authStatus': 'not completed'}
        else:
            #raise Exception("Something went wrong requesting (%s): %s" % (resp['errors'][0]['errorType'],
            # resp['errors'][0]['message']))
            print("&&&&&&&&& LOG:[fitbitPyWrapper] Error refreshing token; pickle if already exists; will be "
                  "replaced with new contents. Notifying client for fresh oAuth authorization")
            return {'uri': self.GetAuthorizationUri(), 'status': 'Fitbit oAuth to be performed',
                    'authStatus': 'not completed'}