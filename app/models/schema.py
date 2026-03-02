from pydantic import BaseModel
from typing import List

class RiskAnalysis(BaseModel):
    clause_text: str       # The actual text from the contract
    risk_level: str        # "High", "Medium", or "Low"
    issue: str             # Why is this risky?
    suggested_edit: str    # How should the startup fix it?

class ContractReport(BaseModel):
    contract_name: str
    risks: List[RiskAnalysis]
    summary: str