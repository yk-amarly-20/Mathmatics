# Queue

class Queue():

    def __init__(self, data=[]):
        self.data = data

    def enqueue(self, x):
        """
        enqueue
        """
        self.data.append(x)

        return self.data

    def dequeue(self):
        """
        dequeue
        """

        if len(self.data) == 0:
            return "Queue is Empty"

        else:
            del self.data[0]

            return self.data
