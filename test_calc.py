from calc import *

class Tester:

  def test_add(self):
    assert 4 == add(1,3)
    assert 5 == add(6,-1)
  
  def test_sub(self):
    assert 1 == sub(3,2);
  
  def test_shout(self):
    assert "DONUTS!!!" == shout('donuts')