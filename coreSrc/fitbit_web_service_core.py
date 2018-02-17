__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: February 17, 2018

This frames the core for extracting contents from fitbit wrapper and serializing results into a web service output.
JSON is the means of communication at this moment.

FALCON is the web service framework that is made use of. Falcon deploys itself onto gunicorn server.
"""

import json
import os
import pickle
from config.fitbit_webservice_config import Fitbit_Webservice_Config
from coreSrc.fitbitPyWrapper import Fitbit


class FitbitAnalytics(Fitbit, Fitbit_Webservice_Config):

    def __init__(self):
        super(FitbitAnalytics, self).__init__()

        self.__pickleTokenName = 'pk_fitbit_tokens.pickle'
        self.__apiStore = self.get_fitbit_endpoints()

        self.authoriseAccess = self._authoriseAccess
        self.generateTokens = self._generateTokenFromAccessCode
        self.storeTokens = self._storeTokensToPickle
        self.getTokens = self._getTokensFromPickle
        self.getFitbitDetails = self._makeApiCall
        self.checkPickleExistence = self._checkIfPickleExists

    def _authoriseAccess(self):
        return {'uri': self.GetAuthorizationUri(), 'status': 'Fitbit oAuth to be performed',
                'authStatus': 'not completed'}


    def _generateTokenFromAccessCode(self, accessCode):
        return self.GetAccessToken(accessCode)

    def _checkIfPickleExists(self):

        try:
            pickle.load(open(self.__pickleTokenName, 'rb'))
            return True
        except (OSError, IOError) as e:
            return False

    def _storeTokensToPickle(self, tokens):
        """

        :param tokens: A dict containing access token and refresh token.
        :return:
        """
        with open (self.__pickleTokenName, 'wb') as handle:
            pickle.dump(tokens, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def _getTokensFromPickle(self):

        try:
            with open(self.__pickleTokenName, 'rb') as handle:
                tokens = pickle.load(handle)
                return tokens
        except Exception as e:
            print ("&&&&&&&&& LOG: [fitbitAnalytics] Error unpickling. Either pickle doesnt exist or there was some"
                   "other issue. Issuing fresh authorization request. Stack trace to follow\n")
            print(str(e))
            print('&&&&&&&&& LOG: [fitbitAnalytics]: End of stack trace')
            return self.authoriseAccess()

    def _refreshAccessToken(self):

        try:
            with open(self.__pickleTokenName, 'rb') as handle:
                oldTokens = pickle.load(handle)
                newTokens = self.RefAccessToken(oldTokens)
                self.storeTokens(newTokens)
                return newTokens
        except Exception as e:
            print ("&&&&&&&&& LOG: [fitbitAnalytics] Error unpickling during refreshing tokens. Either pickle doesnt "
                   "exist or there was some other issue. Issuing fresh authorization request. Stack trace to follow\n")
            print(str(e))
            print('&&&&&&&&& LOG: [fitbitAnalytics]: End of stack trace')
            self.authoriseAccess()

    def _makeApiCall(self, keyword):
        #todo: based on keyword, persist appropriate data into db.

        try:
            token = self.getTokens()

            if 'uri' in token:
                return json.dumps(token)

            results = self.ApiCall(token, self.__apiStore[keyword])
            if 'uri' in results:
                #delete existing pickle
                os.remove(self.__pickleTokenName)
                return results
            # store tokens from result in pickle and revoke tokens from results. Client need not know them.
            self.storeTokens(results['token'])
            del results['token']

            #TODO: Custom PK's processing for sleep and heart details!

            return results

        except Exception as e:
            print("[fitbitAnalytics - error log: ] Something did not work as expected whilst connecting to the API's."
                  " Stack trace to follow\n")
            print(str(e))
            print("--------- END of stack trace ---------\n")
            print("Attempting to re-initialize the fitbit API's by destroying existing store...")
            # delete pickle file
            os.remove(self.__pickleTokenName)
            print("Reissuing api call to fitbit with keyword: {}".format(keyword))
            self._makeApiCall(keyword)

if __name__ == '__main__':
    fa = FitbitAnalytics()
    print(fa.getFitbitDetails('todays_heart_details'))