def dfs(node, val, ret):
    intVal = val*10+node.val
    if node.left:
        dfs(node.left, intVal, ret)
    if node.right:
        dfs(node.right, intVal, ret)

    if not node.left and not node.right:
        ret.append(intVal)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = []
        dfs(root, 0, ret)
        return sum(ret)
