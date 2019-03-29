# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553810430.099951
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'center_column']


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
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        numpages = context.get('numpages', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

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
        __M_writer('Catalog')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def center_column():
            return render_center_column(context)
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="text-center">\r\n    <h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Products' if category is None else category.name ))
        __M_writer('</h1>\r\n    <div id="catalog">\r\n')
        for product in products:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\r\n')
        __M_writer('    </div>\r\n</div>\r\n    <div id="paginator" class="text-center">\r\n        <br>\r\n        <a class="btn btn-secondary" href="/catalog/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
        __M_writer('/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page if page == 1 else (page - 1) ))
        __M_writer('">Back</a>\r\n        <a class="btn btn-secondary" href="/catalog/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
        __M_writer('/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page if page == numpages else (page + 1) ))
        __M_writer('">Next</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "53": 19, "59": 3, "65": 3, "71": 5, "82": 5, "83": 7, "84": 7, "85": 9, "86": 10, "87": 10, "88": 10, "89": 12, "90": 16, "91": 16, "92": 16, "93": 16, "94": 17, "95": 17, "96": 17, "97": 17, "103": 97}}
__M_END_METADATA
"""
