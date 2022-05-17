# This is implementing Python Data Structures: Linked List
# class Node: # Define class for Nodes
class NodeSingly: # Define class for Singly-linked Nodes
    """This is a class for a Singly-Linked Node"""
    def __init__(self, data = None, next = None):
        """Creates a new Singly-Linkable Node.
        
        Args:
            data: May take data as the item property. (default = None)
            next: May take a Node as pointer to the next in the Linked List. (default = None)
        """
        self.data = data
        self.next = next
    

    # Methods for managing the Node
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



class SinglyLinkedList: # Define class for Singly-linked List of Nodes
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
        # The tail is set by the value of cur.
        self.tail = cur

    
    # Methods for managing the Linked List
    def getSize(self): # Integer size of the List
        """Method to return size of the linked list.

        Returns:
            The size of the list, in Int form.
        """
        return self.size


    def addHead(self, data = None): # Appends to the head of the List
        """Method that adds a new Node to the head of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = NodeSingly(data, self.head)
        self.size += 1
        self.head = newNode


    def addTail(self, data = None): # Appends to the tail of the List
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


    def remove(self, data):
        """Method that removes a Node containing the first instance of passed data.
        
        Args:
            data: The data within the Node to be removed from the list.

        Returns:
            True if removal success, False otherwise.
        """
        thisNode = self.head
        prevNode = None
        while thisNode:
            if thisNode.getData() == data:
                if prevNode: # If this isn't the head, stitch the last and next Nodes together
                    prevNode.setNext(thisNode.getNext())
                else: # If this was the head, set next to head and set data and next here to None
                    self.head = thisNode.getNext()
                    # thisNode.setNext(None)
                    # thisNode.setData(None)
                
                if thisNode.next == None: # If this was the tail, set tail to previous
                    self.tail = prevNode

                self.size -= 1 # Decrement the count and set deleted Node value and next to None
                thisNode.setNext(None)
                thisNode.setData(None)

                return True # Data found and removed
            else: # Data not in thisNode, move pointer to the next Node
                prevNode = thisNode
                thisNode = thisNode.getNext()

        return False # Data not found



class NodeDoubly: # Define class for Doubly-linked Nodes
    """This is a class for a Doubly-Linked Node"""
    def __init__(self, data = None, prev = None, next = None):
        """Creates a new Doubly-Linkable Node.
        
        Args:
            data: May take data as the item property. (default = None)
            next: May take a Node as pointer to the next in the Linked List. (default = None)
        """

        self.data = data
        self.prev = prev
        self.next = next


    # Methods for managing the Node
    def getData(self):
        """Method to return Node data.
        
        Returns:
            The data contained in the Node this is called on.
        """
        return self.data
    

    def getPrev(self):
        """Method to return the previous Node.
        
        Returns:
            The previous Node in the list from the one called on.
        """
        return self.prev


    def getNext(self):
        """Method to return the next Node.
        
        Returns:
            The next Node in the list from the one called on.
        """
        return self.next
    

    def getLinks(self):
        """Method to get both the next and previous Nodes in the list.
        
        Returns:
            The previous and next Nodes in the list from the one called on.
        """
        return self.prev, self.next
    

    def setData(self, data = None):
        """Method to set Node data.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        self.data = data
    

    def setPrev(self, prev = None):
        """Method to set the previous Node in the linkage.
        
        Args:
            prev: The previous Node in the linkage to be assigned here. (default = None)
        """
        self.prev = prev


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
        self.prev, self.next = prev, next



class DoublyLinkedList: # Define class for Singly-linked List of Nodes
    """This class implements a Doubly-Linked List"""
    def __init__(self, head = None):
        """Creates a new Doubly-Linked List.
        
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
        # The tail is set by the value of cur. 
        self.tail = 1 #cur


    # Methods for managing the Linked List
    def getSize(self):
        """Method to return size of the linked list.

        Returns:
            The size of the list, in Int form.
        """
        return self.size


    def addHead(self, data = None):
        """Method that adds a new Node to the head of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        oldHead = self.head
        newNode = NodeDoubly(data, prev = None, next = oldHead)
        self.size += 1
        if oldHead == None:
            self.tail = newNode
        else:
            oldHead.setPrev(newNode)

        self.head = newNode


    def addTail(self, data = None):
        """Method that adds a new Node to the tail of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        oldTail = self.tail
        newNode = NodeDoubly(data, prev = oldTail, next = None)
        self.size += 1
        if oldTail == None:
            self.head = newNode
        else:
            oldTail.setNext(newNode)
        
        self.tail = newNode

    
    def remove(self, data):
        """Method that removes a node containing the passed data.
        
        Args:
            data: The data within the Node to be removed from the list.

        Returns:
            True if removal success, False otherwise.
        """
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
        """Method to locate the first occurence of passed data in a List.
        
        Args:
            data: The data that will be looked for in the List.
        
        Returns:
            The data from the Node found by the method, or None if not found.
        """
        thisNode = self.head
        while thisNode:
            if thisNode.getData() == data:
                return thisNode.getData() # Data found and returned
            else:
                thisNode = thisNode.getNext()
        
        return None # Data not found
