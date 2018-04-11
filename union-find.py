class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                parent[a] = parent[b]
                self.nodes -= 1
                return True
            return False

        parent = [i for i in range(n)]
        self.nodes = n
        for e in edges:
            if not union(e[0], e[1]):
                return False
        print parent
        return self.nodes == 1

o = Solution()
print o.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
