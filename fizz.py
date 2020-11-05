from list import List


class Fizz(List):

    def __init__(self):
        super().__init__() # Inheriting parent class
        self.fizz_list = [] # Creating new lists
        self.buzz_list = []
        self.fizzbuzz_list = []

    def fizz(self):
        fizz_number = int(input("What would you like the fizz divide number to be?   "))
        buzz_number = int(input("What would you like the buzz divide number to be?   "))

        # self.list is added to fizz_list, if there isn't a remainder when list_value / fizz_number then value
        # changed to "Fizz"
        for i in self.list:
            if i % fizz_number != 0:
                self.fizz_list.append(i)
            elif i % fizz_number == 0:
                self.fizz_list.append("Fizz")
        # self.list is added to buzz_list, if there isn't a remainder when list_value / buzz_number then value
        # changed to "Fizz"
        for i in self.list:
            if i % buzz_number != 0:
                self.buzz_list.append(i)
            elif i % buzz_number == 0:
                self.buzz_list.append("Buzz")
        # adds fizz_list to fizzbuzz_list
        for i in self.fizz_list:
            self.fizzbuzz_list.append(i)
        # Changes values to "Buzz" on matching index with Buzz_list
        for index, i in enumerate(self.buzz_list):
            if i == "Buzz":
                self.fizzbuzz_list[index] = i
        # Changes values to "Fizzbuzz" where fizz and buzz are in the same index location
        for index, i in enumerate(self.buzz_list):
            if self.buzz_list[index] == "Buzz" and self.fizz_list[index] == "Fizz":
                self.fizzbuzz_list[index] = "Fizzbuzz"

        return print(self.fizzbuzz_list)
