/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PhoneField } from "@web/views/fields/phone/phone_field";
import { SendWhatsAppButton } from "@oe_whatsapp_web/whatsapp_button";

patch(PhoneField, {
    components: {
        ...PhoneField.components,
        SendWhatsAppButton,
    },
});
