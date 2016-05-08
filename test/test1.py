from nose.tools import assert_equal

from app.program import Program

def test_build_deck():
  program = Program()
  assert_equal(isinstance(program.build_deck("cards.txt"), str), True)

def tearDown(self):
  program = Program()
  print
  print "1."
  print "STR DECK:", program.build_deck("cards.txt")

