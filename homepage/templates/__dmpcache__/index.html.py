# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553993656.2103696
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'left_column2', 'center_column', 'right_column']


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
        def right_column():
            return render_right_column(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_column2():
            return render_left_column2(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
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
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n')
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
        def center_column():
            return render_center_column(context)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n<h1>Welcome to Sprint 4!</h1>\r\n<br>\r\n<br>\r\n<p>Please enjoy this picture of Usain Bolt, the world\'s fastest sprinter.</p>\r\n<img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/UsainBolt.jpg" alt="Usain Bolt" id="usainbolt"/>\r\n<p>This image comes from <a href="https://i.ytimg.com/vi/Q8FaDru7sBU/maxresdefault.jpg" style="color:black">https://i.ytimg.com/vi/Q8FaDru7sBU/maxresdefault.jpg</a></p>\r\n<br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n<p>This is Home Page content</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "54": 10, "59": 21, "64": 32, "70": 3, "76": 3, "82": 5, "88": 5, "94": 12, "102": 12, "103": 18, "104": 18, "110": 23, "116": 23, "122": 116}}
__M_END_METADATA
"""
