#include <stdio.h>
#include <stdlib.h>

// Node for adjacency list
struct Node {
    int vertex;
    struct Node* next;
};

// Graph structure
struct Graph {
    int numVertices;
    struct Node** adjLists;
};

// Create a new node
struct Node* createNode(int v) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// Create a graph
struct Graph* createGraph(int vertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;
    graph->adjLists = (struct Node**)malloc(vertices * sizeof(struct Node*));
    for (int i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;
    return graph;
}

// Add edge (undirected)
void addEdge(struct Graph* graph, int u, int v) {
    struct Node* nodeV = createNode(v);
    nodeV->next = graph->adjLists[u];
    graph->adjLists[u] = nodeV;

    struct Node* nodeU = createNode(u);
    nodeU->next = graph->adjLists[v];
    graph->adjLists[v] = nodeU;
}

// Delete edge
void deleteEdge(struct Graph* graph, int u, int v) {
    struct Node **prev, *curr;

    // Remove v from u's list
    prev = &graph->adjLists[u];
    curr = graph->adjLists[u];
    while (curr != NULL) {
        if (curr->vertex == v) {
            *prev = curr->next;
            free(curr);
            break;
        }
        prev = &curr->next;
        curr = curr->next;
    }

    // Remove u from v's list
    prev = &graph->adjLists[v];
    curr = graph->adjLists[v];
    while (curr != NULL) {
        if (curr->vertex == u) {
            *prev = curr->next;
            free(curr);
            break;
        }
        prev = &curr->next;
        curr = curr->next;
    }
}

// Print adjacency list
void printGraph(struct Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        struct Node* temp = graph->adjLists[i];
        printf("%d: ", i);
        while (temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("NULL\n");
    }
}

// Driver code
int main() {
    int V = 5; // Number of vertices
    struct Graph* graph = createGraph(V);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    printf("Graph adjacency list:\n");
    printGraph(graph);

    printf("\nDeleting edge 1-4\n");
    deleteEdge(graph, 1, 4);
    printGraph(graph);

    return 0;
}
