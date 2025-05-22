/** @odoo-module **/

import { useState } from "@odoo/owl";
import { PosComponent } from "@point_of_sale/app/core/pos_component";
import Registries from "@point_of_sale/app/core/registries";
import { usePos } from "@point_of_sale/app/store/pos_hook";

class GiftSelectorPopup extends PosComponent {
    setup() {
        super.setup();
        this.pos = usePos();
        this.state = useState({
            selected: null,
            message: '',
        });
        this.products = this.pos.db.get_product_by_category(0).filter(p => p.is_loyalty_reward);
    }

    selectGift(product) {
        const customer = this.pos.get_order().get_partner();
        const points = customer ? customer.loyalty_points || 0 : 0;
        if (points >= product.points_required) {
            this.state.selected = product;
            this.state.message = `Selected ${product.display_name}`;
            // In thực tế, bạn sẽ gọi RPC để log lại redemption và trừ điểm ở backend
        } else {
            this.state.message = "Not enough points";
        }
    }
}

GiftSelectorPopup.template = 'GiftSelectorPopup';
Registries.Component.add(GiftSelectorPopup);
