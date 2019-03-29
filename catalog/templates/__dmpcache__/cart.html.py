# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553892170.999669
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        SI = context.get('SI', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def center_column():
            return render_center_column(context._locals(__M_locals))
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
        SI = context.get('SI', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def center_column():
            return render_center_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<table>\r\n    <tr>\r\n        <td>Product Image</td>\r\n        <td>Product Name</td>\r\n        <td>Quantity</td>\r\n        <td>Price</td>\r\n        <td>Extended</td>\r\n        <td>Actions</td>\r\n    </tr>\r\n')
        for item in SI:
            __M_writer('        <tr>\r\n            <td><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.product.image_url(item.product.images_url()) ))
            __M_writer('" class="cart_image"></td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.product.name ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.quantity ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.price ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.price * item.quantity ))
            __M_writer('</td>\r\n            <td><a href="/catalog/remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( item.id ))
            __M_writer('" class="remove">Remove</td>\r\n        </tr>\r\n')
        __M_writer('    <tr>\r\n        <td></td>\r\n        <td>Tax</td>\r\n        <td></td>\r\n        <td></td>\r\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.tax ))
        __M_writer('</td>\r\n        <td></td>\r\n    </tr>\r\n    <tr>\r\n        <td></td>\r\n        <td>Total</td>\r\n        <td></td>\r\n        <td></td>\r\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.total ))
        __M_writer('</td>\r\n        <td></td>\r\n    </tr>\r\n</table>\r\n\r\n<a href="/catalog/checkout/" class="btn btn-primary">Check Out</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "51": 45, "57": 3, "63": 3, "69": 5, "78": 5, "79": 16, "80": 17, "81": 18, "82": 18, "83": 19, "84": 19, "85": 20, "86": 20, "87": 21, "88": 21, "89": 22, "90": 22, "91": 23, "92": 23, "93": 26, "94": 31, "95": 31, "96": 39, "97": 39, "103": 97}}
__M_END_METADATA
"""
