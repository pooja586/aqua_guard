 Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document
@frappe.whitelist()
def get_tax_in_words(tax_amount):
	print "inside tax_____________________________________________________\n\n\n\n\n\n"
	