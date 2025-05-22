import appdaemon.plugins.hass.hassapi as hass
import datetime

class PredictiveLighting(hass.Hass):
    def initialize(self):
        self.listen_state(self.arrived_home, "person.you", new="home")

    def arrived_home(self, entity, attribute, old, new, kwargs):
        hour = datetime.datetime.now().hour
        temp = float(self.get_state("sensor.outdoor_temperature"))
        if 17 <= hour <= 22 and temp < 75:
            self.call_service("light/turn_on", entity_id="light.living_room", brightness=200)
