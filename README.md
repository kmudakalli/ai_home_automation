# AI Home Automation Project

This project uses Home Assistant and AppDaemon to build an AI-enhanced smart home automation system that responds to user behavior, weather conditions, and scheduled events.

Predictive Lighting: Uses AppDaemon and presence detection to automatically adjust lighting when you arrive home.
Behavioral HVAC Control: Trains a machine learning model to predict user arrival patterns and preemptively set temperature.
Calendar-Based Automation: Integrates Google Calendar to prepare rooms before meetings or scheduled events.
Weather-Based Lighting: Adjusts brightness and color temperature on overcast days to maintain comfort.
Offline Redundancy: Includes a fallback script to run local automations in case of internet or Home Assistant service failure.

Technologies: Python, AppDaemon, Home Assistant, YAML, scikit-learn, joblib, requests, Raspberry Pi (for local fallback)

Setup:
1. Run the `train_model.py` script inside `model_training/` to generate `home_return_model.pkl`
2. Move the `.pkl` model file to `models/` and `/config/appdaemon/apps/` if running in Home Assistant
3. Install Home Assistant and AppDaemon
4. Copy automations and apps into the appropriate directories
5. Configure `appdaemon.yaml` and `apps.yaml` as needed
6. Restart AppDaemon and Home Assistant
