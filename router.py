import sys

INF = sys.maxsize

class RoutingTableEntry:
    def __init__(self):
        self.nextHop = -1
        self.cost = INF

def distance_vector_routing(cost_matrix):
    num_routers = len(cost_matrix)
    routing_table = [[RoutingTableEntry() for _ in range(num_routers)] for _ in range(num_routers)]

    for i in range(num_routers):
        for j in range(num_routers):
            if i == j:
                routing_table[i][j].nextHop = i
                routing_table[i][j].cost = 0
            elif cost_matrix[i][j] != INF:
                routing_table[i][j].nextHop = j
                routing_table[i][j].cost = cost_matrix[i][j]

    for k in range(num_routers):
        for i in range(num_routers):
            for j in range(num_routers):
                if routing_table[i][j].cost > routing_table[i][k].cost + routing_table[k][j].cost:
                    routing_table[i][j].cost = routing_table[i][k].cost + routing_table[k][j].cost
                    routing_table[i][j].nextHop = k

    return routing_table

def main():
    num_routers = int(input("Enter the number of routers: "))

    cost_matrix = [[INF] * num_routers for _ in range(num_routers)]

    print("Enter the cost matrix (use INF for no direct link):")
    for i in range(num_routers):
        cost_matrix[i] = list(map(int, input().split()))

    routing_table = distance_vector_routing(cost_matrix)

    print("\nRouting Table:")
    for i in range(num_routers):
        for j in range(num_routers):
            if i != j:
                print(f"Router {i} to Router {j} via Router {routing_table[i][j].nextHop} Cost: {routing_table[i][j].cost}")

if __name__ == "__main__":
    main()
