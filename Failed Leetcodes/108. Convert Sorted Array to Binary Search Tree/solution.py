def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    # Time: O(n)
    # Space: O(n) in the case of skewed binary tree.
    def convert(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = convert(left, mid - 1)
        node.right = convert(mid + 1, right)
        return node
    return convert(0, len(nums) - 1)