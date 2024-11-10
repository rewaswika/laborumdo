function findNearest(node, queryPoint, currentClosestNode):
    if node is null:
        return currentClosestNode
    
    // Calculate distance from query point to the node's bounding box or centroid
    distanceToBoundary = distance(queryPoint, node.boundary)
    
    // Check if this quadrant can't contain a closer node than current closest
    if distanceToBoundary > distance(queryPoint, currentClosestNode):
        return currentClosestNode  // Stop searching this quadrant
    
    // Check if the node itself is closer than current closest
    if distance(queryPoint, node) < distance(queryPoint, currentClosestNode):
        currentClosestNode = node
    
    // Recursively search child quadrants or nodes
    for each child in node.children:
        currentClosestNode = findNearest(child, queryPoint, currentClosestNode)
    
    return currentClosestNode
