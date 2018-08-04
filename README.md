# ulauncher-cloudflare

> Ulauncher plugin for quickly access to your CloudFlare Zones Configuration.

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7
* CloudFlare Python package (```pip install cloudflare```)
* A [CloudFlare](https://cloudflare.com) account and an API Key.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```<%= https://github.com/brpaz/ulauncher-cloudflare %>```

## Usage

Before using the plugin, you must configure your Cloudflare account in the plugin settings, by adding your user email and an API Key.
You can get your API key, on "My Profile" page in CloudFlare.

## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## License

MIT
