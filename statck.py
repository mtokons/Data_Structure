

class has:

    def __init__(self):
        self.st = []


    def add(self, a):

        if a not in self.st:
            self.st.append(a)
            return True
        else:
            return False

    def empty(self):
        if not self.st:
            return True
        else:
            return False


    def fulllist(self):
        return self.st[:]

    def peek(self):
        return self.st[-1]

    def size(self):
        return len(self.st)

    def remove(self):
        if len(self.st) <= 0:
            return ("No element in the Stack")
        else:
            return self.st.pop()


ast = has()
ast.add(10)
ast.add(1)
ast.add(110)
ast.add(5)

print("Stack Last value is : ", ast.peek())
print("List is empty: ", ast.empty())
print("List size: ", ast.size())
print("Full Stack is : ", ast.fulllist())
print("Stack Remove option : ", ast.remove())
print("List size after pop: ", ast.fulllist())


