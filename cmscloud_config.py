# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        settings['JQUERY_JS'] = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
        settings['JQUERY_UI_JS'] = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
        settings['JQUERY_UI_CSS'] = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
        settings['CMSPLUGIN_BLOG_PLACEHOLDERS'] = ('excerpt', 'content',)
        return settings