odoo.define('web.ListGroupExpand', function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({
        init: function (parent, state, params) {
            this._super.apply(this, arguments);
            this.isOpen = false;
            this.groupExpandView = state.getContext().groupExpandView;
        },
        _renderView: function () {
            var self = this;
            var res = this._super();
            if (this.isOpen == false && this.groupExpandView == true){
                _.each(self.state.data, function(group) {
                    if(group && group.isOpen == false){
                        self.trigger_up('toggle_group', {group: group});
                        self.isOpen = true;
                    }
                });
            }
            return res
        },
    })
})