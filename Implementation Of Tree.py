#from QueueLinkedList import Queue
import QueueLinkedList1 as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBT=TreeNode("Drink")
leftChild=TreeNode("Hot")
tea=TreeNode("Tea")
coffee=TreeNode("Coffee")
leftChild.leftChild=tea
leftChild.leftChild=coffee
rightChild=TreeNode("Cold")
newBT.leftChild=leftChild
newBT.rightChild=rightChild

#Pre Order Traversal

def PreOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOrderTraversal(rootNode.leftChild)
    PreOrderTraversal(rootNode.rightChild)
#PreOrderTraversal(newBT)

#Inorder Traversal
 
def InorderTraversal(rootNode):
    if not rootNode:
        return
    InorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InorderTraversal(rootNode.rightChild)
#InorderTraversal(newBT)

#Post Order traversal

def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
#PostOrderTraversal(newBT)

#Level Order traversal

def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:    
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
#LevelOrderTraversal(newBT)

#Searching for a node in binary tree

def SearchBT(rootNode,nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==nodeValue:
                return"success"

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild) 
    return "Not Found"
#print(SearchBT(newBT,"Tea")) 

#Insert a Node In binary Tree

def InsertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return"Successfully Inserted"

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return"Successfully Inserted"
#newNode=TreeNode("Cola")
#print(InsertNodeBT(newBT,newNode))
#LevelOrderTraversal(newBT)                

#Delete a Node From Binary Tree

def GetDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode=root.value
        return deepestNode
#deepestNode=GetDeepestNode(newBT)
#print(deepestNode.data) 

#Delete DeepestNode 

def DeleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
#newNode=GetDeepestNode(newBT)
#DeleteDeepestNode(newBT,newNode)
#LevelOrderTraversal(newBT)

#Delete Node

def deleteNodeBT(rootNode,Node):
    if not rootNode:
        return"The BT does not exist"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==Node:
                dNode=GetDeepestNode(rootNode)
                root.value.data=dNode.data
                DeleteDeepestNode(rootNode,dNode)
                return"The Node is successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)    
        return "Failed To delete"
#deleteNodeBT(newBT,"Cold")
#LevelOrderTraversal(newBT) 

#Delete Entire Node

def deleteBT(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "The BT has been successfully deleted"
deleteBT(newBT)     
LevelOrderTraversal(newBT)       




                   




