import imagematrix
import math


class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        # initialize
        dp = dict()
        parent = dict()
        for i in range(-1, self.width+1):
            dp[i, -1] = 0
        for j in range(self.height):
            dp[-1, j] = math.inf
            dp[self.width, j] = math.inf

        # bottom-up subproblem
        for j in range(self.height):
            for i in range(self.width):
                m = math.inf
                for delta in (-1, 0, 1):
                    if dp[i+delta, j-1] < m:
                        m = dp[i+delta, j-1]
                        parent[i, j] = (i+delta, j-1)
                dp[i, j] = m + self.energy(i, j)

        # original problem
        m = math.inf
        pos = None
        for i in range(self.width):
            if dp[i, self.height-1] < m:
                pos = (i, self.height-1)
                m = dp[pos]

        coordinates = []
        while pos in parent: 
            coordinates.append(pos)
            pos = parent[pos]

        return list(reversed(coordinates))

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
