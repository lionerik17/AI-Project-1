def depthFirstSearch(problem):
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = set()
    while not stack.isEmpty():
        state, path = stack.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in visited:
                    stack.push((successor, path + [action]))
    return []
