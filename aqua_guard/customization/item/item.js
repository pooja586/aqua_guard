// Copyright (c) 2017, Frappe and contributors
// For license information, please see license.txt

cur_frm.fields_dict['taxes'].grid.get_field('item_tax').get_query = function(doc, cdt, cdn) {
	var d = locals[cdt][cdn]
	return{
		filters:[
			['Item', 'sub_item_group', '=', d.sub_item_group]
		]
	}
}