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
<img src="URL">
</body>
</html>"""


def pug_view(request):
    return HttpResponse(TEMPLATE.replace("URL", random.choice(PUGS)))


class PugAdminModule(AdminModule):
    name = "Pugs"

    def get_urls(self):
        return [
            admin_url("pug/$", pug_view, name="pug")
        ]

    def get_menu_entries(self, request):
        yield MenuEntry(
            category="Pugs", text="Pug me!",
            url="shoop_admin:pug", icon="fa fa-paw"
        )

    def get_menu_category_icons(self):
        return {
            "Pugs": "fa fa-paw"
        }
