# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from setuptools import setup, find_packages
from pip.req import parse_requirements
import ast,json
from frappe.utils import money_in_words



def set_taxes(doc,method):
	for tax_row in doc.taxes:		
		tax_key = tax_row.account_head
		print "\n\n___________________tax_key",tax_key		
		for row in doc.items:			
			item_tax = row.item_tax_rate
			print "\n\n___________________item_tax",item_tax				
			dic = ast.literal_eval(item_tax)
			print "\n\n___________________dic",dic		
			if tax_key in dic:
				val = dic[tax_key]
				print "\n\n___________________val",val				
				row.tax = val

def get_taxes(doc,method):
	dic = {}
	account_head_list = set()

	for item in doc.items:
		account_head = json.loads(item.get('item_tax_rate'))
		qty = item.get('qty')
		rate = item.get('rate')
		tax_head = account_head.keys()
		tax_value = account_head.values()
	
		f = float(tax_value[0])
			
		total_amount = ((f * qty * rate)/100)
		if (str(tax_head[0]) in account_head_list):
			dic[str(tax_head[0])] =dic[str(tax_head[0])] + total_amount

		else:
			dic[str(tax_head[0])] = total_amount
			account_head_list.add(tax_head[0])
	print "\n\n_______________________",account_head_list		
	print "\n\n\n\n\n_______________________",dic

	# set_tax(dic)
	set_tax(doc, dic)

def set_tax(doc, dic):
	print "\n\n------------------------",dic
	if dic:
		for i, v in dic.iteritems():
			tax = doc.append("taxes",{})
			tax.charge_type = "On Net Total"
			tax.account_head  = i
			tax.description = "item"
			tax.rate = 0
			tax.tax_amount = v

@frappe.whitelist()
def get_tax_in_words(doc,method):
	# print "inside tax_____________________________________________________\n\n\n\n\n\n", tax_amount
	tax_value = money_in_words(doc.total_taxes_and_charges)
	print "\n\n\n_______________________________________",tax_value
	doc.tax_in_words = tax_value
	