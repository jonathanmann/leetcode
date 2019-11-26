class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.q.reverse()
        self.q.pop()
        self.q.reverse()

    def peek(self):
        """
        :rtype: int
        """
        self.q.reverse()
        p = self.q.pop()
        self.push(p)
        self.q.reverse()
        return p

    def empty(self):
        """
        :rtype: bool
        """
        if self.q == []:
            return True
        return False

z = Queue()
