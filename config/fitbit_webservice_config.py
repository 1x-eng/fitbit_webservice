__author__ = 'pruthvi kumar'

"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: February 2, 2018

This is a simple python file that holds all the configuration parameters required for fitbit webservice wrapper.

"""

class Fitbit_Webservice_Config(object):

    def __init__(self):
        super(Fitbit_Webservice_Config, self).__init__()
        self.get_fitbit_endpoints = self._getFitbitEndpoints

    def _getFitbitEndpoints(self):
        """
        All the valid endpoints supported by Fitbit API's.

        :return: A dictionary with valid hash map for fitbit API's which will be utilized by the wrapper.

        """
        return {
            'todays_steps_realtime': '/1/user/-/activities/steps/date/today/1d.json',
            'last_7_days_steps': '/1/user/-/activities/steps/date/today/7d.json',
            'todays_calories_realtime': '/1/user/-/activities/calories/date/today/1d.json',
            'last_7_days_calories': '/1/user/-/activities/calories/date/today/7d.json',
            'todays_sedentary_minutes_realtime': '/1/user/-/activities/minutesSedentary/date/today/1d.json',
            'last_7_days_sedentary_minutes': '/1/user/-/activities/minutesSedentary/date/today/7d.json',
            'todays_lightly_active_minutes_realtime': '/1/user/-/activities/minutesLightlyActive/date/today/1d.json',
            'todays_fairly_active_minutes_realtime': '/1/user/-/activities/minutesFairlyActive/date/today/1d.json',
            'todays_very_active_minutes_realtime': '/1/user/-/activities/minutesVeryActive/date/today/1d.json',
            'last_7_days_lightly_active_minutes': '/1/user/-/activities/minutesLightlyActive/date/today/7d.json',
            'last_7_days_fairly_active_minutes': '/1/user/-/activities/minutesFairlyActive/date/today/7d.json',
            'last_7_days_very_active_minutes': '/1/user/-/activities/minutesVeryActive/date/today/7d.json',
            'todays_realtime_distance_covered': '/1/user/-/activities/distance/date/today/1d.json',
            'last_7_days_distance_covered': '/1/user/-/activities/distance/date/today/7d.json',
            'lifetime_activities_details': '/1/user/-/activities.json',
            'get_friends_leader_board': '/1/user/-/friends/leaderboard.json',
            'todays_sleep_details': '/1.2/user/-/sleep/date/today.json',
            'todays_heart_details': '/1/user/-/activities/heart/date/today/1d.json',
        }