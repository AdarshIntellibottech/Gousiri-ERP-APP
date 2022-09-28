import frappe
import os
from frappe.frappeclient import FrappeClient
 



#This api is to add data from registration doc type to employee doctype on status Accept
# this will add employee with user type nominal and farmer id will be appended with N 
#http(s)://hostname/api/method/subhiksha_app.subhiksha_app.edit_nominal.edit_register
#http://localhost:8000/api/method/goumitra_test.goumitra_test.hello_world.say_hello

@frappe.whitelist(allow_guest=True)
def say_hello():
    os.system('clear')
    print("hi")
    msg = "Hello executed from function"
    frappe.response["message"]= msg
    print("#################################-----------------################")
