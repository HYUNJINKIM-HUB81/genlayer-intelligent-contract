# GenLayer Intelligent Contract Example
# Language: Python (GenLayer SDK)

class IntelligentContract:
    def __init__(self):
        # 계약 상태 변수 초기화
        self.state_proposal = ""
        self.status = "PENDING"
        self.consensus_score = 0

    def submit_proposal(self, proposal_text: str):
        """
        사용자가 제안서(자연어 텍스트)를 제출하는 함수
        """
        self.state_proposal = proposal_text
        self.status = "UNDER_REVIEW"
        return f"Proposal submitted successfully: {proposal_text}"

    def evaluate_consensus(self, validator_feedbacks: list):
        """
        GenLayer의 Optimistic Democracy 합의 메커니즘을 흉내낸 검증기 합의 평가 함수
        - 다수의 검증기(Validator)가 자연어 논리를 추론하여 동등성(Equivalence)을 평가합니다.
        """
        if not validator_feedbacks:
            return "No validator feedbacks provided."

        # 검증 노드 간 동의/합의 비중 계산
        positive_votes = sum(1 for vote in validator_feedbacks if vote.get("approved") is True)
        total_votes = len(validator_feedbacks)
        
        approval_ratio = positive_votes / total_votes

        # 다수결 자연어 합의 도출
        if approval_ratio >= 0.66:
            self.status = "APPROVED"
            self.consensus_score = approval_ratio
            return f"Contract Approved with {approval_ratio * 100:.1f}% Consensus."
        else:
            self.status = "REJECTED"
            self.consensus_score = approval_ratio
            return f"Contract Rejected. Approval ratio: {approval_ratio * 100:.1f}%."

    def get_contract_state(self):
        """
        현재 온체인 지능형 계약의 상태를 조회하는 함수
        """
        return {
            "proposal": self.state_proposal,
            "status": self.status,
            "consensus_score": self.consensus_score
        }
