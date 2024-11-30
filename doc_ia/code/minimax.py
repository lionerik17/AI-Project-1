def getAction(gameState):
    def minimax(agentIndex, depth, state):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)

        numAgents = state.getNumAgents()
        nextAgent = (agentIndex + 1) % numAgents
        nextDepth = depth + 1 if nextAgent == 0 else depth

        if agentIndex == 0:
            return max(minimax(nextAgent, nextDepth,
                   state.generateSuccessor(agentIndex, action))
                   for action in state.getLegalActions(agentIndex))
        else:
            return min(minimax(nextAgent, nextDepth,
                   state.generateSuccessor(agentIndex, action))
                   for action in state.getLegalActions(agentIndex))

    legalMoves = gameState.getLegalActions(0)
    scores = [minimax(1, 0,
             gameState.generateSuccessor(0, action))
             for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices)
    return legalMoves[chosenIndex]
