from typing import List

def bayes_ball(A: List[List[int]], X: List[int], E: List[int]) -> List[int]:
    ans = set()  # Initialize ancestors of evidence nodes
    for e in E:
        for i in range(len(A)):
            if (e in A[i]):
                ans.add(i)
    frontier = []  # Initialize the frontier
    explored = set()  # Initialize explored nodes
    reachable = set()  # Initialize reachable nodes
    E = set(E)  # Convert evidence nodes to a set
    
    for a in X:
        frontier.append((a, 0))
        

    while len(frontier) > 0:
        node, direction = frontier.pop(0)
        reachable.add(node)

        if node in E:  # If this node is observed
            if direction == 0:  # Reached from a child (from-child)
                pass
            else: #Reached from a parent
                for parent in A:
                    if node in parent:
                        if ((A.index(parent),0) not in explored and (A.index(parent),0) not in frontier):
                            frontier.append((A.index(parent), 0))
        else:  # If this node is unobserved
            if (direction == 0):
                for parent in A:
                    if node in parent:
                        if ((A.index(parent),0) not in explored and (A.index(parent),0) not in frontier):
                            frontier.append((A.index(parent), 0))
                for child in A[node]:
                    if ((child, 1) not in explored and (child, 1) not in frontier):
                        frontier.append((child, 1))
            else:
                for parent in A:
                    if node in parent:
                        if (node in ans and (A.index(parent), 0) not in explored and (A.index(parent), 0) not in frontier):
                            frontier.append((A.index(parent), 0))
                for child in A[node]:
                    if ((child,1) not in explored and (child,1) not in frontier):
                        frontier.append((child, 1))
                        

        explored.add((node, direction))  # Mark the current node as explored

    # Compute unreachable nodes
    n = len(A)
    all_nodes = set(range(n))
    unreachable = all_nodes - reachable

    return list(unreachable)


# Example usage:
A = [[1, 3], [4], [1], [4], [5], []]
X, E = [3], [0]
result = bayes_ball(A, X, E)
print("Unreachable nodes:", result)

