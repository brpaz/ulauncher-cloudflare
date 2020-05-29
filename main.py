"""
Ulauncher CloudFlare extension
This extension allows you to access your cloudflare domains directly from Ulauncher
"""

import logging
import CloudFlare

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

LOGGER = logging.getLogger(__name__)


class CloudFlareExtension(Extension):
    """ Main extension class """
    def __init__(self):
        """ init method """
        LOGGER.info('Initializing CloudFlare Extension')
        super(CloudFlareExtension, self).__init__()

        # initializes CloudFlare Client
        self.cf_client = None

        # Event listeners
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def get_zones(self, event):
        """ Returns the list of Zones from Cloudflare """
        items = []

        query = event.get_argument() or ""

        zones = self.cf_client.zones.get()

        for zone in zones:

            if query.lower() not in zone["name"].lower():
                continue

            url = "https://dash.cloudflare.com/%s/%s" % (zone["account"]['id'],
                                                         zone["name"])
            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name=zone["name"],
                                    description=zone["status"],
                                    on_enter=OpenUrlAction(url)))

        if not items:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='No results found matching your criteria',
                    highlightable=False))

        return items


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """
    def on_event(self, event, extension):  # pylint: disable=unused-argument
        """ Handles the event """

        items = []

        try:
            items = extension.get_zones(event)

        except CloudFlare.exceptions.CloudFlareError as e:
            LOGGER.error(e)
            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name="CloudFlare API error",
                                    description="Error %s : %s" %
                                    (e.evalue.code, e.evalue.message),
                                    on_enter=HideWindowAction(),
                                    highlightable=False))

        return RenderResultListAction(items[:8])


class PreferencesEventListener(EventListener):
    """
    Listener for prefrences event.
    It is triggered on the extension start with the configured preferences
    """
    def on_event(self, event, extension):
        """ Handles Preferences change event """
        extension.cf_client = CloudFlare.CloudFlare(
            email=event.preferences['email'],
            token=event.preferences['api_key'])


class PreferencesUpdateEventListener(EventListener):
    """
    Listener for "Preferences Update" event.
    It is triggered when the user changes any setting in preferences window
    """
    def on_event(self, event, extension):
        """ Handles Prefences Update event """
        if event.id == 'api_key':
            extension.cf_client = CloudFlare.CloudFlare(
                email=extension.preferences['email'], token=event.new_value)
        elif event.id == 'email':
            extension.cf_client = CloudFlare.CloudFlare(
                email=event.new_value, token=extension.preferences['api_key'])


if __name__ == '__main__':
    CloudFlareExtension().run()
