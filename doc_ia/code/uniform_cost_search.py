def uniformCostSearch(problem):
    pqueue = util.PriorityQueue()
    pqueue.push((problem.getStartState(), [], 0), 0)
    visited = set()
    cost_so_far = {problem.getStartState(): 0}
    while not pqueue.isEmpty():
        state, path, stepCost = pqueue.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                new_cost = stepCost + cost
                if successor not in cost_so_far or new_cost < cost_so_far[successor]:
                    cost_so_far[successor] = new_cost
                    pqueue.push((successor, path + [action], new_cost), new_cost)
    return []
