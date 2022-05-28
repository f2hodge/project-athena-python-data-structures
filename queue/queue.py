# This is implementing Python Data Structures: Queue
class Node: # Define class for Nodes - singly-linked (Superclass)
    """This is a class to form the base of Node classes."""
    # More specifically...
    """This is a class for a Singly-Linked Node

        Implementation of all this functionality is in the Node class.
    """

    def __init__(self, data = None, next = None):
        """Creates a new Singly-Linkable Node.
        
        Args:
            data: May take data as the item property. (default = None)
            next: May take a Node as pointer to the next in the Linked List. (default = None)
        """
        self.data = data
        self.next = next
    
    # Methods for managing the Node that will be commom across classes
    def getData(self):
        """Method to return Node data.
        
        Returns:
            The data contained in the Node this is called on.
        """
        return self.data


    def getNext(self):
        """Method to return the next Node.
        
        Returns:
            The next Node in the list from the one called on.
        """
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



class Queue: # Define class for Single-ended Queue of Nodes
    """This class implements a Queue"""
    def __init__(self, head = None):
        """Creates a new Queue.
        
        Args:
            head: May take a Node as the head property. (default = None)
        """
        self.head = head
        if self.head:
            self.size = 1
            thisNode = self.head
            nextNode = thisNode.getNext()

            while nextNode:
                self.size += 1
                thisNode = nextNode
                nextNode = thisNode.getNext()

            else:
                self.tail = thisNode

        else:
            self.size = 0

    
    # Methods for managing the Queue
    def getSize(self): # Integer size of the List
        """Method to return size of the linked list.

        Returns:
            The size of the list, in Int form.
        """
        return self.size


    def enqueue(self, data = None): # Appends to the tail of the List
        """Method that adds a new Node to the tail of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = Node(data)
        self.size += 1
        if self.getSize() == 1:
            self.head = self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode

    
    def find(self, data): # Find and return a Node if the data is in the List
        """Method to locate the first occurence of passed data in a List.
        
        Args:
            data: The data that will be looked for in the List.
        
        Returns:
            The Node containing the first instance of the data found by the method, or None if not found.
        """
        thisNode = self.head
        while thisNode:
            if thisNode.getData() == data:
                return thisNode # Data found and Node returned
            else:
                thisNode = thisNode.getNext()
        
        return None # Data not found


    def contains(self, data): # Find and return bool indicating presence of data
        """Method to see if passed data is in a List.
        
        Args:
            data: The data that will be looked for in the List.
        
        Returns:
            True if data from the Node found by the method, or False if not found.
        """
        return self.find(data) != None # Returns True if found, False otherwise


    def dequeue(self):
        """Method that removes the first Node in the Queue.
        
        Returns:
            The data contained in the first Node.
        """
        if self.getSize == 0:
            return None
        
        thisData = self.head.getData()

        self.head = self.head.next
        self.size -= 1
        
        return thisData