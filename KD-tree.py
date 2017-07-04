from collections import namedtuple
from pprint import pformat
import numpy as np

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))

def kdtree(range_list, depth=0):
    
    k = len(range_list) # cal number of dimensions
    axis = depth % k # Select axis based on depth so that axis cycles through all valid values
    
    
    if abs(range_list[axis][1] - range_list[axis][0]) < 2:  #Set the condition that the range cann't be divided 
        axis_hat = axis
        axis = (axis + 1)%k
        
        while((abs(range_list[axis][1] - range_list[axis][0]) < 2 and axis != axis_hat)):
            axis = (axis + 1)%k
        if axis == axis_hat:
            return Node(
                location = range_list,
                left_child= None,
                right_child= None )

    cuttingPoint = (range_list[axis][1] + range_list[axis][0])/2
    left_range_list = range_list[:] 
    right_range_list = range_list[:] 
    left_range_list[axis] = (range_list[axis][0],cuttingPoint)
    right_range_list[axis] = (cuttingPoint,range_list[axis][1],)
    
    # Create node and construct subtrees
    
    left_randomPoint = np.random.uniform(left_range_list[axis][0],left_range_list[axis][1],2)
    right_randomPoint = np.random.uniform(right_range_list[axis][0],right_range_list[axis][1],2)
    print(left_randomPoint)
    print(right_randomPoint)
    # Create node and construct subtrees
    if abs(left_randomPoint[0] - left_randomPoint[1]) < 1:
        left_child = "Eliminated"
    else:
        left_child = kdtree(left_range_list, depth + 1)

    if abs(right_randomPoint[0] - right_randomPoint[1]) < 1:
        right_child = "Eliminated"
    else:
        right_child = kdtree(right_range_list, depth + 1)

    return Node(
    location = range_list,
    left_child = left_child,
    right_child = right_child
    )

def main():
    """Example usage"""
    range_list = [(4,16),(7,23)]
    tree = kdtree(range_list)
    print(tree)

if __name__ == '__main__':
    main()
