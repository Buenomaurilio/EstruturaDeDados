'''
defina uma função que recebe dois números e retorna o maior deles
'''

def maximo2(a, b):
    if a > b:
        return a
    return b

#print(maximo2(8, 6))

'''
defina uma função que recebe três números e retorna o maior deles
'''

def maximo3(a, b, c):
    max = maximo2(b, c)
    if a > max:
        return a
    return max

#print(maximo3(19, 3, 11))        

'''
defina uma função que recebe quatro números e retorna o maior deles
'''

def maximo4(a,b,c,d):
    max = maximo3(b, c, d)
    if a > max:
        return a 
    return max

#print(maximo4(12,19,16,11))


'''
defina uma função que recebe cinco números e retorna o maior deles
'''

def maximo5(a,b,c,d,e):
    max = maximo4(b,c,d,e)
    if a > max:
        return a
    return max

#print(maximo5(-11,-2,-1,-4,-5))

import unittest

class TestStringMethods(unittest.TestCase):

    def test_maximo2(self):
        self.assertEqual(maximo2(1,2),2)
        self.assertEqual(maximo2(3,2),3)
        self.assertEqual(maximo2(-3,-2),-2)
        self.assertEqual(maximo2(-10,2),2)

    def test_maximo3(self):
        self.assertEqual(maximo3(-2,1,2),2)
        self.assertEqual(maximo3(3,2,1),3)
        self.assertEqual(maximo3(-4,-3,-2),-2)
        self.assertEqual(maximo3(-10,2,12),12)
    
    def test_maximo4(self):
        self.assertEqual(maximo4(1,2,3,4),4)
        self.assertEqual(maximo4(3,2,1,5),5)
        self.assertEqual(maximo4(-4,-1,-3,-2),-1)
        self.assertEqual(maximo4(-10,-3,-4,2),2)

    def test_maximo5(self):
        self.assertEqual(maximo5(1,2,3,4,5),5)
        self.assertEqual(maximo5(3,2,6,7,8),8)
        self.assertEqual(maximo5(-10,-8,-5,-3,-2),-2)
        self.assertEqual(maximo5(-10,-3,1,-2,2),2)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()