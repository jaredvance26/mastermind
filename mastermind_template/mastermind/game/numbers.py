import random
class Numbers:
    """ Create and generate random code. Takes in a guess and compares. """

    def __init__(self):
        self.code = random.randint(1000, 9999)
        # print(self.code)

    def get_hint(self, guess):
        pass

    def compare(self, guess):
        guess = str(guess)
        self.code = str(self.code)
        output = []

        for index, number in enumerate(guess):
            if number == self.code[index]:
                output.append('x')
            elif number in self.code:
                output.append('o')
            else:
                output.append('*')
        return output
            
                
    # def _prepare(self):
    #     for i in range(4):
    #         code = random.randint(1, 9)
    #         self.code.append(code)

number = Numbers()
guess = '1234'

number.compare(guess)