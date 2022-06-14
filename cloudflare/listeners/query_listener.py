import logging
from ulauncher.api.client.EventListener import EventListener

LOGGER = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):  # pylint: disable=unused-argument
        """ Handles the event """

        query = event.get_argument() or ""
        keyword_id = self.get_keyword_id(extension.preferences,
                                         event.get_keyword())

        if keyword_id == "kw_zones":
            return extension.list_zones(query)

        # TODO add support for more actions like pages, workers etc.

    def get_keyword_id(self, preferences, keyword):
        """ Returns the keyword ID from the keyword name """
        kw_id = None
        for key, value in preferences.items():
            if value == keyword:
                kw_id = key
                break

        return kw_id
