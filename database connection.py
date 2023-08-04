# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:56:27 2023

@author: januk
"""

import mysql.connector


cnx = mysql.connector.connect(user='root', password='$JanuHari27$',
                              host='localhost',
                              database='pydb',auth_plugin='mysql_native_password')

cursor = cnx.cursor(buffered=True)


query = ("SELECT idjanani FROM janani")
cursor.execute(query)

for (idjanani) in cursor:
  print("{} this is from mysql database".format(idjanani))

"""
cursor.execute("SELECT idjanani FROM janani")
idjanan = cursor.fetchone()[0]
print(idjanan)
try:
    cursor.fetchall()  # fetch (and discard) remaining rows
except mysql.connector.errors.InterfaceError as ie:
    if ie.msg == 'No result set to fetch from.':
        # no problem, we were just at the end of the result set
        pass
    else:
        raise
cursor.execute("SELECT idjanani FROM janani")  # OK now
"""

cursor.close()
cnx.close()

