# -*- coding: utf-8 -*-
import unittest
import sqlite3 as lite
import sys
import modules
import types

anio = unicode('2015', 'utf-8')
pais = unicode('ARA', 'utf-8')
sesion = unicode('Q2', 'utf-8')

class Test(unittest.TestCase):
    def test_motogp(self):
        con = lite.connect('gp.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO CARRERAS VALUES('AAA', 'Circuito Aragón')")
            lid = cur.lastrowid #Devuelve el id de la uĺtima fila
            cur.execute("DELETE FROM CARRERAS WHERE CODIGO = 'AAA'")
            self.assertEqual(lid, 19)

    def test_errores(self):
        modules.comprobacion_errores(anio, pais)

    def test_url(self):
        modules.get_url(anio,pais,sesion)


if __name__ == '__main__':
    unittest.main()
