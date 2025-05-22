odoo.define('customer_loyalty_gift_selector_advanced.GiftSelectorPopup', function (require) {
    const { PosComponent } = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const rpc = require('web.rpc');
    const Registries = require('point_of_sale.Registries');

    class GiftSelectorPopup extends PosComponent {
        async onClick() {
            const partner_id = this.env.pos.get_order().get_client()?.id;
            if (!partner_id) {
                alert('Chưa chọn khách hàng.');
                return;
            }
            const rewards = await rpc.query({
                model: 'loyalty.reward',
                method: 'search_read',
                args: [[], ['name', 'points_cost']],
            });
            const chosen = window.prompt("Nhập tên phần thưởng để đổi: \n" +
                rewards.map(r => `${r.name} (${r.points_cost} điểm)`).join('\n'));
            const reward = rewards.find(r => r.name === chosen);
            if (!reward) return;

            await rpc.query({
                model: 'loyalty.transaction',
                method: 'create',
                args: [{
                    partner_id,
                    reward_id: reward.id,
                    type: 'redeem',
                    points: reward.points_cost,
                }],
            });
            alert(`Đã đổi quà: ${reward.name}`);
        }
    }

    GiftSelectorPopup.template = 'GiftSelectorPopup';

    ProductScreen.addControlButton({
        component: GiftSelectorPopup,
        condition: () => true,
        position: ['before', 'SetCustomer'],
    });

    Registries.Component.add(GiftSelectorPopup);

    return GiftSelectorPopup;
});