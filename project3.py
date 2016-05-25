

class BSTNode:
    def __init__(self,x,L=None,R=None,level=None):
        self.data=x
        self.left=L
        self.right=R
        self.level=level

    def hasL(self):
        if(self.l!=None):
            return True
        else:
            return False
    def hasR(self):
        if(self.r!=None):
            return True
        else:
            return False
    def Data(self):
        return self.data


class BST:
    def __init__(self):
        self.root=None

    def insert(self,x):
        def recurse(p):
            if x<p.data:
                if p.left==None:
                    p.left=BSTNode(x)
                else:
                    recurse(p.left)
            else:
                if p.right==None:
                    p.right=BSTNode(x)
                else:
                    recurse(p.right)
        if self.root==None:
            self.root=BSTNode(x)
        else:
            recurse(self.root)


            
    def display_in_order (self):		# parenthesized inorder traversal
        def recurse (p, rightChild=False):
            if p==None: return
            if rightChild: print ("", end=",")
            print ("[", end="")
            recurse (p.left)
            print (p.data,end="")
            recurse (p.right, True)
            print ("]", end="")
            if not rightChild: print ("", end="")
        recurse (self.root)
        print( )

    def display_pre_order(self):
        def recurse (p, rightChild=False):
            if p==None: return
            if rightChild: print ("", end=",")
            print ("[", end="")
            print (p.data,end="")
            recurse (p.left)
            recurse (p.right, True)
            print ("]", end="")
            if not rightChild: print ("", end="")
        recurse (self.root)
        print( )

    def display_post_order(self):
        def recurse (p, rightChild=False):
            if p==None: return
            if rightChild: print ("", end="")
            print ("[", end="")
            recurse (p.left)
            recurse (p.right, True)
            print (p.data,end="")
            print(',',end='')
            print ("]", end="")
            if not rightChild: print ("", end="")
        recurse (self.root)
        print( )


        
    def display_level_order(self):
        self.root.level=0
        q=[self.root]
        out=[[]]
        current_level=self.root.level
        while len(q)>0:
            current_node=q.pop(0)
            if current_node.level>current_level:
                current_level+=1
                out.append([])
               # print(out)
            out[current_level].append(current_node.data)
            if current_node.left:
                current_node.left.level=current_level+1
                #out.append([])
                q.append(current_node.left)
                #print(out)
            if current_node.right:
                current_node.right.level=current_level+1
                #out.append([])
                q.append(current_node.right)
                #print(out)
        print((out))




def main():
    T =BST()
    L=eval(input("Enter a list: "))
    for x in L:
        T.insert(x)
    print("In-order: ",end="")
    T.display_in_order()
    print("Pre-order: ",end='')
    T.display_pre_order()
    print("Post-order: ",end='')
    T.display_post_order()
    print("Level-order: ",end='')
    T.display_level_order()




main()        
