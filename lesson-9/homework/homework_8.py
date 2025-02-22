class Secret():
    def __init__(self):
        self.a = "This is private"

    def _hidden_message(self):
        print(self.a)

x= Secret()
x._hidden_message()
