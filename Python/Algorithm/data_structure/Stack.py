# スタック

class Stack():

    def __init__(self, data=[]):
        self.data = data

    def push(self, x):
        """
        xをpush
        """

        self.data.append(x)

        return self.data

    def pop():
        """
        最後に入れた値をpop
        """

        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            cell = self.data.pop()

            return cell

