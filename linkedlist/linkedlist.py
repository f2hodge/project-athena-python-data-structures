# This is implementing Python Data Structures: Linked List
class NodeSingly:
    """This is a class for a Singly-Linked Node"""
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    

    # Methods for managing the Node
    def getData(self):
        """Method to return Node data."""
        return self.data


    def getNext(self):
        """Method to return the next Node."""
        return self.next


    def setData(self, data = None):
        """Method to set Node data.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        self.data = data


    def setNext(self, next = None):
        """Method to set the next Node in the linkage.
        
        Args:
            next: The next Node in the linkage to be assigned here. (default = None)
        """
        self.next = next



class SinglyLinkedList:
    """This class implements a Singly Linked List"""
    def __init__(self, head = None):
        """Creates a new Singly-Linked List.
        
        Args:
            head: May take a Node as the head property. (default = None)
        """
        self.head = head
        cur = self.head
        self.size = 0
        # If there's a head, size is 1. Add to this if there is a pointer.
        if self.head != None:
            self.size = 1
            while cur.next != None:
                self.size += 1
                cur = cur.getNext()
    

    def getSize(self):
        """Method to return size of the linked list."""
        return self.size


    def addHead(self, data = None):
        """Method that adds a new Node to the head of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = NodeSingly(data, self.head)
        self.size += 1
        self.head = newNode


    def addTail(self, data = None):
        """Method that adds a new Node to the tail of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = NodeSingly(data)
        self.size += 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    
    def remove(self, data = None):
        thisNode = self.head
        prevNode = None
        while thisNode:
            if thisNode.getData() == data:
                if prevNode:
                    prevNode.setNext(thisNode.getNext())
                else:
                    self.head = thisNode

                self.size -= 1

                return True # Data found and removed
            else:
                prevNode = thisNode
                thisNode = thisNode.getNext()

        return False # Data not found


    def find(self, data):
        thisNode = self.head
        while thisNode:
            if thisNode.getData() == data:
                return thisNode.getData() # Data found and returned
            else:
                thisNode = thisNode.getNext()
        
        return None # Data not found



class NodeDoubly:
    """This is a class for a Doubly-Linked Node"""
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

    # Methods for managing the Node
    def getPrev(self):
        """Method to return the previous Node."""
        return self.prev

    def getData(self):
        """Method to return Node data."""
        return self.data
    
    def getNext(self):
        """Method to return the next Node."""
        return self.next
    
    def getLinks(self):
        """Method to return both the next and previous links."""
        return self.prev, self.next
    
    def setPrev(self, prev = None):
        """Method to set the previous Node in the linkage.
        
        Args:
            prev: The previous Node in the linkage to be assigned here. (default = None)
        """
        self.prev = prev

    def setData(self, data = None):
        """Method to set Node data.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        self.data = data
    
    def setNext(self, next = None):
        """Method to set the next Node in the linkage.
        
        Args:
            next: The next Node in the linkage to be assigned here. (default = None)
        """
        self.next = next

    def setLinks(self, prev = None, next = None):
        """Method to set both the previous and next links.
        
        Args:
            prev: The previous Node in the linkage to be assigned here. (default = None)
            next: The next Node in the linkage to be assigned here. (default = None)
        """
        return self.prev, self.next