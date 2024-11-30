def cornersHeuristic(state, problem):
    corners = problem.corners
    walls = problem.walls
    heuristic = 0

    cornersVisited = state[1]
    unvisitedCorners = [corner for i, corner in enumerate(corners)
                       if not cornersVisited[i]]

    if not unvisitedCorners:
        return 0

    current = state[0]

    while unvisitedCorners:
        distances = [(util.manhattanDistance(current, corner), corner)
                    for corner in unvisitedCorners]
        minDistance, nextCorner = min(distances)
        heuristic += minDistance
        current = nextCorner
        unvisitedCorners.remove(nextCorner)

    return heuristic
