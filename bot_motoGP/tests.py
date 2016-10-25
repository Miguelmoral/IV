# -*- coding: utf-8 -*-
import unittest
import sqlite3 as lite
import sys

class Test(unittest.TestCase):
    def test_motogp(self):
        con = lite.connect('gp.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO CARRERAS VALUES('AAA', 'Circuito Aragón')")
            lid = cur.lastrowid #Devuelve el id de la uĺtima fila
            cur.execute("DELETE FROM CARRERAS WHERE CODIGO = 'AAA'")
            self.assertEqual(lid, 19)


if __name__ == '__main__':
    unittest.main()
