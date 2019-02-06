# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549466689.4782822
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['navbar_items', 'navbar_items2', 'left_column', 'left_column2']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_items2():
            return render_navbar_items2(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_column2():
            return render_left_column2(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items2():
            return render_navbar_items2(context)
        request = context.get('request', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<nav class="navbar">\r\n    <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/">Home</a></li>\r\n    <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/contact/">Contact</a></li>\r\n    <li class="nav-item"><a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a></li>\r\n    <li class="nav-item">\r\n        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown">\r\n            Welcome, User\r\n        </a>\r\n        <div class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n            <a class="dropdown-item" href="/account/index/">Account</a>\r\n            <div class="dropdown-divider"></div>\r\n            <a class="dropdown-item" href="/account/logout/">Logout</a> \r\n        </div>\r\n    </li>\r\n</nav>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items2'):
            context['self'].navbar_items2(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items2():
            return render_navbar_items2(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        def left_column2():
            return render_left_column2(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul>\r\n        <li><a class="nav-link" href="/">Home</a></li>\r\n        <li><a class="nav-link" href="/contact/">Contact</a></li>\r\n    </ul>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column2'):
            context['self'].left_column2(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column2():
            return render_left_column2(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 22, "59": 3, "69": 3, "70": 5, "71": 5, "72": 6, "73": 6, "74": 7, "75": 7, "80": 21, "86": 19, "92": 19, "98": 24, "106": 24, "111": 31, "117": 29, "123": 29, "129": 123}}
__M_END_METADATA
"""
