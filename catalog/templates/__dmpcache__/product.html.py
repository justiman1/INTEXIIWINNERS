# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553814093.771547
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/product.html'
_template_uri = 'product.html'
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
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def center_column():
            return render_center_column(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        product = context.get('product', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="catalog">\r\n        <div class="product-tile">\r\n')
        for image in product.images_url():
            if image == product.images_url()[0]:
                __M_writer('                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( image ))
                __M_writer('" class="product-image">\r\n')
            else:
                __M_writer('                    <div class="subimage">\r\n                        <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( image ))
                __M_writer('" class="small-image">\r\n                    </div>\r\n')
        __M_writer('\r\n\r\n            <h3 class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer('</h3>\r\n            <p class="product-price">$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.price ))
        __M_writer('</p>\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.description))
        __M_writer('\r\n        </div> \r\n\r\n        <!--Form here-->\r\n<br>\r\n        <div class="center">\r\n            <form action="" method="post">\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
        __M_writer('\r\n                <input type="submit" value="Buy Now">\r\n            </form>\r\n        </div>\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "56": 3, "64": 3, "70": 5, "79": 5, "80": 8, "81": 9, "82": 10, "83": 10, "84": 10, "85": 11, "86": 12, "87": 13, "88": 13, "89": 17, "90": 19, "91": 19, "92": 20, "93": 20, "94": 21, "95": 21, "96": 28, "97": 28, "103": 97}}
__M_END_METADATA
"""
