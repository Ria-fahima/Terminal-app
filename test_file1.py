from main import check_member
#check the existing member
def fake_input_first(prompt):
    return 'y'
class TestGetresponse:
    def  test_valid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input_first)
        assert check_member() == 'no'

def fake_input_second(prompt):
    return "n"   
def third_input(prompt):
    return "n"     
class Testresponse:
    def  test_valid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input_second)
        monkeypatch.setattr("builtins.input", third_input)
        assert check_member() == 'no'
