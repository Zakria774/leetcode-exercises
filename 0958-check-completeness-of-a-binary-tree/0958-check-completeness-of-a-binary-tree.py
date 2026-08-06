# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Recursive helper returns (is_complete, height, is_perfect)
        def dfs(node):
            if not node:
                return True, 0, True
            
            comp_l, h_l, perf_l = dfs(node.left)
            comp_r, h_r, perf_r = dfs(node.right)
            
            # Case A: Left is PERFECT, Right is COMPLETE, same height
            cond_a = perf_l and comp_r and (h_l == h_r)
            
            # Case B: Left is COMPLETE, Right is PERFECT, left height is 1 greater
            cond_b = comp_l and perf_r and (h_l == h_r + 1)
            
            is_complete = cond_a or cond_b
            height = 1 + max(h_l, h_r)
            is_perfect = perf_l and perf_r and (h_l == h_r)
            
            return is_complete, height, is_perfect

        # Return only the boolean (is_complete) to LeetCode
        return dfs(root)[0]