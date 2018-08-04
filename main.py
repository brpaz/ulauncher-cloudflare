"""Ulauncher extension main class"""

import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import CloudFlare

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


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """

        items = []
        try:
            zones = extension.cf_client.zones.get()

            for zone in zones:
                url = "https://dash.cloudflare.com/%s/%s" % (
                    zone["account"]['id'], zone["name"])
                items.append(ExtensionResultItem(icon='images/icon.png',
                                                 name=zone["name"],
                                                 description=zone["status"],
                                                 on_enter=OpenUrlAction(url)))
        except CloudFlare.exceptions.CloudFlareError as e:  # pylint: disable=invalid-name
            LOGGER.error(e)
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name="CloudFlare API error",
                                             description="Error %s : %s" % (
                                                 e.evalue.code, e.evalue.message),
                                             on_enter=HideWindowAction()))

        return RenderResultListAction(items)


class PreferencesEventListener(EventListener):
    """
    Listener for prefrences event.
    It is triggered on the extension start with the configured preferences
    """

    def on_event(self, event, extension):
        extension.cf_client = CloudFlare.CloudFlare(
            email=event.preferences['email'],
            token=event.preferences['api_key']
        )


class PreferencesUpdateEventListener(EventListener):
    """
    Listener for "Preferences Update" event.
    It is triggered when the user changes any setting in preferences window
    """

    def on_event(self, event, extension):
        if event.id == 'api_key':
            extension.cf_client = CloudFlare.CloudFlare(
                email=extension.preferences['email'],
                token=event.new_value
            )
        elif event.id == 'email':
            extension.cf_client = CloudFlare.CloudFlare(
                email=event.new_value,
                token=extension.preferences['api_key']
            )


if __name__ == '__main__':
    CloudFlareExtension().run()
