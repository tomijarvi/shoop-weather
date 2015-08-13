# -*- coding: utf-8 -*-


from shoop.apps import AppConfig


class PugConfig(AppConfig):
    name = "shoop_weather"
    provides = {
        "admin_module": [
            "shoop_weather.admin_module:WeatherAdminModule"
        ]
    }
