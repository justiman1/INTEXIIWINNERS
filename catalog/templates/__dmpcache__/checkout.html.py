# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553891756.9182646
_enable_loop = True
_template_filename = 'C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['center_column']


from django.conf import settings 

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
        def center_column():
            return render_center_column(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        stripeTotal = context.get('stripeTotal', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_column'):
            context['self'].center_column(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_column():
            return render_center_column(context)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        stripeTotal = context.get('stripeTotal', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<form action="" method="post">\r\n    \r\n        <table>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table()))
        __M_writer(' \r\n        </table>\r\n        <!-- <input type="submit" class="btn btn-info" value="Buy Now"> -->\r\n\r\n    <script\r\n    src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n    data-key="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STRIPE_PUBLIC_KEY ))
        __M_writer('"\r\n    data-amount="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( stripeTotal ))
        __M_writer('"\r\n    data-name="Stripe.com"\r\n    data-description="Widget"\r\n    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n    data-locale="auto"\r\n    data-zip-code="true">\r\n  </script>\r\n\r\n</form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/justi/OneDrive/Desktop/School/Winter 2019/IS 413/sprint/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "47": 26, "53": 4, "62": 4, "63": 9, "64": 9, "65": 15, "66": 15, "67": 16, "68": 16, "74": 68}}
__M_END_METADATA
"""
