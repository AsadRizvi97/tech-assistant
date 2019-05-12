import pymysql as db


class ITSDB:
    def __init__( self):
        self.conn = db.connect(host="localhost", user="####", passwd="####",
                               db="####", use_unicode=True, charset="utf8")
      
    def __del__(self):
        self.conn.close()

    def listClient(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT Fname, Lname, Username, Email, PhoneNumber, Building, Room, Status, D.Name
                       FROM Client, Department AS D
                       WHERE Department = D.ID
                       ORDER BY Username ASC""")

        return cur

    def listAsset(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT A.AssetNumber, A.AssetType, A.Model, A.Client, A.Status, C.Building, C.Room
                       FROM Asset AS A, Client AS C
                       WHERE A.Client = C.Username
                       ORDER BY A.Client ASC""")

        return cur

    def listTicket(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT Ticket_no, Client, Assigned_tech, Status, T.Name, Asset FROM Ticket, Tech_Group AS T
                       WHERE Tech_group = T.ID
                       ORDER BY Ticket_no DESC""")

        return cur

    def listAppt(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT TicketNo, T.Client, Tech, Appointment.Time, C.Building, C.Room, Notes, T.Asset
                       FROM Appointment, Client AS C, Ticket as T
                       WHERE TicketNo = T.Ticket_no AND C.Username = T.Client
                       ORDER BY Ticket_no DESC""")

        return cur

    def listTech(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT C.Fname, C.Lname, T.Type
                       FROM Technician AS T, Client AS C
                       WHERE T.Username = C.Username
                       ORDER BY T.Username ASC""")

        return cur

    def listDept(self):
        cur = self.conn.cursor()

        cur.execute("SELECT * FROM Department")

        return cur

    def listEmployee(self):
        cur = self.conn.cursor()

        cur.execute("""SELECT C.Fname, C.Lname, E.ManagerName, T.Name
                       FROM ITS_Employee AS E, Client AS C, Tech_Group AS T
                       WHERE E.Username = C.Username AND E.TechGroup = T.ID
                       ORDER BY C.Username ASC""")

        return cur

    def listBldg(self):
        cur = self.conn.cursor()

        cur.execute("SELECT * FROM Building ORDER BY Name ASC")

        return cur

    def updateDept(self, oldName, newName):
        cur = self.conn.cursor()

        params = (newName, oldName)
        cur.execute("UPDATE Department SET Name = '%s' WHERE Name = '%s'" % params)

        self.conn.commit()

    def checkUpdateDept(self, oldName):
        cur = self.conn.cursor()

        cur.execute("SELECT * FROM Department WHERE Name = '%s'" % oldName)

        return cur

    def deleteDept(self, deptName):
        cur = self.conn.cursor()

        params = (deptName,)
        cur.execute("DELETE FROM Department WHERE Name = '%s'" % params)

        self.conn.commit()

    def checkDeleteDept(self, deptName):
        cur = self.conn.cursor()

        params = (deptName,)
        cur.execute("""SELECT * FROM Client WHERE Department IN 
                      (SELECT ID FROM Department WHERE Name = '%s')""" % params)

        return cur
