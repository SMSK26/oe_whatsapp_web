{
    'name': 'WhatsApp Web Redirect | Click-to-Chat from Contacts | Send WhatsApp Messages from Odoo',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Send WhatsApp Messages Directly from Odoo Contacts | Click-to-Chat | Pre-filled Message via WhatsApp Web',
    'description': """
WhatsApp Web Redirect for Odoo 18
=================================

Reach your contacts on WhatsApp in one click — straight from the Odoo contact form.
No API keys, no webhooks, no third-party services. Just a clean wizard that opens
WhatsApp Web with the chat and message ready to send.

KEY FEATURES
============

ONE-CLICK CHAT
--------------
- Inline WhatsApp button right next to the contact's mobile field
- Button auto-hides when no mobile number is set
- Opens a wizard with the contact and phone pre-filled

PRE-FILLED MESSAGE WIZARD
-------------------------
- Type your message inside Odoo before opening WhatsApp
- Phone number is sanitized to digits-only international format
- Edit the number on the fly if formatting needs a fix

DIRECT WHATSAPP WEB REDIRECT
----------------------------
- Skips the wa.me interstitial - lands straight on web.whatsapp.com
- Chat opens with your message ready in the input box
- Send with one final click in WhatsApp Web

ZERO CONFIGURATION
------------------
- Install and use - no setup, no credentials, no provider account
- Depends only on stock Odoo base + contacts
- Does not interfere with any existing WhatsApp Business API module

PERFECT FOR
-----------
- Sales teams reaching leads from the CRM contact form
- Support teams following up with customers
- Property / real-estate agents messaging tenants and buyers
- Any team that already uses WhatsApp Web on desktop

WHY CHOOSE THIS MODULE?
=======================
- No monthly API fees - uses your own WhatsApp Web session
- No risk of account bans from unofficial APIs
- Works with personal and WhatsApp Business numbers alike
- Lightweight: one transient wizard, one inherited view, one CSV
- Clean uninstall - leaves no residual data

If you like this module, please rate us on the Odoo App Store!
    """,
    'author': 'Sheikh Muhammad Saad, OdooElevate',
    'website': 'https://odooelevate.odoo.com/',
    'support': 'support@odooelevate.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/oe_whatsapp_web_wizard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'oe_whatsapp_web/static/src/whatsapp_button.js',
            'oe_whatsapp_web/static/src/whatsapp_button.xml',
            'oe_whatsapp_web/static/src/whatsapp_phone_field.js',
            'oe_whatsapp_web/static/src/whatsapp_phone_field.xml',
        ],
    },
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'sequence': 1,
}
