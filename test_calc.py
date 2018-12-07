import calc

class Tester:

  def test_add(self):
    assert 4 == calc.add(1,3)
    assert 5 == calc.add(6,-1)
  
  def test_sub(self):
    assert 1 == calc.sub(3,2);
  
  def test_shout(self):
    assert "DONUTS!!!" == calc.shout('donuts')