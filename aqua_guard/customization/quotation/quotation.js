// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

/*frappe.ui.form.on("Quotation", {
})

frappe.ui.form.on('Quotation Item', {
	item_code: function(frm,cdt,cdn) {
		var item = frappe.get_doc(cdt, cdn);
		console.log(item,"**************")
		get_tax(frm,item.item_code)
	}
})

get_tax = function(frm,item) {
	console.log(item,"&&&&&&&&&&&&")
		frappe.call({
				method: 'aqua_guard.customization.quotation.quotation.get_item',
				args: {
					"item": item
				},
				callback: function(r) {
					if(r.message) {
						console
					}
					
				}
			});
}
*/