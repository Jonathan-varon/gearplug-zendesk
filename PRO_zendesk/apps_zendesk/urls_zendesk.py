from django.conf.urls import url
from apps_zendesk.views import zendesk_webhook

urlpatterns = [
    url(r'^zendesk_webhook/$',zendesk_webhook, name="zendesk_webhookk"),



]