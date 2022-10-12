from fileinput import filename
from importlib.resources import contents
import frappe
import requests
from datetime import date , timedelta
import json
import os
import base64
from frappe.frappeclient import FrappeClient
import re

 



#This api is to add data from registration doc type to employee doctype on status Accept
# this will add employee with user type nominal and farmer id will be appended with N 
#http(s)://hostname/api/method/subhiksha_app.subhiksha_app.edit_nominal.edit_register
#http://localhost:8000/api/method/goumitra_test.goumitra_test.customer_register.register_customer

@frappe.whitelist(allow_guest=True)
def register_customer():
    os.system('clear')
    print("customer creation api")
    user_id = str(frappe.form_dict["docname"])
    docname= (str(frappe.form_dict["docname"]).strip()).split('-',1)[1]
    print(docname)
    custName = "CUST-"
    customer_name = custName+docname
    print("customer name is ", customer_name)
    doc={
		"doctype": "Customer",
		"userid":user_id,
        "customer_name":customer_name,
        "customer_type":"Individual",
        "customer_group": "Individual",
        "territory":"India"
	}
    token = str(frappe.form_dict["token"]).strip()
    header = {"Authorization" : token}
    url=str(frappe.utils.get_url()).strip()+"/api/resource/Customer"
    print("Sending Request ........")
	
    r=requests.post(url,headers=header, data=json.dumps(doc))

    print("Customer creation success")
	
    #msg = "Hello executed from function"
    #frappe.response["message"]= msg
    print("#################################-------------end--------------################")
