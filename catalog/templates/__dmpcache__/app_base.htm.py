# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552690645.880837
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['left_column']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<ul id="category_list">\r\n    <li class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category is None else '' ))
        __M_writer('"><a href="/catalog/index/">All Products</a></li>\r\n')
        for cat in cmod.Category.objects.order_by('name'):
            __M_writer('        <li class="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category == cat else '' ))
            __M_writer('"><a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.id ))
            __M_writer('/">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.name ))
            __M_writer('</a></li>\r\n')
        __M_writer('</ul>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "40": 1, "41": 2, "51": 4, "59": 4, "60": 6, "61": 6, "62": 7, "63": 8, "64": 8, "65": 8, "66": 8, "67": 8, "68": 8, "69": 8, "70": 10, "76": 70}}
__M_END_METADATA
"""
