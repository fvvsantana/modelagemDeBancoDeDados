import cx_Oracle

# info about the oracle connection
dsn_tns = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
user = 'C9771525'
password = 'C9771525'

# open the oracle server connection
def openConnection():
    global con
    con = cx_Oracle.connect(user, password, dsn_tns)
    global cur
    cur = con.cursor()

# close the oracle server connection
def closeConnection():
    cur.close()
    con.close()