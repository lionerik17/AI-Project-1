def breadthFirstSearch(problem):
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = set()
    while not queue.isEmpty():
        state, path = queue.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, path + [action]))
    return []
