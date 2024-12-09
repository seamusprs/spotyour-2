import spotyour2.stats.testreaddata
import spotyour2.stats.testshowstats
import spotyour2.quiz.testplaygame
import spotyour2.quiz.testquizbuilder
import unittest

# run this outside of the spotyour2 directory!

tests = unittest.TestLoader().discover(start_dir="spotyour2", pattern="test*.py")

# print("Tests: ", tests)

if __name__ == "__main__":
   unittest.TextTestRunner(verbosity=2).run(tests)







