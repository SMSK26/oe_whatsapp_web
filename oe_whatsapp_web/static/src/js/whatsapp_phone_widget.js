odoo.define('oe_whatsapp_web.fields', function (require) {
"use strict";

var basic_fields = require('web.basic_fields');
var core = require('web.core');

var _t = core._t;

/**
 * Override of FieldPhone to add an inline WhatsApp link (res.partner only),
 * shown next to the Call / SMS links on the phone & mobile fields.
 */
var Phone = basic_fields.FieldPhone;
Phone.include({
    /**
     * Open the WhatsApp wizard pre-filled with this field's number.
     *
     * @private
     */
    _onClickWhatsApp: function (ev) {
        ev.preventDefault();
        ev.stopPropagation();
        if (this.model !== 'res.partner') {
            return;
        }
        var context = {
            default_partner_id: parseInt(this.res_id),
            wa_number: this.value,
        };
        return this.do_action({
            name: _t('Send WhatsApp'),
            type: 'ir.actions.act_window',
            res_model: 'oe.whatsapp.web.wizard',
            target: 'new',
            views: [[false, 'form']],
            context: context,
        });
    },

    /**
     * Append the WhatsApp link after the phone number (readonly, contacts only).
     *
     * @override
     * @private
     */
    _renderReadonly: function () {
        var def = this._super.apply(this, arguments);
        if (this.model === 'res.partner' && this.value) {
            var $waButton = $('<a>', {
                title: _t('Send WhatsApp'),
                href: '',
                class: 'ml-3 d-inline-flex align-items-center o_field_phone_whatsapp text-success',
                html: $('<small>', {class: 'font-weight-bold ml-1', html: 'WhatsApp'}),
            });
            $waButton.prepend($('<i>', {class: 'fa fa-whatsapp'}));
            $waButton.on('click', this._onClickWhatsApp.bind(this));
            this.$el = this.$el.add($waButton);
        }
        return def;
    },
});

return Phone;

});
