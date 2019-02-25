# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550676993.3896415
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'left_column2', 'center_column']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def left_column2():
            return render_left_column2(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column2'):
            context['self'].left_column2(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column2():
            return render_left_column2(context)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n<p>This is a fun project used to help us learn django-mako-plus</p>\r\n<br>\r\n<p>This content will only appear on the homepage.</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n<h1>Welcome to Sprint 1!</h1>\r\n<br>\r\n<br>\r\n<p>Please enjoy this picture of Usain Bolt, the world\'s fastest sprinter.</p>\r\n<img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/UsainBolt.jpg" alt="Usain Bolt" id="usainbolt"/>\r\n<p>This image comes from <a href="https://i.ytimg.com/vi/Q8FaDru7sBU/maxresdefault.jpg" style="color:black">https://i.ytimg.com/vi/Q8FaDru7sBU/maxresdefault.jpg</a></p>\r\n<br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 10, "62": 3, "68": 3, "74": 5, "80": 5, "86": 12, "94": 12, "95": 18, "96": 18, "102": 96}}
__M_END_METADATA
"""
