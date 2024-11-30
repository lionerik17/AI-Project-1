def aStarSearch(problem, heuristic=nullHeuristic):
    pqueue = util.PriorityQueue()
    pqueue.push((problem.getStartState(), [], 0),
                heuristic(problem.getStartState(), problem))
    cost_so_far = {problem.getStartState(): 0}
    while not pqueue.isEmpty():
        state, path, cost = pqueue.pop()
        if problem.isGoalState(state):
            return path
        for successor, action, stepCost in problem.getSuccessors(state):
            new_cost = cost + stepCost
            if successor not in cost_so_far or new_cost < cost_so_far[successor]:
                cost_so_far[successor] = new_cost
                priority = new_cost + heuristic(successor, problem)
                pqueue.push((successor, path + [action], new_cost), priority)
    return []
