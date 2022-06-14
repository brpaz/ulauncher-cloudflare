"""
Ulauncher CloudFlare extension
This extension allows you to access your cloudflare domains directly from Ulauncher
"""

from cloudflare.extension import CloudFlareExtension

if __name__ == '__main__':
    CloudFlareExtension().run()
