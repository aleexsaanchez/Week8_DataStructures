class DoctorNode:
    def __init__(self,name):
        self.name = name #Dr's Name
        self.left = None 
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None #Root level doctor
    
    def insert(self, parentName, childName, side): #adds a new doctor under root doctor
        def insertRecursive(node): #function created to search the tree recursively to find a parent
            if node is None:
                return False
            if node.name == parentName:
                if side == "left" and node.left is None:
                    node.left = DoctorNode(childName)
                    return True
                if side == "right" and node.right is None:
                    node.right = DoctorNode(childName)
                    return True
                else:
                    print(f"Error: {side} side is already occupied for Doctor {parentName}.")
                    return False
                
            return insertRecursive(node.left) or insertRecursive(node.right)
        if not insertRecursive(self.root):
            print(f"Error: Doctor {parentName} was not found. ")

    #Traversal Methods
    #Preorder
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
    #This function visits the root and then left subtree then right subtree

    #Inorder
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
    #This function visit the left subtree first, then root, then right subtree
     
    #Postorder 
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
    #This function first visit the left subtree, then right subtree, then the root




# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Gutierrez")
tree.insert("Dr. Gutierrez", "Dr. Sanchez", "left")
tree.insert("Dr. Gutierrez", "Dr. Andrews", "right")
tree.insert("Dr. Andrews", "Dr. St. CLair", "left")
tree.insert("Dr. Andrews", "Dr. Ribeiro", "right")

print("Preorder: ", tree.preorder(tree.root))
print("Inorder: ", tree.inorder(tree.root))
print("Postorder: ", tree.postorder(tree.root))