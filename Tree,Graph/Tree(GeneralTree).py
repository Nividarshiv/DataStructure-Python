class TreeNode:
    def __init__(self,name,destignation):
        self.name=name
        self.destignation=destignation
        self.child=[]
        self.parent=None

    def append_child(self,child):
        child.parent=self
        self.child.append(child)    

    def get_levels(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent    
        return level    

    def print_tree(self,data,levels):
        if self.get_levels()>levels:
               return
        space="   "*self.get_levels()
        prefix=space+"|__" if self.parent else " "
        if data=="both":
            print(prefix,self.name,"  (",self.destignation,")")  
        elif data=="name":
            print(prefix+self.name)
        else:
            print(prefix+self.destignation)    
     
        if self.child:
            for child in self.child:
                child.print_tree(data,levels)    

def build_tree():
    root=TreeNode("Nilpul","CEO")
    cinmay=TreeNode("Cinmay","CTO")
    vishwa=TreeNode("Vishwa","InfractureHead")
    vishwa.append_child(TreeNode("Dhwal","Cloud manager"))
    vishwa.append_child(TreeNode("Ambhit","Appmanager"))

    cinmay.append_child(vishwa)
    cinmay.append_child(TreeNode("Amair","Application head"))

    Gels=TreeNode("Gels","HR-Head")
    Gels.append_child(TreeNode("peter","Recuirement Manager"))
    Gels.append_child(TreeNode("waquas","policymanager"))

    root.append_child(cinmay)
    root.append_child(Gels)

    root.print_tree("both",3)
    root.print_tree("name",1)
    root.print_tree("destignation",2)

build_tree()   