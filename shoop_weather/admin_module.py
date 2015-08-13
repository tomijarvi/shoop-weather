# -*- coding: utf-8 -*-
import random

from django.http.response import HttpResponse
from shoop.admin.base import AdminModule, MenuEntry
from shoop.admin.utils.urls import admin_url
from .kennel import PUGS

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }

        html, body {
            overflow: hidden;
            height: 100%;
        }

        body {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #222;
        }

        img {
            box-shadow: 0px 0px 60px -15px rgba(70, 200, 249, 0.87);
            animation-duration: 1s;
            animation-fill-mode: both;
            animation-name: fadeIn;
        }
    </style>
</head>
<body>
<p>Cloudy weather</p>
</body>
</html>"""


def weather_view(request):
    return HttpResponse(TEMPLATE))


class WeatherAdminModule(AdminModule):
    name = "Weather"

    def get_urls(self):
        return [
            admin_url("weather/$", pug_view, name="weather")
        ]

    def get_menu_entries(self, request):
        yield MenuEntry(
            category="Weather", text="Weather!",
            url="shoop_admin:weather", icon="fa fa-paw"
        )

    def get_menu_category_icons(self):
        return {
            "Pugs": "fa fa-paw"
        }
