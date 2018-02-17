__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: February 2, 2018

This is a simple python file that holds all the configuration parameters required for the Fitbit wrapper to function.
This will be the only file that needs to be edited in order to get the web service functional (Given all the
requirements from requirements.txt are satisfied).

"""

class Fitbit_Config(object):

    def __init__(self):
        super(Fitbit_Config, self).__init__()
        self.get_static_config = self.__static_config
        self.get_dynamic_config = self._dynamic_config

    def __static_config(self):
        """
        DO NOT CHANGE ANYTHING HERE.
        :return: a dictionary of static config required for Fitbit Wrapper.
        """

        # These settings should probably not be changed.
        API_SERVER = 'api.fitbit.com'
        WWW_SERVER = 'www.fitbit.com'
        AUTHORIZE_URL = 'https://%s/oauth2/authorize' % WWW_SERVER
        TOKEN_URL = 'https://%s/oauth2/token' % API_SERVER

        return {
            'api_server': API_SERVER,
            'www_server': WWW_SERVER,
            'authorization_url': AUTHORIZE_URL,
            'token_url': TOKEN_URL
        }

    def _dynamic_config(self):
        """
        Use this section to copy your fitbit client ID, client secret and alter redirect URL.
        For more help on getting client ID, client secret , visit - https://dev.fitbit.com/apps page

        Redirect URL is the URL that OAuth must redirect once its successfully authorized.

        :return: a dictionary of dynamic config required for Fitbit wrapper.
        """

        CLIENT_ID = 'XXXXX' # Add your client ID here.
        CLIENT_SECRET = 'xxxxx' # Add your client secret here.
        REDIRECT_URI = 'http://localhost:8000/fitbitAuthCallback' # Add your redirect URI here.

        # Decide which information the FitBit.py should have access to.
        # Options: 'activity', 'heartrate', 'location', 'nutrition',
        #          'profile', 'settings', 'sleep', 'social', 'weight'

        API_SCOPES = ('activity', 'heartrate', 'location', 'nutrition', 'profile', 'settings', 'sleep', 'social',
                      'weight')

        return {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'api_scopes': API_SCOPES
        }
