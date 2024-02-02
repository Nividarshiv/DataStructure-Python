class Graph:
    def __init__(self,edges):
        self.dic_edges={}
        for start,end in edges:
            if start in self.dic_edges:
                self.dic_edges[start].append(end)
            else:
                self.dic_edges[start]=[end]
        print(self.dic_edges)    

    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]  
        if start not in self.dic_edges:
            return []        
        paths=[]
        for node in self.dic_edges[start]:
            if node not in path:
                path_list=self.get_paths(node,end,path)
                for p in path_list:   
                    paths.append(p)        
        return paths        
    
    def get_path_shortest(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path      
        if start not in self.dic_edges:
            return None       
        shortestpaths=None
        for node in self.dic_edges[start]:
            if node not in path:
                sp=self.get_path_shortest(node,end,path)
                if sp:  
                 if shortestpaths is None or len(sp)<=len(shortestpaths): 
                     shortestpaths=sp
        return shortestpaths        

routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
way=Graph(routes)  
print(way.get_paths("Mumbai","New York"))  
print(way.get_path_shortest("Mumbai","New York")) 
