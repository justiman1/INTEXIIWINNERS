# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551054351.0407205
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_items', 'left_column', 'center_column', 'right_column']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def left_column():
            return render_left_column(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def right_column():
            return render_right_column(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Sprint 1 &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css">\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n')
        __M_writer('        <link rel="icon" type="image/png" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/byu.png">\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <div id="maintenance_container">\r\n            <div id="maintenance_message" class="alert alert-danger center-block">The server is going offline tonight for two hours.</div>\r\n        </div>\r\n\r\n        <header id="header">\r\n\r\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/byu.png" alt="byu logo" id="image"/>\r\n                <br>\r\n                <ul class="nav nav-tabs justify-content-end">\r\n                    <nav class="navbar">\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                            <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/">Home</a></li>\r\n                            <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/contact/">Contact</a></li>\r\n                            <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a></li>\r\n                            <li class="nav-item">\r\n')
        if user.is_authenticated:
            __M_writer('                                    <div class="dropdown">\r\n                                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                        Account\r\n                                        </button>\r\n                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n                                                <a class="dropdown-item" href="/account/logout/">Logout</a>\r\n                                        </div>\r\n                                    </div>\r\n')
        else:
            __M_writer('                                    <a class="nav-link" href="/account/login/">Login</a></li>\r\n')
        __M_writer('                            </li>\r\n                    </nav>\r\n                </ul>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="left_block">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n            </div>   \r\n\r\n            <div id="center_block">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n            </div>  \r\n            \r\n            <div id="right_block">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n            </div>   \r\n\r\n            \r\n \r\n        </main>\r\n\r\n        <footer>\r\n                ')
        __M_writer('\r\n            <p>&copy; Copyright ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().strftime("%Y") ))
        __M_writer('. All rights reserved</p>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 82, "20": 0, "39": 2, "44": 7, "45": 10, "46": 10, "47": 10, "48": 13, "49": 13, "50": 16, "51": 17, "52": 17, "53": 20, "54": 20, "55": 20, "56": 31, "57": 31, "62": 36, "63": 37, "64": 37, "65": 38, "66": 38, "67": 39, "68": 39, "69": 41, "70": 42, "71": 50, "72": 51, "73": 53, "78": 62, "83": 68, "88": 74, "89": 82, "90": 83, "91": 83, "97": 7, "108": 35, "114": 35, "120": 60, "126": 60, "132": 66, "138": 66, "144": 72, "150": 72, "156": 150}}
__M_END_METADATA
"""
