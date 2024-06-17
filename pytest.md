pytest : 

to check if exception is raised : 
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10,0)
		

if you write test in class then two auto methods : setup and teardown
these two methods will run before and after each actual class method

class TestCircle:
    
    def setup_method(self,method):
        print(f"Setting up {method}")
    
    def teardown_method(self,method):
        print(f'Tearing down {method}')


in setup method is used to set up any state or resources needed for the test. to initialize resources such as database connections, temporary files, or other stateful dependencies that are required by your tests.
teardown method : is used to clean up any state or resources after each test method runs. e.g., close files, release resources, etc. to ensure any resources initialized in setup_method or during the test are properly cleaned up, preventing resource leaks and ensuring isolation between tests.

next is pytest fixtures






