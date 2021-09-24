from stack import Stack

class History:
    def __init__(self):
        self.undos = Stack()
        self.redos = Stack()
        self.max_size = 10

    def add(self, text):
        self.undos.push(text)

    def undo(self):
        if (self.undos.is_empty()):
            return print('Nothing to undo')
        
        element = self.undos.pop()
        self.redos.push(element)
    
    def redo(self):
        if (self.redos.is_empty()):
            print('Nothing to redo')

        element = self.redos.pop()
        self.undos.push(element)

    def get_text(self):
        return self.undos.top()
