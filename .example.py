class Example():
    def __init__(self, text, number, bool_test):
        self.text = text
        self.bool_test = bool_test
        self.number = number

    def multiply_number(self):
        if self.bool_test == True and self.number > 0:
            return self.number * self.number

        elif self.bool_test == False and self.number > 0:
            return "Boolean parameter is False"

    def return_text(self):
        if self.bool_test == True:
            return self.text

        else:
            return "Boolean parameter is False"

    def return_text_loop(self):
        for i in range(self.number):
            return self.text

test = Example('test', 2, True)
multiply = test.multiply_number()
print_text = test.return_text()
text_return = test.return_text_loop()

print(multiply, print_text, text_return)
