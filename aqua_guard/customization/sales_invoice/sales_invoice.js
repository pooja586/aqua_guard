// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

/*frappe.ui.form.on('Sales Invoice', {
	validate : function(frm) {
		if (frm.doc.total_taxes_and_charges) {
			get_tax(frm)
			console.log(frm.doc.total_taxes_and_charges,"frmmmmmmmmmmmmmmm)))))))))))")
		}
		console.log("inside validate.................")
		// get_tax(frm)
	}
	due_date:function(frm){
		console.log("get tax_________________")
		frappe.call({
			method: "aqua_guard.customization.salesinvoice.get_tax_in_words",
			args: {
				"tax_amount": frm.doc.company
			},	
			callback: function(r, rt) {
				if(r.message){
					
				}	
			}
		});
	}
})



get_tax = function(frm){
	console.log(frm.doc.total_taxes_and_charges,"frmmmmmmmmmmmmmmm)))))))))))")
	console.log("inside tax_________________")
		frappe.call({
			method: "aqua_guard.customization.salesinvoice.get_tax_in_words",
			args: {
				tax_amount: frm.doc.total_taxes_and_charges,
				currency: frm.doc.currency
			},	
			callback: function(r, rt) {
				if(r.message){
					console.log(r.message,"_______________________________")
					frm.set_value("tax_in_words", r.message);
					frm.refresh_fields();
				}	
			}
		});
}
*/
frappe.ui.form.on('Sales Invoice Item', {
	discount_percentage: function(frm,cdt,cdn) {
		var row = locals[cdt][cdn];
		disc_value = (row.price_list_rate - ((row.price_list_rate * row.discount_percentage)/100));
		frappe.model.set_value(cdt, cdn, "discount_value", disc_value);
	}
})