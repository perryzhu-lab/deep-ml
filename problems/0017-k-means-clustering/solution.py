import numpy as np


def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int,
) -> list[tuple[float, ...]]:
    for _ in range(max_iterations):
        # 1. 计算每个点与k个中心的距离
        points = np.asarray(points, dtype=float)
        initial_centroids = np.asarray(initial_centroids, dtype=float)

        distances = np.linalg.norm(
            points[:, None, :] - initial_centroids[None, :, :], axis=2
        )

        # 2. 分配数据点
        index = np.argmin(distances, axis=1)

        # 3. 更新聚类中心
        new_centroids = initial_centroids.copy()
        for i in range(k):
            cluster = points[index == i]
            if len(cluster) > 0:
                new_centroids[i] = np.mean(cluster, axis=0)

        initial_centroids = new_centroids

    final_centroids = np.round(initial_centroids, 4)

    return [tuple(row) for row in final_centroids]
