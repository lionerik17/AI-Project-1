def foodHeuristic(state, problem):
    position, foodGrid = state
    foodList = foodGrid.asList()

    if not foodList:
        return 0

    left = min(food[0] for food in foodList)
    right = max(food[0] for food in foodList)
    top = min(food[1] for food in foodList)
    bottom = max(food[1] for food in foodList)

    minDistance = min(util.manhattanDistance(position, food) for food in foodList)
    maxDistance = (right - left) + (bottom - top)
    heuristic = minDistance + maxDistance

    return heuristic
