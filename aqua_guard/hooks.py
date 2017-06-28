# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aqua_guard"
app_title = "Aqua Guard"
app_publisher = "Sagar .S"
app_description = "Distribution and Retailing"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = " "
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aqua_guard/css/aqua_guard.css"
# app_include_js = "/assets/aqua_guard/js/aqua_guard.js"

# include js, css files in header of web template
# web_include_css = "/assets/aqua_guard/css/aqua_guard.css"
# web_include_js = "/assets/aqua_guard/js/aqua_guard.js"

fixtures = ["Custom Field", "Property Setter", "Print Format", "Report"]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

doctype_js={
	"Quotation":["customization/quotation/quotation.js"],
	"Sales Invoice":["customization/sales_invoice/sales_invoice.js"],
	"Item":["customization/item/item.js"]
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aqua_guard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aqua_guard.install.before_install"
# after_install = "aqua_guard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aqua_guard.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

#"validate":["aqua_guard.custom_method.get_taxes","aqua_guard.custom_method.set_taxes"]
# doc_events = {
# 	"Quotation":{
# 		"validate": "aqua_guard.custom_method.set_taxes",
# 		"before_submit" :'aqua_guard.custom_method.get_taxes'

# 	}
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
 # }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aqua_guard.tasks.all"
# 	],
# 	"daily": [
# 		"aqua_guard.tasks.daily"
# 	],
# 	"hourly": [
# 		"aqua_guard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aqua_guard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aqua_guard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aqua_guard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aqua_guard.event.get_events"
# }


