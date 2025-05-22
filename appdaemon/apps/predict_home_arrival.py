import appdaemon.plugins.hass.hassapi as hass
import datetime
import pandas as pd
import joblib

class PredictHomeArrival(hass.Hass):
    def initialize(self):
        self.model = joblib.load("/config/appdaemon/apps/home_return_model.pkl")
        self.run_every(self.check_prediction, "now", 60 * 60)

    def check_prediction(self, kwargs):
        now = datetime.datetime.now()
        hour = now.hour
        weekday = now.weekday()
        prediction = self.model.predict([[hour, weekday]])
        if prediction[0] == 1:
            self.log("User likely returning soon, preparing home")
            self.turn_on("light.living_room")
            self.turn_on("climate.thermostat")
