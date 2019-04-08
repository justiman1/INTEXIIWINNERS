# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553993885.5965402
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
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def navbar_items2():
            return render_navbar_items2(context._locals(__M_locals))
        def left_column():
            return render_left_column(context._locals(__M_locals))
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
        def navbar_items():
            return render_navbar_items(context)
        def navbar_items2():
            return render_navbar_items2(context)
        __M_writer = context.writer()
        __M_writer('\r\n    \r\n    ')
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
        __M_writer('\r\n    <ul id="topic_list">\r\n        <li><a class="nav-link" href="/">Home</a></li>\r\n        <li><a class="nav-link" href="/contact/">Contact</a></li>\r\n        <li><a class="nav-link" href="/catalog/index/">Catalog</a></li>\r\n    </ul>\r\n    ')
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
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 8, "57": 3, "65": 3, "70": 7, "76": 5, "82": 5, "88": 10, "96": 10, "101": 18, "107": 16, "113": 16, "119": 113}}
__M_END_METADATA
"""
