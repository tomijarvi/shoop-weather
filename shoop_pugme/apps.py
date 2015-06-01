# -*- coding: utf-8 -*-


from shoop.apps import AppConfig


class PugConfig(AppConfig):
    name = "shoop_pugme"
    provides = {
        "admin_module": [
            "shoop_pugme.admin_module:PugAdminModule"
        ]
    }
