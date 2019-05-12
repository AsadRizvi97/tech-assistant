#!/usr/bin/python
# -*- coding: utf-8 -*-
# "she-bang" line is a directive to the web server: where to find python
#
# filename: assistant.py
# assistant = ITS Technician Assistant

import cgi
import cgitb; cgitb.enable()
import interface


################################################################################
def doHTMLHead():

    print("""
    <html>
    <head>
    <style>
    body { margin: auto; width: 50%; padding: 10px;}
    
    .allTables {font-family: "Trebuchet MS", Arial, Helvetica, sans-serif; border: 1px solid #ddd; border-collapse: 
    collapse; width:100%; }
    
    .allTables td, #allTables th { border: 1px solid #ddd; padding: 8px;
    }
    
    .allTables tr:nth-child(even){background-color: #f2f2f2;}
    
    .allTables tr:hover {background-color: #ddd;}
    
    .allTables th {padding-top: 12px; padding-bottom: 12px; text-align: left; background-color: #4CAF50; color: white;}
    
    </style>
    <title>ITS Technician Assistant</title>
    </head>
    <body>
    """)


################################################################################
def doHTMLTail():
    print("""
    <p>
    <hr>
    </body>
    </html>
    """)


################################################################################
if __name__ == "__main__":
    print("Content-Type: text/html; charset=utf-8")
    print("Cache-Control: no-cache, must-revalidate") # HTTP/1.1 
    print("Expires: Sat, 26 Jul 1997 05:00:00 GMT") # Date in the past 
    print()

    form = cgi.FieldStorage()
    
    doHTMLHead()

    #print("<br><br>")
    #print("Debugging mode with 'print form':<br>")
    #print(form)
    #print("<br><br>")

    if "listClient" in form:
        interface.listClient()
    elif "listAsset" in form:
        interface.listAsset()
    elif "listTicket" in form:
        interface.listTicket()
    elif "listAppt" in form:
        interface.listAppt()
    elif "listTech" in form:
        interface.listTech()
    elif "listDept" in form:
        interface.listDept()
    elif "listEmployee" in form:
        interface.listEmployee()
    elif "listBldg" in form:
        interface.listBldg()
    elif "updateDept" in form and "oldName" in form and "newName" in form:
        oldName = form["oldName"].value
        newName = form["newName"].value
        interface.checkUpdateDeptName(oldName, newName)
    elif "updateDept" in form:
        interface.showUpdateDeptForm()
    elif "deleteDept" in form and "name" in form:
        name = form["name"].value
        interface.checkDeleteDeptName(name)
    elif "deleteDept" in form:
        interface.showDeleteDeptForm()
    else:
        interface.showDefaultPage()
    doHTMLTail()    
