import unittest
from main immport *

class UnitTests( unittest.TestCase ): 
   def test_a1_defined(self):
      self.assertTrue( "a1" in globals(), "No variable named a1 has been defined in your program" )
   def test_a1_correct(self):
      self.assertTrue( a1==3, "The variable a1 has not been set correctly" )
   def test_b2_defined(self):
      self.assertTrue( "b2" in globals(), "No variable named b2 has been defined in your program" )
   def test_b2_correct(self):
      self.assertTrue( b2==(4+5)/2, "The variable b2 has not been set correctly" )
   def test_c3_defined(self):
      self.assertTrue( "c3" in globals(), "No variable named c3 has been defined in your program" )
   def test_c3_correct(self):
      self.assertTrue( c3==3*(9+4), "The variable d4 has not been set correctly" )
   def test_d4_defined(self):
      self.assertTrue( "d4" in globals(), "No variable named d4 has been defined in your program" )
   def test_d4_correct(self):
      self.assertTrue( d4==(7+4)*5, "The variable d4 has not been set correctly" )
      
   
