
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        s = []

        def serialize_helper(root):
            if not root:
                s.append('null')
                return
            s.append(str(root.val))
            serialize_helper(root.left)
            serialize_helper(root.right)
        serialize_helper(root)

        return ' '.join(s)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        s = [int(i) for i in data.split(' ') if i != 'null']

        def deserialize_helper(serializedList, sortedList):

            if not serializedList and not sortedList:
                return None
            node = TreeNode(serializedList[0])
            ind = sortedList.index(node.val)
            node.left = deserialize_helper(
                serializedList[1:ind+1], sortedList[:ind])
            node.right = deserialize_helper(
                serializedList[ind+1:], sortedList[ind+1:])
            return node
        return deserialize_helper(s, sorted(s))
