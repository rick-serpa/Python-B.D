import unittest

class teste(unittest.TestCase):
    def test_A(self, vl1 =1 , vl2 = 1):
        self.assertEqual(vl1,vl2)

    def test_B(self,vl1, vl2):
        if (vl1 + vl2 == 4):
            retorno =  'Ok'
        else:
            retorno = 'Falha'
        self.assertEqual(retorno,'Ok')

class teste02(unittest.TestCase):
    def test_Teste02A(self,valor = 17):
        self.assertNotEqual(18, valor)
    
    def test_Teste02B(self,valor = True):
        curso =  'Python avançado'
        valor = (curso == 'Python avançado')
        self.assertTrue(valor)
    
    def test_Saldo(self,valor = 0):
        valot = 1
        self.assertEqual(valor,1)