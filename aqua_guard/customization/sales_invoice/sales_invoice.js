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

frappe.ui.form.on("Sales Invoice Item", {
	item_code: function(doc,cdt,cdn) {
		frappe.call({
			method: "gst_customization.customization.sales_invoice.sales_invoice.set_different_gst",
			args: {"item_code" : "xyz"},
			callback: function(r) {
				console.log(r.message)
			}
		})
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
	},
	item_code: function(frm,cdt,cdn) {
		var item = locals[cdt][cdn];
		default_warehouse = frappe.defaults.get_default("default_warehouse")
		comapny_abbr = default_warehouse.split("-")[1]
		var customer_gstin = frm.doc.customer_gstin;
		var company_gstin = frm.doc.company_gstin;
		if (customer_gstin && company_gstin) {
			if (item.item_code) {
				frappe.call({
					method:"aqua_guard.customization.salesinvoice.set_gst_tax",
					args: {item_code: item.item_code},
					callback: function(r){
						if (r.message){
							$.each(r.message, function(i,v){
								console.log(v['tax_type'])
								if (customer_gstin.substring(0, 2) == company_gstin.substring(0, 2)) {
									if (v['tax_type'] == "C-CGST - " + comapny_abbr.trim()) {
										item.cgst = v['tax_rate']
									}
									else if (v['tax_type'] == "C-SGST - " + comapny_abbr.trim()) {
										item.sgst = v['tax_rate']
									}

								} else if(customer_gstin.substring(0, 2) != company_gstin.substring(0, 2)){
									if (v['tax_type'] == "C-IGST - " + comapny_abbr.trim()) {
										item.igst = v['tax_rate']
									}
									
								}
							})
						}
					}
					})
			}
		} else {
			frappe.msgprint(__("Please Specify Customer GSTIN and Company GSTIN"))
		}

	}
})