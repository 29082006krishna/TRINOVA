class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run(self, text, meta):
        state = {}
        state["tokens"] = self.agents["intake"].run(text)
        state["risk"] = self.agents["risk"].run(state["tokens"])
        state["context"] = self.agents["context"].run(meta)
        state["decision"] = self.agents["decision"].run(
            state["risk"], state["context"]
        )
        state["human"] = self.agents["human"].run(state["decision"])
        state["audit"] = self.agents["audit"].run(state)
        return state
