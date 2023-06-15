import os
import sys
from typing import Optional
from pyprojroot import here as get_project_root
os.chdir(get_project_root())
sys.path.append(str(get_project_root()))
from modules.lc_supplementary import TreeNode, to_binary_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ordered_nodes = []

        def inOrder(node):
            if node is None:
                return None
            inOrder(node.left)
            ordered_nodes.append(node.val)
            inOrder(node.right)

        inOrder(root)
        min_diff = 10**5
        for idx in range(1, len(ordered_nodes)):
            min_diff = min(min_diff, ordered_nodes[idx] - ordered_nodes[idx - 1])
        
        return min_diff


class TestClass:

    def test_one(self):
        input = [4,2,6,1,3] 
        test = Solution()
        assert test.getMinimumDifference(to_binary_tree(input)) == 1


    def test_two(self):
        input = [1,0,48,None,None,12,49]
        test = Solution()
        assert test.getMinimumDifference(to_binary_tree(input)) == 1