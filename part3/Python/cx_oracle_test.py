import cx_Oracle

dsn_tns = cx_Oracle.makedsn('grad.icmc.usp.br', 15215, 'orcl')
user = #seu usuario no Oracle
password = #sua senha no Oracle
con = cx_Oracle.connect(user, password, dsn_tns)
cur = con.cursor()

#inserir operações de banco de dados aqui

cur.close()
con.close()
