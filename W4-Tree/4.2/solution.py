# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []
        current = []
        if root:
            current = [root]
        while current:
            right_side.append(current[-1].val)
            new_level_nodes = []
            for node in current:
                if node.left:
                    new_level_nodes.append(node.left)

                if node.right:
                    new_level_nodes.append(node.right)

            current = new_level_nodes

        return right_side
