/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";

const { Component } = owl;

export class SendWhatsAppButton extends Component {
    setup() {
        this.action = useService("action");
        this.title = this.env._t("Send WhatsApp");
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
                wa_number: this.props.value,
            },
        });
    }
}
SendWhatsAppButton.template = "oe_whatsapp_web.SendWhatsAppButton";
SendWhatsAppButton.props = ["*"];
