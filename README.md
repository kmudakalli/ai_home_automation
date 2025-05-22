# AI Home Automation 

Uses Home Assistant and AppDaemon to build an AI-enhanced smart home automation system that responds to user behavior, weather conditions, and scheduled events.

uses AppDaemon and presence detection to automatically adjust lighting when you arrive home
trains machine learning model to predict user arrival patterns and set temperature ahead of time
calendar based automation: integrates Google Calendar to prepare room before meetings (close curtains, brighten lights, etc.)
adjusts brightness and color temperature on overcast days to maintain comfort.
offline redundancy fallback script on rasbperry pi

Technologies: Python, AppDaemon, Home Assistant, YAML, scikit-learn, joblib, requests, Raspberry Pi (for local fallback)

Setup:
1. Run the `train_model.py` script inside `model_training/` to generate `home_return_model.pkl`
2. Move the `.pkl` model file to `models/` and `/config/appdaemon/apps/` if running in Home Assistant
3. Install Home Assistant and AppDaemon
4. Copy automations and apps into the appropriate directories
5. Configure `appdaemon.yaml` and `apps.yaml` as needed
6. Restart AppDaemon and Home Assistant
