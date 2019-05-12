from itsdb import ITSDB

dbobj = ITSDB()


def topLayout():
    print("""
        <h1><a href="?">ITS Technician Assistant</a></h1>
        <table border=1 >
            <tr>
                <th><button onclick="window.location.href='?listClient=1';">Clients</button></th>
                <th><button onclick="window.location.href='?listAsset=1';">Assets</button></th>
                <th><button onclick="window.location.href='?listTicket=1';">Tickets</button></th>
                <th><button onclick="window.location.href='?listAppt=1';">Appointments</button></th>
                <th><button onclick="window.location.href='?listTech=1';">Technicians</button></th>
                <th><button onclick="window.location.href='?listDept=1';">Departments</a></button></th>
                <th><button onclick="window.location.href='?listEmployee=1';">ITS Employees</button></th>
                <th><button onclick="window.location.href='?listBldg=1';">Buildings</button></th>
            </tr>
        </table>
        """)


def listClient():
    cur = dbobj.listClient()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Clients</h3>
    <tr>
        <th>First Name</th><th>Last Name</th><th>Username</th><th>Email Address</th><th>Phone Number</th>
        <th>Building</th><th>Room</th><th>Status</th><th>Department</th>
    </tr>
    """)
    for row in result:
        (fname, lname, uname, email, number, bldg, room, status, dept) = row
        print("""
        <tr>
            <td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
        </tr>
        """ % (fname, lname, uname, email, number, bldg, room, status, dept))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
        </tr>
    </table>
    """)


def listAsset():
    cur = dbobj.listAsset()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Assets</h3>
    <tr>
        <th>Asset Number</th><th>Asset Type</th><th>Model</th><th>Client</th><th>Status</th><th>Building</th>
        <th>Room</th>
    </tr>
    """)
    for row in result:
        (anum, atype, model, client, status, bldg, room) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (anum, atype, model, client, status, bldg, room))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>
    """)


def listTicket():
    cur = dbobj.listTicket()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Tickets</h3>
    <tr>
        <th>Ticket Number</th><th>Client</th><th>Assigned Tech</th><th>Status</th><th>Tech Group</th><th>Asset</th>
    </tr>
    """)
    for row in result:
        (tnum, client, atech, status, tgroup, asset) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (tnum, client, atech, status, tgroup, asset))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>""")


def listAppt():
    cur = dbobj.listAppt()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Appointments</h3>
    <tr>
        <th>Ticket Number</th><th>Client</th><th>Technician</th><th>Time</th><th>Building</th><th>Room</th>
        <th>Notes</th><th>Asset</th>
    </tr>
    """)
    for row in result:
        (tnum, client, tech, time, bldg, room, note, asset) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (tnum, client, tech, time, bldg, room, note, asset))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1 >
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>""")


def listTech():
    cur = dbobj.listTech()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Technicians</h3>
    <tr>
        <th>First Name</th><th>Last Name</th><th>Type</th>
    </tr>
    """)
    for row in result:
        (fname, lname, type) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (fname, lname, type))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>""")


def listDept():
    cur = dbobj.listDept()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Departments</h3>
    <tr><th>Name</th></tr>
    """)
    for row in result:
        (Id, name) = row
        print("<tr><td>%s</td></tr>" % name)
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateDept=1';">Update Existing Record</button></th>
            <th><button onclick="window.location.href='?deleteDept=1';">Delete Existing Record</button></th>
        </tr>
    </table>""")


def listEmployee():
    cur = dbobj.listEmployee()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>ITS Employees</h3>
    <tr>
        <th>First Name</th><th>Last Name</th><th>Manager</th><th>Tech Group</th>
    </tr>
    """)
    for row in result:
        (fname, lname, manager, tgroup) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (fname, lname, manager, tgroup))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>""")


def listBldg():
    cur = dbobj.listBldg()
    result = cur.fetchall()

    topLayout()
    print("""
    <table border=1 class="allTables">
    <h3>Buildings</h3>
    <tr>
        <th>Name</th><th>Address</th><th>Elevator</th><th>Ramp</th>
    </tr>
    """)
    for row in result:
        (name, address, elevator, ramp) = row
        print("""
                <tr>
                    <td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                """ % (name, address, elevator, ramp))
        print()
    print("""
    </table>
    """)
    print("""
    <br>
    <table border=1>
        <tr>
            <th><button onclick="window.location.href='?create=1';">Add New Record</button></th>
            <th><button onclick="window.location.href='?updateAsset=1';">Update Existing Record</button></th>
        </tr>
    </table>""")


def updateDeptName(oldName, newName):
    dbobj.updateDept(oldName, newName)
    topLayout()
    print("""
    <h3>Updated database name from %s to %s</h3>
    <button onclick="window.location.href='?listDept=1';">Back</button>
    """ % (oldName, newName))


def checkUpdateDeptName(oldName, newName):
    cur = dbobj.checkUpdateDept(oldName)
    result = cur.fetchall()
    if len(result) == 0:
        topLayout()
        print("""
        <h3>Department %s does not exist.</h3>
        <button onclick="window.location.href='?updateDept=1';">Back</button>
        """ % oldName)
    else:
        updateDeptName(oldName, newName)



def deleteDeptName(name):
    dbobj.deleteDept(name)
    topLayout()
    print("""
    <h3>Deleted %s from database</h3>
    <button onclick="window.location.href='?listDept=1';">Back</button>
    """ % name)


def checkDeleteDeptName(name):
    cur = dbobj.checkDeleteDept(name)
    clients = cur.fetchall()
    cur = dbobj.checkUpdateDept(name)
    exists = cur.fetchall()
    if len(clients) == 0 and len(exists) != 0:
        deleteDeptName(name)
    elif len(exists) == 0:
        topLayout()
        print("""
                <h3>Department %s does not exist.</h3>
                <button onclick="window.location.href='?deleteDept=1';">Back</button>
                """ % name)
    else:
        topLayout()
        print("""
        <h3>Cannot delete %s since a client exists in this department.</h3>
        <button onclick="window.location.href='?deleteDept=1';">Back</button>
        """ % name)


def showDefaultPage():
    topLayout()
    print("""
    <br>
    <p>Welcome. I am the ITS Help Desk Technician Assistant.<br>
    To create, view, update or delete any information from my database, go ahead and click on one of
    the buttons at the top.</p>
    """)


def showUpdateDeptForm():
    topLayout()
    print("""
    <h3>Update Department</h3>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">

    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="updateDept" value="1">
    <table>
        <tr>
            <td>Old Department Name</td>
            <td><INPUT TYPE="TEXT" NAME="oldName" VALUE=""></td>
        </tr>
        <tr>
            <td>New Department Name</td>
            <td><INPUT TYPE="TEXT" NAME="newName" VALUE=""></td>
        </tr>
        <tr>
            <td><input type="submit" name="updateDept" value="Update!"></td>
        </tr>
    </table>
    </FORM>
    <table>
        <tr>
            <td><button onclick="window.location.href='?listDept=1';">Back</button></td>
        </tr>
    </table>
    """)


def showDeleteDeptForm():
    topLayout()
    print("""
    <h3>Delete Department</h3>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">

    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="deleteDept" value="1">
    <table>
        <tr>
            <td>Department Name</td>
            <td><INPUT TYPE="TEXT" NAME="name" VALUE=""></td>
        </tr>
        <tr>
            <td><input type="submit" name="deleteDept" value="Delete!"></td>
        </tr>
    </table>
    </FORM>
    <table>
        <tr>
            <td><button onclick="window.location.href='?listDept=1';">Back</button></td>
        </tr>
    </table>
    """)

