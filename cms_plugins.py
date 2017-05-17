from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PayRaveModel
from django.conf import settings
from django.utils.translation import ugettext as _


class PayRave(CMSPluginBase):
    model = PayRaveModel  # model where plugin data are saved
    module = _("PayRave")
    name = _("Pay Rave")  # name of the plugin in the interface
    render_template = "pay_rave_integration/payrave_plugin.html"
    text_enabled = True


    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + 'payrave/images/purp.png'


    def icon_alt(self, instance):
        return u'PayRave: %s' % instance
plugin_pool.register_plugin(PayRave)  # register the plugin