from transformers import AutoTokenizer
from models.risk_model import GBVRiskClassifier
from orchestrator import Orchestrator

from agents.intake_agent import IntakeAgent
from agents.risk_agent import RiskAnalysisAgent
from agents.context_agent import ContextAgent
from agents.decision_agent import DecisionAgent
from agents.human_agent import HumanAgent
from agents.audit_agent import AuditAgent

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = GBVRiskClassifier("bert-base-multilingual-cased")

agents = {
    "intake": IntakeAgent(tokenizer),
    "risk": RiskAnalysisAgent(model),
    "context": ContextAgent(),
    "decision": DecisionAgent(),
    "human": HumanAgent(),
    "audit": AuditAgent()
}

system = Orchestrator(agents)

output = system.run(
    text="He locked the door and threatened me",
    meta={"hour": 22, "repeat_case": True}
)

print(output)
