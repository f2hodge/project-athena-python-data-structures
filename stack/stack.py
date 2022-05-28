# This is implementing Python Data Structures: Stack
class Node: # Define class for Nodes - stacked (Superclass)
    """This is a class to form the base of Node classes."""
    # More specifically...
    """This is a class for a Single-direction Node

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



class Stack: # Define class for a Stack of Nodes
    """This class implements a Stack"""
    def __init__(self, top = None):
        """Creates a new Stack.
        
        Args:
            top: May take a Node as the top property. (default = None)
        """
        self.top = top
        if self.top:
            self.size = 1
            thisNode = self.top
            nextNode = thisNode.getNext()

            while nextNode:
                self.size += 1
                thisNode = nextNode
                nextNode = thisNode.getNext()

            else:
                self.bottom = thisNode

        else:
            self.size = 0
            self.bottom = None

    
    # Methods for managing the Stack
    def getSize(self): # Integer size of the Stack
        """Method to return size of the Stack.

        Returns:
            The size of the Stack, in Int form.
        """
        return self.size


    def addTop(self, data = None): # Appends to the top of the Stack
        """Method that adds a new Node to the top of the Stack.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = Node(data, self.top)
        self.size += 1
        if self.bottom:
            pass
        else:
            self.bottom = newNode

        self.top = newNode

    
    def find(self, data): # Find and return a Node if the data is in the Stack
        """Method to locate the first occurence of passed data in a Stack.
        
        Args:
            data: The data that will be looked for in the Stack.
        
        Returns:
            The Node containing the first instance of the data found by the method, or None if not found.
        """
        thisNode = self.top
        while thisNode:
            if thisNode.getData() == data:
                return thisNode # Data found and Node returned
            else:
                thisNode = thisNode.getNext()
        
        return None # Data not found


    def contains(self, data): # Find and return bool indicating presence of data
        """Method to see if passed data is in a Stack.
        
        Args:
            data: The data that will be looked for in the Stack.
        
        Returns:
            True if data from the Node found by the method, or False if not found.
        """
        return self.find(data) != None # Returns True if found, False otherwise


    def popTop(self):
        """Method that removes the top Node in the Stack.
        
        Returns:
            The data contained in the first Node.
        """
        if self.getSize == 0:
            return None
        
        thisData = self.top.getData()

        self.top = self.top.next
        self.size -= 1
        
        return thisData