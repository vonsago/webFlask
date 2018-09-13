#!/usr/bin/env python
# coding=utf-8
'''
> File Name: i18n.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  9/13 15:52:38 2018
'''

from flask import Blueprint, g, jsonify, request
from flask_babel import Babel, lazy_gettext as _

#from app.config.common import config

def i18n(app):
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = config.I18N_DIR
    app.config['BABEL_DEFAULT_LOCALE'] = config.I18N_DEFAULT_LOCALE
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, 'user', None)
        if user is not None:
            return getattr(user, 'locale')
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        brower_languages = request.accept_languages.best_match(['en', 'zh'])
        if brower_languages:
            return brower_languages
        return 'zh'

    @babel.timezoneselector
    def get_timezone():
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone

    return babel
