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
     else:
      currentNode=nodeBar #set current node to root node
      outerNode=Node()
      while True:
        outerNode=currentNode
        if a<currentNode.value:
          outerNode.leftNode=node
          # if input value is less than current node, add as left node
          if currentNode.value== None:
            outerNode.leftNode== Node()
            outerNode.leftNode= node
            return
