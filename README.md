# Ulauncher Cloudflare

> Ulauncher extension that provides quick access to your Cloudflare sites.

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-cloudflare)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-cloudflare/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz7ulauncher-cloudflare)
![License](https://img.shields.io/github/license/brpaz/ulauncher-cloudflare.svg?style=for-the-badge)

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher 5](https://ulauncher.io/)
* Python >= 3
* A [CloudFlare](https://cloudflare.com) account and an API token. (https://dash.cloudflare.com/profile/api-tokens)

For this extension to work, the [python-cloudflare](https://github.com/cloudflare/python-cloudflare) Python package must be installed on your system.

You can install the correct version, by running the following command in the terminal after you downloaded the extension:

```bash
cd ~/.local/share/ulauncher/extensions/com.github.brpaz.ulauncher-cloudflare
pip install -r requirements.txt
```

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```<%= https://github.com/brpaz/ulauncher-cloudflare %>```

## Usage

Before using the plugin, you must configure your Cloudflare account in the plugin settings, by adding your API Token
You can get yours from your CloudFlare account [here](https://dash.cloudflare.com/profile/api-tokens).

⚠️ **In previous versions of this extension, we used API key and email for user authentication. This was changed to a simpler API tokens. If you had an older version of this extension installed, please ensure that you have the correct configurations.**

Next, simply type `cloudflare` on the ulauncher input bar, to access the extension.


## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## License

Copywright @ 2020 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
