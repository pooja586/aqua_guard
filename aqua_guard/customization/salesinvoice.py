# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

@frappe.whitelist()
def set_gst_tax(item_code):
	query ="""
			select 
				tax_type, tax_rate, parent 
			from 
				`tabItem Tax` 
			where 
				parent ='{}' 
			and 
				parenttype='Item'""".format(item_code)
	result = frappe.db.sql(query,as_dict=1)
	return result