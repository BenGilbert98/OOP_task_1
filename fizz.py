from list import List


class Fizz(List):

    def __init__(self):
        super().__init__()
        self.fizz_list = []
        self.buzz_list = []
        self.fizzbuzz_list = []

    def fizz(self):
        fizz_number = int(input("What would you like the fizz divide number to be?   "))
        buzz_number = int(input("What would you like the buzz divide number to be?   "))
        for i in self.list:
            if i % fizz_number != 0:
                self.fizz_list.append(i)
            elif i % fizz_number == 0:
                self.fizz_list.append("Fizz")

        for i in self.list:
            if i % buzz_number != 0:
                self.buzz_list.append(i)
            elif i % buzz_number == 0:
                self.buzz_list.append("Buzz")

        for i in self.fizz_list:
            self.fizzbuzz_list.append(i)
        for index, i in enumerate(self.buzz_list):
            if i == "Buzz":
                self.fizzbuzz_list[index] = i
        for index, i in enumerate(self.buzz_list):
            if self.buzz_list[index] == "Buzz" and self.fizz_list[index] == "Fizz":
                self.fizzbuzz_list[index] = "Fizzbuzz"

        return print(self.fizzbuzz_list)