# Tasks:
# [ ] Call testing method
# [ ] Call setUp method before calling the testing method
# [ ] Call tearDown method after calling the testing method
# [ ] Method tearDown must be called even if the testing method was failed
# [ ] Run many tests
# [ ] Result report

class TestCase:
	def __init__(self, name):
		self.name = name
    
	def run(self):
		method = getattr(self, self.name)
		method()

class WasRun(TestCase):
	def __init__(self, name):
		self.wasRun = None
		TestCase.__init__(self, name)

	def testMethod(self):
		self.wasRun = 1

class TestCaseTest(TestCase):
	def testRunning(self):
		test = WasRun('testMethod')
		assert(not test.wasRun)
		test.run()
		assert(test.wasRun)

TestCaseTest('testRunning').run()
