def getAction(gameState):
    def alphaBeta(agentIndex, depth, state, alpha, beta):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)

        numAgents = state.getNumAgents()
        nextAgent = (agentIndex + 1) % numAgents
        nextDepth = depth + 1 if nextAgent == 0 else depth

        if agentIndex == 0:
            value = float('-inf')
            for action in state.getLegalActions(agentIndex):
                value = max(value, alphaBeta(nextAgent, nextDepth,
                        state.generateSuccessor(agentIndex, action), alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value
        else:
            value = float('inf')
            for action in state.getLegalActions(agentIndex):
                value = min(value, alphaBeta(nextAgent, nextDepth,
                        state.generateSuccessor(agentIndex, action), alpha, beta))
                if value < alpha:
                    return value
                beta = min(beta, value)
            return value

    alpha = float('-inf')
    beta = float('inf')
    bestAction = None
    bestValue = float('-inf')
    for action in gameState.getLegalActions(0):
        value = alphaBeta(1, 0,
                gameState.generateSuccessor(0, action), alpha, beta)
        if value > bestValue:
            bestValue = value
            bestAction = action
        alpha = max(alpha, bestValue)

    return bestAction
