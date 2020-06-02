class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == None:
            self.value = value
        if value < self.value:
            
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
           
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

   
    def in_order_print(self, node):
        ordered = []

        ordered.append(self)

        while len(ordered) > 0:
            current = ordered.pop()
            if current.right:
                ordered.append(current.right)
            if current.left:
                ordered.append(current.left)

            (current.value)