import unittest
from KMAP_Solver import minFunc
class testpoint(unittest.TestCase):
        def test_minFunc(self):
                #for 2 variable kmap
                self.assertEqual(minFunc(2,"(0,1,2) d -"),"w\' + x\'")
                self.assertEqual(minFunc(2,"(0,1,2,3) d -"),"1")
                self.assertEqual(minFunc(2,"(0,3) d -"),"x\'w\' + xw")
                self.assertEqual(minFunc(2,"(0) d (2,3)"),"x\'")
                self.assertEqual(minFunc(2,"(0,1) d -"),"w\'")

                #for 3 variable kmap
                self.assertEqual(minFunc(3,"(0,3,5,6) d -"),"y\'x\'w\' + yxw\' + yx\'w + y\'xw")
                self.assertEqual(minFunc(3,"(2,3,4,5) d -"),"xw\' + x\'w")
                self.assertEqual(minFunc(3,"(2,3,6,7) d -"),"x")
                self.assertEqual(minFunc(3,"(0,1,2,6) d -"),"x\'w\' + y\'x")
                self.assertEqual(minFunc(3,"(0,1,4,5,6) d (2,3,7)"),"1")

                #for 4 variable kmap

                self.assertEqual(minFunc(4,"(2,3,12,13,14,15) d -"),"yx\'w\' + xw")
                self.assertEqual(minFunc(4,"(1,5,7,15) d -"),"zy\'w\' + zyx")
                self.assertEqual(minFunc(4,"(2,4,7,10,12) d (0,6,8)"),"yxw\' + z\'x\' + z\'y\'")
                self.assertEqual(minFunc(4,"(3,7,11,13,14,15) d -"),"zxw + yxw + zy")
                self.assertEqual(minFunc(4,"(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) d -"),"1")

                
                
                
                
                             
if __name__=='__main__':
	unittest.main()
