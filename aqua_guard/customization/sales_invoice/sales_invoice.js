// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on('Sales Invoice Item', {
	discount_percentage: function(frm,cdt,cdn) {
		var row = locals[cdt][cdn];
		disc_value = (row.price_list_rate - ((row.price_list_rate * row.discount_percentage)/100));
		frappe.model.set_value(cdt, cdn, "discount_value", disc_value);
	}
})