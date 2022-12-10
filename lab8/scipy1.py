#A convex hull is the smallest polygon that covers all of the given points.
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [1, 3],
  [2, 4],
  [1, 0],
  [2, 3],
  [0, 1],
  [1, 2],
  [5, 4],
  [5, 1],
  [1, 2],
  [0, 2]
])
#clasa convexhull din scipy.spatial
hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()