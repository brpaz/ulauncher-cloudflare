from ulauncher.api.client.EventListener import EventListener
import CloudFlare


class PreferencesEventListener(EventListener):
    """
    Listener for prefrences event.
    It is triggered on the extension start with the configured preferences
    """

    def on_event(self, event, extension):
        """ Handles Preferences change event """
        extension.cf_client = CloudFlare.CloudFlare(
            debug=True, token=event.preferences['api_token'])


class PreferencesUpdateEventListener(EventListener):
    """
    Listener for "Preferences Update" event.
    It is triggered when the user changes any setting in preferences window
    """

    def on_event(self, event, extension):
        """ Handles Prefences Update event """
        if event.id == 'api_token':
            extension.cf_client = CloudFlare.CloudFlare(token=event.new_value)
