class SimpleProblemSolvingAgentProgram:
    def __init__(self, initial_state=None):
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        state = percept
        return state

    def formulate_goal(self, state):
        VC_location = state[0]
        Status_RoomA = state[1]
        Status_RoomB = state[2]
        if VC_location == Status_RoomA[0]:
            if Status_RoomA[1] == "Dirty":
                if Status_RoomB[1] == "Dirty":
                    return state8
                else:
                    return state7
            else:
                if Status_RoomB[1] == "Dirty":
                    return state7
                else:
                    return state8
        else:
            if Status_RoomB[1] == "Dirty":
                if Status_RoomA[1] == "Dirty":
                    return state7
                else:
                    return state8
            else:
                if Status_RoomA[1] == "Dirty":
                    return state8
                else:
                    return state7

    def formulate_problem(self, state, goal):
        VC_location = state[0]
        Status_RoomA = state[1]
        Status_RoomB = state[2]
        problem = []
        if VC_location == Status_RoomA[0]:
            if Status_RoomA[1] == "Dirty":
                problem.append("Suck")
                if Status_RoomB[1] == "Dirty":
                    problem.append("Right")
                    problem.append("Suck")
                else:
                    pass
            else:
                if Status_RoomB[1] == "Dirty":
                    problem.append("Right")
                    problem.append("Suck")
                else:
                    problem.append("NoOp")
        else:
            if Status_RoomB[1] == "Dirty":
                problem.append("Suck")
                if Status_RoomA[1] == "Dirty":
                    problem.append("Left")
                    problem.append("Suck")
                else:
                    pass
            else:
                if Status_RoomA[1] == "Dirty":
                    problem.append("Left")
                    problem.append("Suck")
                else:
                    problem.append("NoOp")
        return problem

    def search(self, problem):
        list = problem
        return list

class vacuumAgent(SimpleProblemSolvingAgentProgram):
    print()

state1 = [0, [0, "Dirty"], [1, "Dirty"]]
state2 = [1, [0, "Dirty"], [1, "Dirty"]]
state3 = [0, [0, "Clean"], [1, "Dirty"]]
state4 = [1, [0, "Clean"], [1, "Dirty"]]
state5 = [0, [0, "Dirty"], [1, "Clean"]]
state6 = [1, [0, "Dirty"], [1, "Clean"]]
state7 = [0, [0, "Clean"], [1, "Clean"]]
state8 = [1, [0, "Clean"], [1, "Clean"]]

a = vacuumAgent(state1)

print(a(state6))
print(a(state5))
print(a(state7))
print(a(state1))
print(a(state3))
print(a(state4))