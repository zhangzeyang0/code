
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, node):  # returns: max one side path sum, max path sum
            l = r = 0
            max_l = max_r = -float('inf')
            # max_l = max_r = 0
            if node.left:
                l, max_l = self.dfs(node.left)
            if node.right:
                r, max_r = self.dfs(node.right)
            return node.val + max(l, r), max(max_l, max_r, node.val + l + r)

    def maxPathSum(self, root):
        if root:
            return self.dfs(root)[1]
        return 0

    def Convert(self, pRootOfTree):
        # write code here
        stack = []
        node = pRootOfTree
        pre_node = TreeNode(None)
        while stack or node:
            # print(stack, node.val)
            if node:
                while node.left:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
            node.left = pre_node
            if pre_node.val is None:
                res = node
            pre_node.right = node
            pre_node = node
            node = node.right
        return res

    def post_order(self, root):
        if not root:
            return
        flag = None
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack[-1].right == flag:
                flag = stack.pop()
                print(flag.val)
            elif stack[-1].left == flag:
                root = stack[-1].right
                flag = None
    def last_common_parent2(self, root, node1, node2):
        if root == None or node1 == None or node2 == None:
            return None

        #如果两个节点中有一个等于该子树的根节点，则直接返回子树的根节点
        if node1 == root or node2 == root:
            return root
        #递归左子树和右子树
        left_lca = self.last_common_parent2(root.left, node1, node2)
        right_lca = self.last_common_parent2(root.right, node1, node2)
        #如果左右子树返回值都不为None,则说明返回在node1 == root or node2 == root处返回的，则返回root
        if left_lca and right_lca:
            return root
        #如果返回的是left_lca为None,则说明左子树找到地也没有找到，则两个节点都在右子树，则返回right_lca
        #如果返回的是right_lca为None,则说明y右子树找到地也没有找到，则两个节点都在左子树，则返回left_lca
        if left_lca == None:
            return right_lca
        else:
            return left_lca







    def last_common_parent(self, root, node1, node2):
        if not root or not node1 or not node2:
            return None
        if node1 == root or node2 == root:
            return root
        left = self.last_common_parent(root.left, node1, node2)
        right = self.last_common_parent(root.right, node1, node2)
        if right and left:
            return root
        return left if right is None else right


a1 = TreeNode(5)
a2 = TreeNode(3)
a3 = TreeNode(8)
a4 = TreeNode(1)
a5 = TreeNode(4)
a6 = TreeNode(6)
a7 = TreeNode(9)
a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7

t = Solution()
# print(t.maxPathSum(a1))
# print(t.Convert(a1))
# t.post_order(a1)

print(t.last_common_parent(a1, a3, a6).val)
