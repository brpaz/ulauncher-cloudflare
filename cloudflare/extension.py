import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from cloudflare.listeners.query_listener import KeywordQueryEventListener
from cloudflare.listeners.preferences_listener import PreferencesEventListener, PreferencesUpdateEventListener
import CloudFlare

LOGGER = logging.getLogger(__name__)


class CloudFlareExtension(Extension):
    """ Main extension class """

    def __init__(self):
        """ init method """
        LOGGER.info('Initializing CloudFlare Extension')
        super(CloudFlareExtension, self).__init__()

        self.icon_path = "images/icon.png"
        # initializes CloudFlare Client
        self.cf_client = None

        # Event listeners
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def list_zones(self, query):
        """ Returns the list of Zones from Cloudflare """

        items = []

        try:

            zones = self.cf_client.zones.get()

            for zone in zones:
                if query.lower() not in zone["name"].lower():
                    continue

                url = "https://dash.cloudflare.com/%s/%s" % (
                    zone["account"]['id'], zone["name"])
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

            return RenderResultListAction(items)

        except CloudFlare.exceptions.CloudFlareError as e:
            LOGGER.error(e)

            return RenderResultListAction([
                ExtensionResultItem(icon=self.icon_path,
                                    name="CloudFlare API error",
                                    description="Error %s : %s" %
                                    (e.evalue.code, e.evalue.message),
                                    on_enter=HideWindowAction(),
                                    highlightable=False)
            ])
