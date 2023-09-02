## Discrete Mathematics with C++: Graph Theory Basics

_Discrete mathematics_ is a branch of mathematics that deals with distinct and separate objects or structures. One of the most prominent areas within discrete mathematics is _graph theory_, which studies networks of interconnected nodes and edges. In this article, we'll explore the basics of graph theory and how to represent and traverse graphs using C++.

### 1. Graph Representation in C++

A graph can be represented in various ways, but the two most common methods are the _adjacency matrix_ and the _adjacency list_.

#### 1.1 Adjacency Matrix

An adjacency matrix is a 2D array of size `V x V` where `V` is the number of vertices in a graph. The value `m[i][j]` is `1` if there is an edge from vertex `i` to vertex `j`, otherwise `0`.

```cpp
#include <iostream>
using namespace std;

#define V 5

void addEdge(int adjMatrix[V][V], int i, int j) {
    adjMatrix[i][j] = 1;
    adjMatrix[j][i] = 1; // For undirected graph
}

int main() {
    int adjMatrix[V][V] = {0};

    addEdge(adjMatrix, 0, 1);
    addEdge(adjMatrix, 0, 4);
    addEdge(adjMatrix, 1, 3);
    addEdge(adjMatrix, 1, 4);
    addEdge(adjMatrix, 2, 3);

    // Print matrix
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cout << adjMatrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
```

#### 1.2 Adjacency List

An adjacency list represents a graph as an array of linked lists. The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Graph {
    int V;
    vector<int> *adjList;

public:
    Graph(int V);
    void addEdge(int v, int w);
    void printGraph();
};

Graph::Graph(int V) {
    this->V = V;
    adjList = new vector<int>[V];
}

void Graph::addEdge(int v, int w) {
    adjList[v].push_back(w);
    adjList[w].push_back(v); // For undirected graph
}

void Graph::printGraph() {
    for (int v = 0; v < V; v++) {
        cout << "Adjacency list of vertex " << v << ":\n";
        for (auto x : adjList[v])
            cout << "-> " << x;
        cout << endl;
    }
}

int main() {
    Graph g(5);

    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 3);

    g.printGraph();

    return 0;
}
```

### 2. Graph Traversal

Graph traversal is the process of visiting all the vertices of a graph. Two of the most common methods are _Depth First Search (DFS)_ and _Breadth First Search (BFS)_.

#### 2.1 Depth First Search (DFS)

DFS is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes by going ahead, if possible, else by backtracking.

```cpp
// ... [Previous code for Graph class]

void Graph::DFSUtil(int v, bool visited[]) {
    visited[v] = true;
    cout << v << " ";

    for (int i = 0; i < adjList[v].size(); i++) {
        if (!visited[adjList[v][i]])
            DFSUtil(adjList[v][i], visited);
    }
}

void Graph::DFS(int v) {
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;

    DFSUtil(v, visited);
}

// ... [Main function]
```

#### 2.2 Breadth First Search (BFS)

BFS is a layer-by-layer traversal method. It uses a queue to keep track of nodes to be explored.

```cpp
// ... [Previous code for Graph class]

void Graph::BFS(int s) {
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;

    list<int> queue;

    visited[s] = true;
    queue.push_back(s);

    while (!queue.empty()) {
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        for (auto i = adjList[s].begin(); i != adjList[s].end(); i++) {
            if (!visited[*i]) {
                visited[*i] = true;
                queue.push_back(*i);
            }
        }
    }
}

// ... [Main function]
```

### Conclusion

Graph theory is a vast and fascinating area of discrete mathematics with numerous applications in computer science. Using C++, we can efficiently represent and traverse graphs, making it a powerful tool for solving complex problems in this domain.
