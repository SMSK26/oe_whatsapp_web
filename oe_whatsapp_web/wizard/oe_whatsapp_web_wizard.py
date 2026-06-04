import re
from urllib.parse import quote

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class OeWhatsappWebWizard(models.TransientModel):
    _name = 'oe.whatsapp.web.wizard'
    _description = 'Send WhatsApp Message via WhatsApp Web'

    partner_id = fields.Many2one(
        'res.partner',
        string='Contact',
        required=True,
        readonly=True,
    )
    phone = fields.Char(
        string='Phone Number',
        required=True,
        help='International format, digits only. Example: 965xxxxxxxx',
    )
    message = fields.Text(
        string='Message',
        required=True,
    )

    @staticmethod
    def _sanitize_phone(value):
        return re.sub(r'\D', '', value or '')

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        partner_id = defaults.get('partner_id') or self.env.context.get('default_partner_id')
        if not partner_id and self.env.context.get('active_model') == 'res.partner':
            partner_id = self.env.context.get('active_id')
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            if partner.exists():
                defaults.setdefault('partner_id', partner.id)
                if 'phone' in fields_list and not defaults.get('phone'):
                    raw = self.env.context.get('wa_number') or partner.phone or ''
                    defaults['phone'] = self._sanitize_phone(raw)
        return defaults

    def action_send(self):
        self.ensure_one()
        number = self._sanitize_phone(self.phone)
        if not number:
            raise UserError(_(
                "Please enter a valid phone number in international format "
                "(digits only, no '+' or spaces)."
            ))
        url = "https://web.whatsapp.com/send?phone=%s&text=%s" % (
            number, quote(self.message or ''),
        )
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
