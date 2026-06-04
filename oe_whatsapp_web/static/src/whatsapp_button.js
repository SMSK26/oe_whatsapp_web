/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

export class SendWhatsAppButton extends Component {
    static template = "oe_whatsapp_web.SendWhatsAppButton";
    static props = ["*"];

    setup() {
        this.action = useService("action");
        this.title = _t("Send WhatsApp");
    }

    async onClick() {
        await this.props.record.save();
        this.action.doAction({
            type: "ir.actions.act_window",
            target: "new",
            name: this.title,
            res_model: "oe.whatsapp.web.wizard",
            views: [[false, "form"]],
            context: {
                default_partner_id: this.props.record.resId,
                wa_number: this.props.record.data[this.props.name],
            },
        });
    }
}
