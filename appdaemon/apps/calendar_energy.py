import appdaemon.plugins.hass.hassapi as hass
import datetime

class CalendarEnergy(hass.Hass):
    def initialize(self):
        self.run_every(self.adjust_energy, "now", 3600)

    def adjust_energy(self, kwargs):
        event = self.get_state("calendar.household_event", attribute="start_time")
        temp = float(self.get_state("sensor.outdoor_temperature"))
        if event:
            self.call_service("climate/set_temperature", entity_id="climate.thermostat", temperature=70 if temp > 80 else 72)
