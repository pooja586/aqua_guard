from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.utils import flt, cint, add_days, cstr
import json

@frappe.whitelist()
def get_item(item):
	item_doc = frappe.get_doc("Item",item)
	for d in item_doc.taxes:
		print "\n\n\n---------------",d.tax_type
		tax_rate = d.tax_type
		return tax_rate

	# 	row = frappe.new_doc("Sales Taxes and Charges")
	# 	row.append(d.tax_type)
	# 