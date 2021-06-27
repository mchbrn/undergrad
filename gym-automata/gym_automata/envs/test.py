class Container:
    def __init__(self, size):
        self.size = size

    def storeItem(self, item):
        self.storage = []
        self.storage.append(item)

class Item:
    def __init__(self, name):
        self.name = name

box = Container(10)
orange = Item("Orange")

box.storeItem(orange)

print("Orange object hash is    " + str(orange))
print("Item stored box hash is " + str(box.storage))
