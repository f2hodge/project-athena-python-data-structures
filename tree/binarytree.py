# This is implementing Python Data Structures: Binary Tree
class Node: # Define class for Nodes - Parent or Child
    """This is a class to form the base of Node classes."""
    # More specifically...
    """This is a class for a Binary Tree Node

    Description:
        Implementation of functional Edges and stored Data is here.
        This Node format will work for Root, Internal, or Leaf Nodes.
        Degree: 2 (left and right)
        Height: unbound (unlimited)
    """

    def __init__(self, data = None, parent = None, left = None, right = None):
        """Creates a new Parent or Child Node.
        
        Args:
            data: May take data as the item property. (default = None)
            parent: May take a Node as pointer to the Parent in the Tree. (default = None)
            left: May take a Node as pointer to the Left Child in the Tree. (default = None)
            right: May take a Node as pointer to the Right Child in the Tree. (default = None)
        """
        self.data = data
        self.parent = parent
        self.leftChild = left
        self.rightChild = right


    # Methods for managing the Node that will be commom across classes
    def getData(self):
        """Method to return Node data.
        
        Returns:
            The data contained in the Node this is called on.
        """
        return self.data
    

    def getParent(self):
        """Method to return Parent Node
        
        Returns:
            The Parent Node in the Tree from the one called on.
        """
        return self.parent


    def getLeft(self):
        """Method to return the Left Child Node.
        
        Returns:
            The Left Child Node in the tree from the one called on.
        """
        return self.left


    def getRight(self):
        """Method to return the Right Child Node.
        
        Returns:
            The Right Child Node in the tree from the one called on.
        """
        return self.right


    def setData(self, data = None):
        """Method to set Node data.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        self.data = data


    def setParent(self, parent = None):
        """Method to set the Parent Node in the Tree."""


    def setLeft(self, left = None):
        """Method to set the Left Child Node in the Tree.
        
        Args:
            left: The Left Child Node in the linkage to be assigned here. (default = None)
        """
        self.left = left


    def setReft(self, right = None):
        """Method to set the Right child Node in the linkage.
        
        Args:
            right: The Right Child Node in the linkage to be assigned here. (default = None)
        """
        self.left = right


class BinaryTree: # Define class for a Binary Tree of Nodes
    """This class implements a Binary Tree"""
    def __init__(self, root = None):
        """This is a class for a Binary Tree

        Description:
            Implementation of functional Edge rules are here.
            This Tree format will work for Binary Search format.
            Rule: Lower value Children go to the left.
            Degree: 2 (left and right)
            Height: unbound (unlimited)
        """
        self.root = root
        if self.root:
            self.size = 1
            thisNode = self.root
            nextNode = thisNode.getNext()

            while nextNode:
                self.size += 1
                thisNode = nextNode
                nextNode = thisNode.getNext()

            else:
                self.tail = thisNode

        else:
            self.size = 0

    
    # Methods for managing the Binary Tree
    def getSize(self): # Integer size of the Tree
        """Method to return size of the Tree.

        Returns:
            The size of the Tree, in Int form.
        """
        return self.size
    

    def getHeight(self): # Integer Height of the Tree
        """Method to return height of the Tree.

        Returns:
            The height of the Tree, in Int form.
        """
        return self.height



    def addNode(self, data = None): # Appends to the head of the List
        """Method that adds a new Node to the head of the list.
        
        Args:
            data: Any information we want to insert. (default = None)
        """
        newNode = Node(data)
        self.size += 1
        thisNode = self.root
        
        if self.tail:
            pass
        else:
            self.tail = newNode

        self.head = newNode


    def addTail(self, data = None): # Appends to the tail of the List
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