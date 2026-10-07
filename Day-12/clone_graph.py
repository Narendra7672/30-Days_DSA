# Clone Graph:
def Clonegraph(node):
    if not node:
        return None
    copy = {}
    queue = [node]
    copy[node] = Node(node.val,[])
    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor not in copy:
               copy[neighbor] = Node(neighbor.val,[])
               queue.append(neighbor)
            copy[current].neighbors.append(copy[neighbor] )
    return copy[node] 

