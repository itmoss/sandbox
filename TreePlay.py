''' 

@Describe :

To print example as like above, implement binary tree follow to these skeletons.

I will use this way that Levelorder-Traverse, because it is easy to verify in a short time and implement also.

Level ordering traverse algorithm : 

For each node, first node visited and then it's child nodes are put in a FIFO queue. 





@How to implement : 

- Search the binary tree algorithm on google. 

- Design how to handle individual nodes. 

- Keep the properties of binary tree e.g. root level, degree of tree, adding child.

- Creates a class for user convenience and flexibility. 



- Degree and Node attributes should be decided when user adds child node to parent.

- Insert data type have to be integer. 



@Result: 

Runtime complexity about this solution - O(n) where n is number of nodes in the binary tree.



@Recommended test case.

- Stability of levelorderTraverse function : 

  Check that function has no problem when user excute it 2 times and more. 

  Verify that this function's tree is same according to user's request. 

  Especially, user's picture of tree have to be same with this response. 

- Parameter check and stability :

  Insert null parameter to class of node.

  Verify that these function have side effect when user input "null" to several functions.

  Data have to be integer when user excute function of "setdata()".

- gracefully exit and return :

  Verify that these statements of "while" will be certainly ended.

  Check that several flags are able to trigger well before quite loop.



'''















#

# Data Structure base follow to this test , and add some methods for user friendly. 

# 

public class Node():

    

# private: 

    _value = 0;

    _left = None;

    _right = None;

    # ROOT of three's depth is 1

    _depth = 1; 



    # constructor of class 

    def __init__(self,leftChild=None,rightChild=None):

        self._value = 0;

        self._left = None;

        self._right = None;

        self.setLeftChild(self,leftChild);

        self.setRightChild(self,rightChild);

    

#public:



    # setting depth, degree. 

    def setDegree(self,degree):

        self._depth = degree;

    

    def getDegree(self):

        return self._depth;

        

    # Data of nodes.     

    def setData(self,data):

        try:

            #cheking integer.

            float(data);

            self._value = data;

        except ValueError:

            self._value = 0;

            return False;

        return True;    

    

    def getData(self):

        return self._value;

        

    def setLeftChild(self,child):

        if None == child:

            return;

        self._left = child;

        child.setDegree(self._depth + 1);

    

    def getLeftChild(self):

        return self._left;



    def setRightChild(self,child):

        if None == child:

            return;

        self._right = child;

        child.setDegree(self._depth + 1);

        

    def getRightChild(self,child):

        return self._right;

#        

#End of Class       

#        







#

# service functions

# prints node. 

_previous_line = 1;

def printTree (node):

    global _previous_line;



    # This is the node of ROOT,

    if 1 == node.getDegree():

        print str(node.getData()),

        return;



    if node.getDegree() == _previous_line:

        print r',' + str(node.getData()),;

    else:

        print r'\n';

        print node.getData(),;



    _previous_line = node.getDegree();







#

# service functions  

# Travers logics and printing.

levelq = [];

def levelorderTraverse(node,fpPrint):

    levelq.append(node);

    while len(levelq) != 0:

        visit_node = levelq.pop(0);

        fpPrint(visit_node);

        

        if None != visit_node.getLeftChild():

            levelq.append(visit_node.getLeftChild());

        

        if None != visit_node.getRightChild():

            levelq.append(visit_node.getRightChild());



#

# sample input 

#

'''

    5

   / \

  3   1

/   / \

9   4   5

   /

  2

'''



root = None;

def init_tree():

    global root;

    root = Node();

    node2 = Node();

    node3 = Node();

    node4 = Node();

    node5 = Node();

    node6 = Node();

    node7 = Node();



    root.setData(5);

    node2.setData(3);

    node3.setData(1);

    node4.setData(9);

    node5.setData(4);

    node6.setData(5);

    node7.setData(2);



    root.setLeftChild(node2);

    root.setRightChild(node3);

    node2.setLeftChild(node4);

    node3.setLeftChild(node5);

    node3.setRightChild(node6);



    node5.setLeftChild(node7);







#     

# main process 

#



print "===========================================";

print "= Printing nodes with levelordered traverse";

print "===========================================";



# Insert nodes as like sample input. 

init_tree();

levelorder_traverse(root,printTree);



print "===========================================";

print "= Bye";

print "===========================================";

        

        

        

        

        

        

        

        

        

        

        

        


































