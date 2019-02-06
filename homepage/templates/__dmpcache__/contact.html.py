# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549430151.2842526
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/contact.html'
_template_uri = 'contact.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def left_column2():
            return render_left_column2(context._locals(__M_locals))
        def right_column():
            return render_right_column(context._locals(__M_locals))
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
        __M_writer('Contact')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column2(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column2():
            return render_left_column2(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <form method="POST">\r\n        <p>Name: <input type="text" name="yourname" /></p>\r\n        <p>Email: <input type="email" name="youremail" /></p>\r\n        <input type="submit" />\r\n        \r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 7, "57": 18, "62": 22, "68": 3, "74": 3, "80": 5, "86": 5, "92": 9, "98": 9, "104": 20, "110": 20, "116": 110}}
__M_END_METADATA
"""
