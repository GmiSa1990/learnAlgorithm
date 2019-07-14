



## 数据类型定义

- 类型名称：图（Graph）

- 数据对象集：G(V, E)由一个**非空的**有限顶点集合**V**和有限边集合**E**组成

- 操作集（部分）：

  ```c
  Graph create();
  Graph insertVertex(Graph G, Vertex V);
  Graph insertEdge(Graph G, Edge E);
  // 从顶点V出发深度优先遍历图G
  void DFS(Graph G, Vertex V);
  // 从顶点V出发宽度优先遍历图G
  void WFS(Graph G, Vertex V);
  // 顶点V到其他任意顶点的最短距离
  void shortestPath(Graph G, Vertex V, int dist[])；
  // 最小生成树
  void MST(Graph G);
  ```

- 常见术语：
  - 有向图与无向图
  - 无权图与有权图
  - 。。。

## 图的表示

- 邻接矩阵

  - 对于无向图的存储，怎样可以节省一半空间？

    用一个长度为N(N-1)/2的一位数组。

  - 优点：直观、简单、方便查找、方便查找任意顶点的邻接点、方便计算任一顶点的度（从该点发出的边数为出度、指向该顶点的边数为入度）

  - 缺点：浪费空间（尤其是点多边少的稀疏图）、浪费时间（统计稀疏图的边数）

- 邻接表
  - G[n]为**指针数组**，对应矩阵每行的一个链表，只存非零元素。
  -   