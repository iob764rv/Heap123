class Heap:
  from Node import Node
  
  global nodeBar
  nodeBar = Node()
  
  def addValue(a):
    from Node import Node
    #add a value to the heap
    
    node=Node().setInput(a)
    if nodeBar.value== None: #condition for empty tree
      
      nodeBar.setValue(a)
