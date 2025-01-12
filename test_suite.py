import unittest

# Import your test modules
import test_initialization
import test_overloading
import test_properties_checking
import test_textual_representation

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the suite
suite.addTests(loader.loadTestsFromModule(test_initialization))
suite.addTests(loader.loadTestsFromModule(test_overloading))
suite.addTests(loader.loadTestsFromModule(test_properties_checking))
suite.addTests(loader.loadTestsFromModule(test_textual_representation))

# Initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
