# -*- coding: utf-8 -*-
import unittest
import sqlite3 as lite
import sys
import modules
import types
import psycopg2

anio = unicode('2015', 'utf-8')
pais = unicode('ARA', 'utf-8')
sesion = unicode('Q2', 'utf-8')

class Test(unittest.TestCase):
    def test_motogp(self):
        #con = psycopg2.connect(database='motogpbot',user='miguel',password='miguel',host='localhost')
        con_bd = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        with con:
            cur = con.cursor()
            valor2 = 'Circuito Aragón'
            valor1 = 'AAA'
            valor = ('ARA', )
            cur.execute("SELECT id FROM datos WHERE id=%s", valor)
            #cur.execute("DELETE FROM datos WHERE id=%s" , valor1)
            self.assertEqual(cur.fetchone()[0], 'ARA       ')


    def test_errores(self):
        modules.comprobacion_errores(anio, pais)

    def test_url(self):
        modules.get_url(anio,pais,sesion)


if __name__ == '__main__':
    unittest.main()
