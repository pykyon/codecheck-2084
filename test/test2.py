from nose.tools import assert_equal

from app.program import Program

def test_gacha():
  program = Program()
  assert_equal(isinstance(program.gacha(1), bool), True)

def tearDown(self):
  program = Program()

  user_count = 0
  total_rare_count = 0
  for user_id in range(1,1000):
    rare_count = 0
    for count in range(1,100):
      if program.gacha(user_id):
        rare_count += 1

    total_rare_count += rare_count
    if rare_count > 0:
      user_count += 1

  print "2."
  print "RARE ITEM RATE: %.4f%%" % (float(total_rare_count) / 1000)
  print "LUCKY MAN RATE: %.4f%%" % (float(user_count) / 10)
  print
