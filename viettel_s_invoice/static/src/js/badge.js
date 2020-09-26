odoo.define('viettel_s_invoice.badge', function (require) {
"use strict";

/**
 * This module contains most of the basic (meaning: non relational) field
 * widgets. Field widgets are supposed to be used in views inheriting from
 * BasicView, so, they can work with the records obtained from a BasicModel.
 */

var AbstractField = require('web.AbstractField');
var registry = require('web.field_registry');
var config = require('web.config');
var core = require('web.core');
var qweb = core.qweb;
var _t = core._t;

var Badge = AbstractField.extend({
    supportedFieldTypes: ['selection'],

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * This widget renders a simple non-editable badge. Color classes can be set
     * using the 'classes' key from the options tag, such as:
     * <field [...] options="{'classes': {'value': 'className', ...}}"/>
     *
     * @private
     * @override
     */
    _render: function () {
        this.classes = this.nodeOptions && this.nodeOptions.classes || {};
        var badgeClass = this.classes[this.value] || 'primary';
        this.$el.addClass('badge badge-auto badge-' + badgeClass).text(this._formatValue(this.value));
    },
});

registry
    .add('badge', Badge);

return {
    Badge: Badge,
};

});
