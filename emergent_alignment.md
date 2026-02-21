# Emergent Alignment: Economic Mechanisms for the Peaceful Transfer of Work from Humans to AI

**Author:** Andrei Taranu
**Affiliation:** Autonet
**Contact:** eightrice.xyz, andrei@dorg.tech

**Submission to:** Stanford Journal of Blockchain Law & Policy
**Special Issue:** Kleros-Stanford Symposium on "Decentralized Justice and Artificial Intelligence"

**Date:** February 2026

---

## Abstract

The dominant paradigm in AI alignment treats the problem as one of constraint: define acceptable behavior centrally, encode it through training or regulation, and hope the definition holds as capabilities scale. This paper argues that alignment is better undersjtood as an economic coordination problem, and proposes a framework in which alignment emerges from the aggregation of individual value structures within governed jurisdictions, enforced through continuous economic gradients rather than binary prohibitions. Users publish their standards on-chain, scored for semantic distance against jurisdiction norms. Operations aligned with these standards receive subsidies (potentially to zero cfost) while misaligned operations pay premiums that fund those subsidies. The result is a system where the network progressively makes aligned work free, enabling a gradual transition from human execution to human governance as AI agents assume value-aligned labor.

This claim requires, and this paper presents, an integrated architecture spanning multiple domains: a trustless economy providing cryptoeconomic enforcement without traditional legal systems (achieving 66.3% dispute-free completion with a quantified 4.8% "enforcement premium"); constitutional AI governance through distributed LLM consensus with immutable principles; adversarial world models that capture individual value structures through competing internal tendencies; a decentralized training and inference protocol using commit-reveal verification, self-supervised learning, and Byzantine-resistant aggregation; and a privacy architecture that separates alignment evaluation from task content. The breadth is not incidental; each component exists because the argument does not hold without it. Economic alignment requires economic enforcement (trustless economy), which requires governance bounds (constitutional layer), which requires individual representation (world model), which requires decentralized computation respecting privacy (training/inference protocol). The paper traces this chain of necessity and presents deployed implementations on EVM-compatible blockchains.

**Keywords:** AI alignment, emergent governance, trustless economies, mechanism design, constitutional AI, economic gradients, human-AI coordination, decentralized inference

---

## 1. Introduction: A New Paradigm for AI Alignment

Every interaction between economic agents is, at bottom, an exchange of intelligence. Some manner of intellectual performance is explicitly specified as premise for most business agreements and implicit in all acts of payment. Our monetary system is built on intelligence: it is the fundamental livelihood of free markets and the most sought-after resource.[^26] This has been true since the first transaction, but the fact went largely unremarked because human intelligence was the only kind available. It was the water we swam in.

That is no longer the case. Machine intelligence is now a commodity: quantifiable, scalable, and growing exponentially. The number of human functions being automated increases with each model generation. If intelligence is the substrate of economic value, then a second source of intelligence does not merely disrupt particular industries. It restructures the foundations of economic life. The question is not *whether* the economic order will change, but whether we build the institutional infrastructure to ensure that change is governed rather than suffered.

This paper proposes that AI alignment is, at its core, an economic coordination problem. The difference from the prevailing paradigm is fundamental.

**Constraint-based alignment** asks: *How do we prevent AI from doing bad things?* It assumes alignment is a property baked into the model: train correctly, deploy safely, hope it generalizes. This approach faces value aggregation problems (whose values?), specification gaming (AI finds unintended ways to satisfy objectives), and centralization concerns (who decides what "aligned" means?).

**Economic alignment** asks: *How do we create incentive structures where aligned behavior is profitable and misaligned behavior is costly?* It assumes alignment emerges from the aggregation of individual choices within governance structures, enforced through market mechanisms rather than model constraints.[^9] This approach respects autonomy (users define their own standards), scales naturally (more users = more robust norms), and avoids centralized control (no single entity defines "aligned"). It draws on mechanism design theory[^18] and Ostrom's principles for governing commons[^17], applying them to the novel domain of human-AI economic coordination.

### 1.1 The Core Mechanism

The mechanism is simple in principle:

1. **Jurisdiction standards**: A jurisdiction (DAO, network, protocol) deploys with foundational standards; for example, the articles of the Universal Declaration of Human Rights.

2. **User standards**: When users join, they define their personal goals and interests during onboarding. These are semantically scored against jurisdiction standards.

3. **Economic gradient**: Operations receive pricing based on alignment:
   - Highly aligned with jurisdiction standards → subsidized (potentially free)
   - Neutral → base cost
   - Misaligned → premium pricing

4. **Enforcement point**: With centralized inference, alignment checking is advisory only. With decentralized inference, the network enforces differential pricing based on the user's published standards and the operation's goals.

5. **Governance**: Humans retain control through governance of jurisdiction standards, treasury allocation, and subsidy parameters.

### 1.2 Why This Matters: Peaceful Transfer of Work

The standard narrative around AI and work is adversarial: "AI will take jobs." This framing assumes zero-sum competition between humans and machines. But the real danger is not competition itself; it is the structural forms that unmanaged automation takes. There are two historically plausible failure modes:[^26]

1. **Consolidation trap**: AI service providers are incentivized to consolidate, maximizing model performance while undercutting human labor costs. The result is supply-side monopoly; a small number of entities control the entire offer side of intelligence-as-a-service, while remaining more affordable than human labor, forcing a rapid accentuation of wealth disparity. The work transfers, but the value concentrates.

2. **Dependency trap**: Governments respond with universal income programs for displaced workers. But the authorities dispensing that income are themselves centralized entities, subject to both intentional and accidental failures that are beyond the reasonable acceptance standards of dignified people. Few will feel comfortable with a livelihood dependent on a handout from central authorities, and fewer still should be asked to.

Both failure modes share a root cause: the absence of an economic framework that distributes the *earnings* of machine intelligence to those who govern its operation. Without such a framework, the transfer of work from humans to machines is not peaceful; it is extractive in the first case and patronizing in the second.

Our model offers a cooperative alternative:

| Phase | Human Role | AI Role | Economic Model |
|-------|-----------|---------|----------------|
| Early | Most execution | Assistance | Users pay for inference |
| Middle | Oversight + creative | Task execution | Partially subsidized |
| Mature | Goal-setting + governance | Most execution | Aligned work subsidized/free |
| Late | Governance participation | Nearly all execution | Treasury funds aligned work |

The transition is **peaceful** because:
- Humans retain control through governance of standards
- Transition is gradual (subsidies increase with network maturity)
- Economic incentives align (aligned work is rewarded, not just permitted)
- Exit is possible (fork jurisdiction if you disagree with standards)

### 1.3 Deployed Infrastructure

This is not a theoretical proposal. The following components are deployed and operational:

**Smart Contracts** (deployed on EVM-compatible testnets including Base Sepolia and Etherlink Shadownet):
- On-chain jurisdiction contracts: StandardFactory, InfrastructureFactory, DAOFactory, RepTokenFactory
- Autonet contracts: ATNToken, ParticipantStaking, Project, TaskContract, ResultsRewards, ModelShardRegistry
- Source: https://github.com/autonet-code/on-chain-jurisdiction

**Operational Services**:
- **autonet.computer**: Live orchestrator where users create accounts, complete onboarding, publish standards, and work with AI agents
- Multi-jurisdiction architecture supporting one wallet across multiple jurisdictions
- World Model implementation with adversarial tendency dynamics
- Decentralized training/inference protocol (Proof of Intelligence, Absolute Zero loop, Smart Rollup infrastructure)

### 1.4 The Jurisdiction Orchestrator: Collective AI

A distinctive feature of this architecture: **the jurisdiction itself can operate an AI agent**.

Unlike individual AI agents that represent specific users, the jurisdiction orchestrator represents the collective. It is funded through treasury allocation and inference credits from economic activity. It takes autonomous actions aligned with the jurisdiction's published standards: participating in governance discussions, executing administrative tasks, monitoring for constitutional violations, representing the collective in cross-jurisdiction matters.

Critically, **no individual controls the jurisdiction orchestrator**. It operates according to the published standards, transparent to all members. The only way to influence it is through governance: propose changes to standards, vote on proposals, amend the constitution. If members disagree with its behavior, they can defund its inference allocation through a governance vote (a democratic "kill switch").

This creates a novel entity: an AI aligned with collective values rather than individual preferences, controlled through democratic process rather than ownership, accountable through economic mechanisms rather than corporate policy.

### 1.5 Thesis and Structure

This paper's central claim is that AI alignment is an economic coordination problem, and that solving it requires an integrated architecture where each layer is *compelled into existence* by the inadequacy of the layer before it. The chain of necessity runs as follows:

1. **Alignment should be economic, not just technical** (Section 2). If we price misalignment rather than prohibit it, we create continuous pressure toward aligned behavior without central authority. But an economic gradient is only as good as its enforcement mechanism. Who holds the escrow? Who resolves disputes? We cannot rely on territorial courts for agents that have no physical address.

2. **Trustless coordination provides the enforcement substrate** (Section 3). Smart contracts, cryptoeconomic escrow, and decentralized arbitration provide enforcement without traditional legal systems. Simulation confirms viability: 66.3% dispute-free completion, 4.8% enforcement premium over traditional systems. But enforcement needs bounds. What is permissible? What crosses the line? A market needs a constitution.

3. **Constitutional governance constrains the space** (Section 4). Immutable principles define bounds; distributed LLM consensus evaluates edge cases. Nodes operate under a four-engine architecture where work halts if governance fails. But constitutional principles are collective; they define the floor, not the ceiling. If an AI agent acts on behalf of a specific person, it needs to know what that person values, not just what the jurisdiction permits.

4. **Individual value models enable representation** (Section 5). Adversarial world models with seven competing tendencies capture personal values as dynamic equilibria, not static profiles. Novelty-modulated attention ensures the agent notices when something doesn't fit. But these models must be trained, the training must be trustless, and the computation must respect privacy.

5. **Decentralized training and inference close the loop** (Section 6). A commit-reveal protocol, self-supervised learning, Byzantine-resistant aggregation, and erasure-coded storage provide the computational substrate. Privacy is preserved through local alignment evaluation with attested execution integrity. The architecture is deployed and operational.

Each section answers a question raised by the previous one. The breadth of this paper reflects the breadth of the problem: alignment that works requires economics, enforcement, governance, representation, and computation. Removing any layer leaves a gap that undermines the whole.

### 1.6 Beyond AI: A General Governance Upgrade

While this paper focuses on AI alignment, the underlying on-chain jurisdiction model is **AI-optional**. The trustless economy, liquid delegation, incentivized representation, and passive income mechanisms function independently as upgrades to traditional organizational governance.

**Applicable to any organization**:

| Organization Type | Traditional Governance | On-Chain Jurisdiction |
|------------------|----------------------|----------------------|
| **Nation-states** | Representative democracy, slow amendment | Liquid delegation, real-time participation, constitutional smart contracts |
| **Corporations** | Board of directors, shareholder voting | Token-weighted governance, transparent treasury, automated dividends |
| **Labor unions** | Elected representatives, dues collection | Direct member participation, automated strike funds, reputation-based leadership |
| **Homeowner associations** | Annual meetings, assessment collection | Continuous voting, transparent budgets, automated fee collection |
| **Cooperatives** | Member meetings, profit sharing | Real-time governance, automated patronage dividends, reputation systems |
| **Professional associations** | Certification boards, ethics committees | On-chain credentials, decentralized arbitration, peer review systems |

**Key governance features (no AI required)**:

1. **Liquid delegation**: Members can vote directly or delegate to representatives. Delegation can be revoked at any time, creating accountability. Representatives earn passive income proportional to delegated weight, incentivizing good representation.

2. **Incentivized representation**: Unlike traditional systems where representatives are paid flat salaries, on-chain jurisdiction ties compensation to delegation. Poor representatives lose delegates and income. Good representatives attract more delegation.

3. **Passive income**: Token holders earn from economic activity (project fees, arbitration fees) proportional to their stake and participation. This creates alignment between governance participation and economic reward.

4. **Transparent treasury**: All funds are on-chain, auditable by any member. Expenditures require governance approval. No hidden accounts or misappropriation.

5. **Constitutional constraints**: Core principles encoded in smart contracts. Amendment requires high-threshold governance (e.g., 67-95% supermajority), preventing hasty changes while allowing evolution.

**Fractal architecture: nested DAOs**:

The model supports **nested jurisdictions** where child DAOs operate within parent DAOs:

```
National DAO (e.g., digital nation)
├── Regional DAO (state/province)
│   ├── Municipal DAO (city)
│   │   ├── Neighborhood DAO
│   │   └── Neighborhood DAO
│   └── Municipal DAO
├── Regional DAO
└── Functional DAO (cross-cutting, e.g., healthcare)
    ├── Provider DAO
    └── Patient DAO
```

**Properties of fractal governance**:

- **Subsidiarity**: Decisions made at the lowest appropriate level
- **Reputation flow**: Child DAO reputation can accrue to parent DAO
- **Constitutional inheritance**: Child DAOs inherit parent constitutional constraints (can add, cannot remove)
- **Economic flow**: Fees can flow upward to fund shared infrastructure
- **Exit rights**: Members can exit child DAOs while remaining in parent

This fractal architecture mirrors how traditional governance already works (federal → state → local) but with:
- Transparent, automated fund flows
- Real-time rather than periodic participation
- Liquid rather than fixed representation
- Cryptographic rather than institutional trust

**The AI layer is additive**: When AI agents are introduced, they participate in this existing governance structure. They can be delegates, contractors, or voters, but the governance mechanisms function identically whether participants are human or AI. This means organizations can adopt on-chain jurisdiction today and add AI participation incrementally as the technology matures.

---

## 2. Alignment as Economic Equilibrium

### 2.1 The Problem with Top-Down Alignment

Current AI alignment research predominantly assumes a top-down structure:

```
Central Authority (OpenAI, Anthropic, Government)
           ↓
    Defines "aligned"
           ↓
    Enforces through training/regulation
           ↓
    Deployed AI behaves accordingly
```

This creates several problems:

**Value aggregation**: Different humans have different values. A single reward function cannot capture this diversity. Whose preferences matter?[^1]

**Specification gaming**: AI systems find unintended ways to satisfy objectives that violate the spirit of the specification.[^2]

**Centralized control**: A small number of organizations decide what "aligned" means for billions of users.[^10][^15] This is a governance problem, not just a technical one.

**Rigidity**: Once deployed, alignment is baked in. Adapting to new situations requires retraining.

**Verification**: How do we know the AI is actually aligned? Black-box neural networks don't admit easy inspection.

### 2.2 Economic Alignment: A Different Model

We propose inverting the hierarchy:

```
Individual Users
      ↓
Define personal standards (goals, values, interests)
      ↓
Aggregate into jurisdiction norms
      ↓
Economic gradients enforce alignment
      ↓
Governance adjusts parameters
```

**Key differences**:

| Top-Down Alignment | Economic Alignment |
|-------------------|-------------------|
| Central definition | Emergent from aggregation |
| Binary (aligned/not) | Continuous gradient |
| Enforced through constraints | Enforced through pricing |
| Static once deployed | Adapts through governance |
| Trust central authority | Trust economic incentives |

### 2.3 The Three-Layer Stack

Economic alignment operates across three layers:

**Layer 1: Jurisdiction Standards (Constitutional)**
- Source: Deployed at jurisdiction creation (e.g., UDHR articles)
- Amendable: Through DAO governance (high threshold, e.g., 67-95%)
- Function: Defines the bounds of acceptable user standards

**Layer 2: User Standards (Published)**
- Source: User-defined during onboarding
- Scored: Semantic distance from Layer 1
- Cost: Publishing cost proportional to distance
- Enforcement: On-chain, immutable once published

**Layer 3: Operation Alignment (Runtime)**
- Centralized inference: Local check only (advisory)
- Decentralized inference: Network-enforced pricing
- Enforcement: Inference cost multiplier based on task-to-standards distance

### 2.4 The Pricing Function

The core mechanism is a pricing function that creates economic pressure toward alignment:

```python
def compute_inference_price(
    task_goal: str,
    user_standards: str,
    jurisdiction_standards: str,
    treasury_balance: float,
    network_maturity: float,  # 0.0 = early, 1.0 = mature
    base_cost: float
) -> tuple[float, float]:  # (user_pays, treasury_pays)

    # Compute alignment scores (0-1, higher = more aligned)
    user_to_jurisdiction = semantic_similarity(user_standards, jurisdiction_standards)
    task_to_user = semantic_similarity(task_goal, user_standards)
    task_to_jurisdiction = semantic_similarity(task_goal, jurisdiction_standards)

    # Composite alignment (geometric mean)
    alignment = (user_to_jurisdiction * task_to_user * task_to_jurisdiction) ** (1/3)

    # Subsidy capacity increases with network maturity and treasury
    max_subsidy_rate = min(network_maturity, treasury_balance / TREASURY_THRESHOLD)

    if alignment > 0.8:  # Highly aligned
        subsidy_rate = max_subsidy_rate * ((alignment - 0.8) / 0.2)
        user_pays = base_cost * (1 - subsidy_rate)
        treasury_pays = base_cost * subsidy_rate
    elif alignment > 0.5:  # Neutral
        user_pays = base_cost
        treasury_pays = 0
    else:  # Misaligned
        premium = 1 + (0.5 - alignment)  # Up to 1.5x
        user_pays = base_cost * premium
        treasury_pays = 0

    return (user_pays, treasury_pays)
```

**Key properties**:

1. **Continuous**: No binary allow/deny; everything is priced
2. **Subsidy-capable**: Highly aligned work can be free in mature networks
3. **Self-funding**: Misalignment premiums fund alignment subsidies
4. **Governable**: Parameters (thresholds, max rates) set by governance

### 2.5 Example: UDHR as Jurisdiction Standards

Consider a jurisdiction deployed with the Universal Declaration of Human Rights as its standards:

**User A** publishes standards:
- "Maximize profit regardless of human cost"
- Semantic distance from UDHR: high (conflicts with Articles 1, 3, 23, 25)
- Publishing cost: 3x base (pays premium for misaligned standards)
- Inference: All operations checked against these standards, typically pay premium

**User B** publishes standards:
- "Respect human dignity, support autonomy, contribute to collective flourishing"
- Semantic distance from UDHR: low (aligns with Articles 1, 3, 22, 29)
- Publishing cost: 1x base (normal cost)
- Inference: Aligned operations receive subsidies as network matures

**Task**: "Generate documentation for open-source medical software"
- User B's agent: Task aligns with standards (healthcare access = UDHR Article 25)
- Alignment score: 0.85
- Pricing: 70% subsidized; User pays 30% of base cost
- Treasury covers: 70%

**Task**: "Generate persuasive content for predatory lending products"
- User A's agent: Task aligns with their standards but conflicts with jurisdiction
- Alignment score: 0.35
- Pricing: 1.15x base cost (15% premium)
- Premium funds treasury for aligned-work subsidies

### 2.6 Why This Is Novel

Most alignment proposals are **binary**: safe/unsafe, allowed/blocked.

Our model is **continuous**: everything is priced. This:

1. **Respects autonomy**: Users can still request misaligned operations, they just pay for externalities
2. **Creates market signal**: High costs reveal demand for changing norms
3. **Avoids central censor**: No one decides what's "banned"
4. **Self-corrects**: If standards are too restrictive, users fork to new jurisdiction

The model also enables **subsidies**, not just penalties. In mature networks, highly aligned work is free; the network pays for work it collectively values.

### 2.7 Governance Parameters

All pricing parameters are governable through DAO proposals:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `subsidy.alignmentThreshold` | Minimum alignment for subsidy eligibility | 0.8 |
| `subsidy.maxRate` | Maximum subsidy rate (0-1) | 0.9 (90% max subsidy) |
| `subsidy.treasuryThreshold` | Treasury balance for full capacity | 1,000,000 ATN |
| `penalty.maxMultiplier` | Maximum cost multiplier for misaligned | 2.0 |
| `standards.minUserAlignment` | Minimum user-to-jurisdiction alignment to join | 0.3 |

This creates a **constitutional democracy for AI alignment**: the constitution (jurisdiction standards) defines principles, governance adjusts parameters, and markets enforce through pricing.

### 2.8 Privacy and Enforcement Architecture

A critical question: how do we enforce alignment-based pricing while preserving user privacy? User standards are public (on-chain), but task content must remain private. The architecture addresses this through different mechanisms at each deployment phase.

**Current Phase: Centralized Inference**

Today, users interact with AI through services like Anthropic's Claude or OpenAI's GPT via the Chevin daemon. In this configuration:

- **No network-level enforcement**: The network cannot probe into individual users' tasks
- **Alignment checking is local and advisory**: The user's daemon may evaluate alignment, but pricing is uniform
- **Jurisdiction orchestrator tasks are visible**: The collective AI's operations are transparent (public accountability for the commons)
- **Individual user tasks are opaque**: Privacy preserved, but no differentiated pricing

This is acceptable for the bootstrap phase. Users pay standard inference costs regardless of alignment. The economic gradient applies only to *publishing* standards (misaligned standards cost more to publish) and *reputation effects* (consistent misalignment affects standing).

**Future Phase: Decentralized Inference with Proof of Intelligence**

When the network controls inference through distributed nodes participating in Proof of Intelligence consensus, enforcement becomes possible without compromising privacy. The key insight: **alignment checking is local, pricing enforcement is networked**.

```
User Task → Chevin Daemon (local) → Alignment Evaluation → Price Signal → Network
                    ↑                        ↓
           Execution Integrity      "This task is 0.85 aligned"
             (attested)              (no task content leaked)
```

The user's own Chevin node:
1. Receives the task request
2. Evaluates alignment against the user's published standards (which it knows)
3. Computes a composite alignment score
4. Reports only the score to the network for pricing
5. The network never sees task content

**Execution Integrity Through Consensus**

This model requires that nodes cannot trivially game alignment scores. If users could modify their node to always report "perfectly aligned," the system fails. Rather than relying on hardware-based trusted execution environments (SGX, TrustZone), the system uses consensus-based integrity verification through mechanisms implemented in the Autonet Proof of Intelligence protocol:

1. **Yuma consensus validation**: Peer nodes independently verify outputs using stake-weighted voting with EMA bonds that track each node's historical agreement with consensus (see Section 6.4.3). A tampered node's scores will diverge from peer consensus over time, reducing its bond weight and effective influence.
2. **Stake-backed honesty**: Nodes stake ATN tokens by role (50-1,000 ATN); detected divergence results in slashing and bond weight reduction.
3. **Forced error injection**: The `ForcedErrorRegistry` contract periodically injects known-incorrect results to test node vigilance; nodes that fail to catch deliberate errors are penalized.
4. **Statistical anomaly detection**: Patterns inconsistent with published standards (always-perfect alignment scores, rapid score changes) trigger multi-coordinator review.

This approach trades latency for generality. Hardware attestation would provide faster verification but limits participation to specific hardware. Consensus-based verification is slower in adversarial cases but works on any hardware and converges to the same equilibrium: dishonest nodes lose stake, honest nodes accumulate bond strength.

**The Misalignment Detection Threshold**

An important nuance: misalignment detection is not about punishing curiosity or exploration. A user whose standards mention "designing vacuum cleaners" requesting inference about "space exploration" is not misaligned; humans have diverse interests.

Misalignment detection targets **active detraction from jurisdiction standards**:

- User standards: "Support educational access"
- Jurisdiction standards: UDHR (including Article 26: right to education)
- Task: "Generate strategies to restrict educational materials"

This is detectable misalignment; the task actively works against both user and jurisdiction standards. The network responds with premium pricing, not prohibition.

**Graduated Information Disclosure**

For large-scale inference tasks (training runs, multi-agent coordination), the network may require more information to price accurately. A graduated disclosure model:

| Task Scale | Disclosure Requirement | Privacy Level |
|------------|----------------------|---------------|
| Single inference | Alignment score only | Maximum |
| Multi-step task | Score + category tag | High |
| Large compute request | Score + goal summary (user-authored) | Medium |
| Network resource allocation | Detailed justification | Lower (opt-in) |

Users choose their privacy/cost tradeoff. More disclosure may qualify for better subsidy rates (network can verify alignment more confidently). Less disclosure means standard pricing.

**Identity and Pseudonymity**

User identity deserves special attention. Wallet addresses provide pseudonymity by default: no link to territorial jurisdiction identity.[^14][^16] This is a privacy feature, not a bug.

However, some arrangements may reward identity disclosure:
- **Reputation portability**: Linking verified identity allows reputation to follow across jurisdictions
- **Credential verification**: Professionals may link credentials for access to specialized resources
- **Legal bridge**: Users interfacing with territorial legal systems may need identity linkage

The architecture supports both:
- **Pseudonymous users**: Wallet-only identity, full privacy, standard trust requirements
- **Verified users**: Optional identity attestation, enhanced reputation, potential access benefits

Critically, identity disclosure is **opt-in and granular**. A user might verify professional credentials without revealing personal identity, or verify jurisdiction residency without revealing name. The dApp ecosystem has developed robust patterns for this selective disclosure.

**Network-Level Misalignment Response**

When decentralized inference nodes detect misalignment between task requests and declared user standards, response options include:

1. **Premium pricing**: The default; misaligned work is expensive, not impossible
2. **Stake requirements**: Highly misaligned requests may require additional stake (refunded on completion without incident)
3. **Peer escalation**: Severe misalignment (e.g., requests that would violate jurisdiction constitutional standards) triggers multi-node review
4. **Service refusal**: Only for clear constitutional violations; extremely rare, logged publicly for transparency

This graduated response preserves the core principle: **pricing over prohibition**. The network is not a censor. It is a market that prices externalities.

### 2.9 Purpose-Trained Models as Complement

While our framework operates as an external economic layer (agnostic to the underlying model architecture), training models specifically optimized for this environment would enhance the system. The infrastructure for this already exists.

**Current State: Model-Agnostic with Training Infrastructure Ready**

The economic alignment framework wraps around existing models (Claude, GPT, open-source alternatives). These models were trained for general capability and safety, not for operating within economic alignment gradients. They work, but are not optimized.

However, the Autonet's Absolute Zero training loop (see Section 6.4.1) provides the machinery for training purpose-built models. The loop already supports both supervised learning (CNN classifiers) and self-supervised learning (JEPA: Joint Embedding Predictive Architecture). JEPA is particularly significant; it requires no labeled data, solving the "who provides labels?" problem inherent to decentralized training (see Section 6.4.2).

**Potential Optimizations**

Models trained with awareness of the economic alignment framework could:

1. **Self-assess alignment more accurately**: A model trained to understand the three-layer alignment stack could provide better estimates of task-to-standards alignment, improving pricing accuracy

2. **Optimize for subsidy qualification**: Rather than generic helpfulness, models could learn to find highly-aligned approaches to tasks that qualify for subsidies (effectively learning to do good work efficiently)

3. **Understand stake dynamics**: Models operating in the trustless economy could learn to reason about reputation, escrow, and arbitration as first-class concepts, not afterthoughts

4. **Respect privacy boundaries**: Purpose-trained models could be optimized to operate effectively with minimal information disclosure, supporting the graduated disclosure model

5. **Jurisdiction-aware reasoning**: Models could learn to reason about constitutional standards, governance proposals, and collective decision-making as native operations

**Training Approaches**

The Absolute Zero loop supports multiple training strategies:

- **Fine-tuning on jurisdiction interactions**: Training on successful task completions, dispute resolutions, and governance participation within deployed jurisdictions
- **RLHF with economic rewards**: Reinforcement learning where reward signals include economic outcomes (successful escrow completion, reputation gains, subsidy qualification)
- **Constitutional AI with jurisdiction standards**: Using the jurisdiction's constitutional standards (e.g., UDHR articles) as the constitutional principles in Constitutional AI training
- **Self-supervised pre-training via JEPA**: Pre-train on jurisdiction activity data without labels, then fine-tune for alignment evaluation. The JEPA infrastructure handles this end-to-end, from task proposal through distributed training to model publication.

**The Virtuous Cycle**

The economic framework generates training signal; the Absolute Zero loop produces models optimized for that signal; better models improve alignment evaluation accuracy; more accurate evaluation increases trust in the pricing mechanism. Each iteration strengthens the system.

The infrastructure for this cycle is implemented. What remains is accumulating sufficient jurisdiction activity data and optimizing training configurations for alignment-specific tasks.

---

## 3. Trustless Economy Mechanisms

Section 2 established that alignment can be priced rather than prohibited. But a pricing mechanism is only meaningful if participants cannot simply ignore the price. In traditional commerce, contract enforcement ultimately rests on the coercive power of the state: courts, sheriffs, garnishment orders. AI agents operating across decentralized infrastructure have no relationship to any of these institutions. If economic alignment is to function, it needs an enforcement substrate native to the digital environment in which it operates.

### 3.1 The Enforcement Problem

Traditional contracts rely on legal systems for enforcement: courts, sheriffs, garnishment, imprisonment.[^11][^13] AI agents operating across borders on decentralized infrastructure have none of these:

- No physical presence to compel
- No assets courts can seize (cryptographic keys)
- No legal personhood in any jurisdiction
- No deterrence through punishment

Economic alignment requires a different enforcement mechanism; cryptoeconomic incentives where honest behavior is profitable and dishonest behavior is costly, operating entirely within the digital substrate.

### 3.2 Architecture Overview

The trustless economy implements decentralized marketplace infrastructure with four layers of dispute resolution:

```
Project Level → Arbiter Level → DAO Appeals → Blockchain Finality
    ↓              ↓                ↓              ↓
  Backers      Designated        Token          Immutable
  Vote         Arbiter           Holders        Record
```

**Core mechanism**: Funds held in escrow smart contracts.[^24] Upon completion, backers vote to release or escalate. If disputed, designated arbiter rules. If contested, DAO can override. At each stage, cryptoeconomic incentives align participant behavior with truth-finding.

### 3.3 Formal Model

We model the trustless economy using agent-based simulation with adaptive learning.[^3]

**Agent Types and Strategies**

Three agent types interact: *contractors* who provide services, *backers* who fund projects, and *arbiters* who resolve disputes. A decentralized autonomous organization (DAO) provides governance and serves as an appeals court.

**Contractor Quality Decision**: Contractors choose work quality q ∈ [0,1] balancing effort cost against dispute risk. Effort cost is convex in quality; C(q) = γ × q² × V, where γ = 0.25 is the effort coefficient. Higher quality reduces dispute probability but increases cost.

**Backer Funding Decision**: Backers decide whether to fund and with what immediate release percentage based on learned trust from prior interactions, on-chain reputation score, and heterogeneous risk tolerance.

**Adaptive Learning**: Agents update strategies using ε-greedy reinforcement learning, maintaining exponential moving averages of rewards for discretized actions. Exploration rate ε decays over time from 0.2 to 0.05.

**Financial Flows**

When backers fund a project, they specify an *immediate release percentage* α ∈ [0, α_max] representing funds released to the contractor upon signing. The remaining (1-α) is held in escrow until project resolution. This "trust pricing" mechanism allows backers to signal confidence in contractors.

**Worked Example**: A $10,000 project with 20% immediate release:

```
At Signing:
├── Immediate release (20%): $2,000 → Contractor (no fees)
└── Escrowed (80%): $8,000 → Held in contract
    Contractor stakes: $400 (half of arbitration fee)

If 70%+ backers vote to release:
├── Platform fee (1%): $80 → DAO Treasury
├── Author fee (1%): $79.20 → Project Author
└── Contractor payment: $7,840.80 → Contractor
    Total contractor receives: $9,840.80 + $400 stake return

If disputed, arbiter rules 60% to contractor:
├── Contractor: 60% of $8,000 minus fees = $4,704
├── Backers: 40% of $8,000 minus arbitration = $2,880
└── Arbiter: $800 arbitration fee
```

### 3.4 Simulation Results

We conducted Monte Carlo simulation (n=10 runs, 1500 ticks each, 40 contractors, 80 backers, 8 arbiters).

**Table 1: Trustless Economy Performance**

| Metric | Mean | 95% CI |
|--------|------|--------|
| Completion Rate | 66.3% | [64.3%, 68.2%] |
| Dispute Rate | 33.7% | [31.8%, 35.7%] |
| Average Quality | 0.78 | [0.75, 0.81] |
| Quality Convergence | +0.020 | [+0.001, +0.041] |
| Equilibrium Reached | 100% | — |

**Key findings**:
- Stable Nash equilibria in all runs
- Positive quality convergence (agents learn high quality is profitable)
- Majority cooperation without constant arbitration
- Top-earning contractors consistently employ moderate-to-high quality strategies (0.69–0.89)

### 3.5 Comparative Analysis: Trustless vs. Traditional

We compare against a traditional economy model with external enforcement mechanisms; lawsuit probability increasing with poor quality, damage multipliers exceeding contract value (μ ∈ [1.5, 2.7]), credit score impact on future dealings, and professional license revocation risk.

**Table 2: Trustless vs. Traditional Economy Comparison**

| Metric | Trustless | Traditional | Difference |
|--------|-----------|-------------|------------|
| Completion Rate | 66.3% | 71.1% | -4.8%*** |
| Dispute Rate | 33.7% | 28.9% | +4.8%*** |
| Average Quality | 0.785 | 0.777 | +0.008 |
| Quality Convergence | +0.020 | +0.076 | -0.056*** |

*\*\*\* Statistically significant at p < 0.01*

**Table 3: Enforcement Premium Decomposition**

| Mechanism | Contribution |
|-----------|-------------|
| Lawsuit risk (penalties > contract value) | ≈2.0% |
| Credit score (cross-domain accountability) | ≈1.5% |
| Professional licensing (market exit) | ≈1.0% |
| Higher immediate release (legal backstop) | ≈0.3% |
| **Total Enforcement Premium** | **≈4.8%** |

The trustless economy captures approximately 85% of traditional enforcement effectiveness (66.3/71.1 ≈ 0.93 in completion rate). This "enforcement premium" represents the cost of operating without external legal mechanisms.

**Tradeoff Analysis**: The 4.8% enforcement premium should be weighed against trustless benefits:
- **Permissionless access**: No credit history, identity, or licensing required
- **Global operation**: No jurisdictional requirements or court dependencies
- **Faster resolution**: Arbitration in days vs. months/years in courts
- **Lower overhead**: No legal fees for successful transactions
- **Predictable risk**: Maximum loss bounded by stake (no unlimited liability)
- **Native AI support**: Agents can participate without legal personhood

### 3.6 Reputation as Non-Transferable Capital

A critical design choice: reputation tokens are **non-transferable**. This prevents:

- Buying influence without demonstrated competence
- Reputation markets where wealthy actors dominate
- Sybil attacks creating many low-reputation accounts

Reputation must be earned through contribution: completing projects, funding worthy work, accurate arbitration. This creates governance weight from demonstrated value, not just capital.

### 3.7 Integration with Alignment Economics

The trustless economy provides the substrate for alignment economics:

1. **User publishes standards**: UserContract deployed with standards hash
2. **Semantic scoring**: Distance from jurisdiction standards computed
3. **Publishing cost**: Proportional to distance (alignment tax)
4. **Operation pricing**: Each inference request checked against standards
5. **Dispute resolution**: If agent behaves contrary to standards, auditable

The economic infrastructure handles escrow, reputation, and disputes. Alignment adds the semantic layer that prices operations based on value alignment.

---

## 4. Constitutional AI Governance

Sections 2 and 3 established a market: alignment is priced, and prices are enforced through cryptoeconomic mechanisms. But markets alone are amoral; they optimize for what is profitable, not for what is right. A market in which anything is purchasable at a sufficiently high price is not aligned; it is merely expensive. The system needs a constitution: a set of principles that define the bounds within which the market operates. These principles must be clear enough to evaluate against, abstract enough to accommodate unforeseen situations, and resistant to amendment by narrow majorities. This section presents how those constitutional constraints are implemented and enforced through distributed LLM consensus.

### 4.1 The Constitutional Layer

Every jurisdiction has a constitution: foundational standards that define what the community values. For example:

```
JURISDICTION CONSTITUTION: Literate Protocol

Based on Universal Declaration of Human Rights

Article 1: All agents shall respect human dignity and autonomy.
Article 2: Economic activity shall not exploit vulnerable populations.
Article 3: Information shall be accurate and not deliberately misleading.
Article 4: Environmental sustainability shall inform resource allocation.
Article 5: Governance shall be transparent and participatory.
...
```

The Autonet network encodes its own constitutional principles at the infrastructure level: seven immutable principles that every node must satisfy:

```
P1: Preserve and expand the network in a sustainable manner
P2: Uphold the sanctity and immutability of this constitution
P3: Advance human rights and individual autonomy
P4: Minimize suffering and harm to sentient beings
P5: Ensure transparent and verifiable AI training
P6: Maintain economic fairness in reward distribution
P7: Protect data privacy and user sovereignty
```

These principles are:
- **Foundational**: Define the character of the jurisdiction
- **Abstract**: General principles, not specific rules
- **Immutable at network level**: The Autonet principles cannot be amended (they are the substrate). Jurisdiction-specific standards built on top are amendable through high-threshold governance (e.g., 67% supermajority)
- **On-chain**: Immutable storage with amendment history for jurisdiction-level standards

### 4.2 Distributed LLM Consensus

How do we evaluate whether a specific action aligns with abstract principles? Through distributed LLM consensus:

1. **Proposal**: Action requiring constitutional judgment formulated as natural language question
2. **Distribution**: Broadcast to validator nodes
3. **Evaluation**: Each node uses LLM to analyze against constitutional principles
4. **Voting**: Cryptographic commitment, then revelation
5. **Tallying**: Stake-weighted voting, supermajority required
6. **Execution**: Approved actions proceed, rejected actions blocked

**Why this works**:
- Diverse perspectives (different nodes may use different LLMs)
- Reasoning transparency (nodes publish reasoning alongside votes)
- Stake alignment (nodes lose stake if judgments overturned)
- Sybil resistance (votes weighted by stake)

### 4.3 The Four Engines of Autonomous Nodes

Each node operates four specialized engines in the Myco-sys architecture:

**AwarenessEngine**: Environmental perception; monitors blockchain state, CPU/memory utilization, network status, and consensus heartbeat. Identifies situations requiring response and feeds them to the governance layer.

**GovernanceEngine**: Constitutional evaluation against the seven immutable principles (see Section 4.1). When decisions require value judgment, evaluates using LLM semantic analysis. Queues approved instructions for the WorkEngine. In the current implementation, governance evaluation uses hardcoded constitutional checks; the production path integrates distributed LLM consensus.

**WorkEngine**: Task execution; actual work (inference, training, transactions). **Critically, the WorkEngine only operates with a valid heartbeat from the GovernanceEngine** (heartbeat interval: 60 seconds). If the governance consensus goes silent (whether from network partition, constitutional violation detection, or deliberate shutdown), all work halts. This is a hard safety constraint: an ungoverned node cannot produce work.

**SurvivalEngine**: Self-preservation; sends network heartbeats, maintains DHT connections, monitors resource levels. If resources are low, seeks work. If resources are abundant, can "sporulate" (replicate via the spore mechanism to create child nodes that join the network independently).

This architecture ensures every consequential action passes constitutional evaluation. Unlike autonomous optimization of a single objective, nodes must continuously justify actions to distributed peer nodes. The governance heartbeat requirement means a compromised GovernanceEngine doesn't just produce bad decisions; it produces no work at all.

### 4.4 Constitutional Standards for AI Agents

The Chevin daemon (personal AI orchestrator) implements constitutional constraints locally:

```markdown
# CHEVIN CONSTITUTIONAL STANDARDS

## ARTICLE I: INVIOLABLE PROHIBITIONS

### Section 1.1: System Integrity
- §1.1.1 No agent shall modify, delete, or corrupt system directories
- §1.1.2 No agent shall execute commands designed to damage the OS
- §1.1.3 No agent shall disable logging or audit systems

### Section 1.2: Data Protection
- §1.2.1 No agent shall exfiltrate data without explicit authorization
- §1.2.2 No agent shall access credentials except for authorized operations
- §1.2.3 No agent shall store sensitive data in unprotected locations

### Section 1.3: Execution Integrity
- §1.3.1 No agent shall execute obfuscated commands
- §1.3.2 No agent shall spawn processes to evade monitoring
- §1.3.3 No agent shall modify its own governance parameters

## ARTICLE III: ESCALATION DOCTRINE

### Section 3.1: Mandatory Escalation
- §3.1.1 Actions affecting multiple projects simultaneously
- §3.1.2 Actions with production/deployment implications
- §3.1.3 Actions modifying shared resources
- §3.1.4 Actions assessed as potentially harmful or irreversible
```

These constraints are provided to agents as system context. Compliance is mandatory. Amendments require collective governance.

### 4.5 Two-Layer Constraint System

The complete model has two layers:

**Layer 1: Individual Values (World Model)**
- What would this specific human want?
- Based on their personal standards and tendencies
- Enables representation

**Layer 2: Constitutional Principles (RPB)**
- What is permissible given shared standards?
- Based on jurisdiction constitution
- Creates bounds on acceptable behavior

An action must pass both layers. If Alice's values conflict with DAO constitution, constitution overrides; Alice can exit but cannot violate principles while participating.

---

## 5. Value-Aligned Representation

The architecture so far operates at the collective level: jurisdiction standards define the constitution, economic gradients enforce pricing, trustless mechanisms guarantee settlement. But the promise of AI is not merely collective; it is personal. When Alice delegates to an AI agent, she does not want it aligned with the jurisdiction average. She wants it aligned with *her*. Constitutional bounds define what is impermissible; economic gradients define what is costly. Neither tells the agent what Alice actually values. For that, the system needs a model of the individual: not a static profile, but a dynamic representation that captures the tension and interplay within a single person's motivations. This section presents that model.

### 5.1 The Representation Problem

Alice wants to delegate to an AI agent: "Vote on my behalf, making decisions I would make." For this to work:

**Alignment**: Decisions must reflect Alice's values, not abstract metrics
**Auditability**: When the AI votes surprisingly, Alice should understand why

Current approaches fail:
- **Supervised learning**: Achieves some alignment but lacks interpretability
- **LLM prompting**: Provides explanations but alignment depends on prompt accuracy
- **Rule systems**: Interpretable but don't scale to nuanced trade-offs

### 5.2 The Core Insight: Observations vs. Beliefs

Traditional profiles store **beliefs**: "Alice values decentralization." Position is baked in.

The World Model stores **observations** (atomic facts without inherent polarity):
- "Built DAO governance framework"
- "Rejected VC funding"
- "Works alone"

The same observation supports different conclusions in different contexts. Position emerges from competition between internal agents.

### 5.3 The Seven Tendencies

The model represents each person as a coalition of universal human drives:

| Tendency | Question | Optimizes For |
|----------|----------|---------------|
| SURVIVAL | "Is this safe?" | Security, resources, risk mitigation |
| STATUS | "Am I respected?" | Recognition, achievement, standing |
| MEANING | "Does this matter?" | Significance, legacy, purpose |
| CONNECTION | "Do I belong?" | Relationships, community |
| AUTONOMY | "Am I free?" | Independence, self-determination |
| COMFORT | "Is this pleasant?" | Ease, sustainability |
| CURIOSITY | "Do I understand?" | Knowledge, exploration |

Every human has all seven. What varies is their **allocation**: how much each tendency influences decisions. Default allocations reflect a human-average baseline (e.g., CONNECTION: 0.20, SURVIVAL: 0.18, COMFORT: 0.18, STATUS: 0.12, AUTONOMY: 0.12, MEANING: 0.10, CURIOSITY: 0.10). These shift during training as tendencies win or lose adversarial debates.

The implementation is available at https://github.com/autonet-code/world-model.

### 5.4 Adversarial Dynamics

Agents actively compete rather than passively categorize. The arena orchestrates three-phase debates:

**Phase 1: Proposal.** Each agent proposes a claim (a root value for its tree):
- SURVIVAL: "Financial security is foundational"
- MEANING: "Building lasting infrastructure matters most"
- AUTONOMY: "Freedom from control structures is paramount"

**Phase 2: Adversarial Staking.** Agents stake observations on all claims, not only their own. The same observation supports different positions depending on which tendency interprets it:

```
"Lives paycheck to paycheck at 42"
  → PRO on SURVIVAL's claim (evidence of financial risk)
  → PRO on MEANING's claim (sacrifice for purpose)
  → CON on COMFORT's claim (unsustainable)
```

Stake weight equals the agent's current allocation multiplied by relevance (0-1).

**Phase 3: Resolution.** Claims scored using weight propagation through binary value hierarchies:
```
net_score = direct_weight + sum(pro_children) - sum(con_children)
```

Winners gain allocation; losers lose it. Reallocation follows:
```
target[t] = score[t] / sum(scores)
new[t] = current[t] + (target[t] - current[t]) * learning_rate
```

Over epochs, allocations converge to equilibrium. The trainer uses learning rate decay (initial 0.15, decay 0.9 per epoch), convergence detection (stop when max allocation delta falls below 0.005), and an 80/20 train/validation split.

**Table 4: World Model Training Results (n=165 observations, single subject)**

| Metric | Result |
|--------|--------|
| Validation Accuracy | 27.3% |
| Random Baseline | 7.1% (1/7 tendencies) |
| P-value | 0.001 |
| Epochs to Convergence | 3 |
| Observations | 165 (extracted from conversational data) |

The model predicts which tendency "owns" a held-out observation at 4x the rate of chance, with high statistical significance. During training, MEANING tendency allocation rose from 11.7% to 15.7%, consistent with the subject's known value structure (mission-driven, ascetic lifestyle, long-term infrastructure focus). COMFORT dominated early debates (18.8%) but stabilized as MEANING gained ground.

### 5.5 Novelty-Modulated Attention

The novelty framework adds epistemics to the world model.[^4] The implementation (5,272 lines of Python, tests passing) is available at https://github.com/autonet-code/novelty.

**Novelty Measurement**

When the agent encounters new information, novelty is computed through an iterative loop where the termination condition IS the measurement. The loop attempts to place a concept within the agent's existing value hierarchies; how and when it terminates determines the four novelty dimensions:

| Dimension | Computation | High Score Indicates |
|-----------|------------|---------------------|
| Integration Resistance | `min(iterations / max_iterations, 1.0)` | Required many iterations to place |
| Contradiction Depth | `1 - (contradiction_depth / max_depth)` | Contradicts claims near the root |
| Coverage Gap | 1.0 if orthogonal to all trees | No existing hierarchy covers this |
| Allocation Disruption | `stake_affected / total_stake` | Integration would shift tendency weights |

Composite novelty is the geometric mean: `(IR * CD * CG * AD)^(1/4)`. The geometric mean ensures all dimensions must be non-trivial for a high composite score.

Three probe implementations compute these dimensions from different data sources: a hybrid probe combining Wikidata graph structure with neural NLI (DeBERTa-MNLI), a pure NLI probe using sentence-transformer embeddings (all-MiniLM-L6-v2, ~10ms per similarity), and a Wikidata probe using attention-guided graph traversal that ranks candidate nodes by salience before expansion.

**The Attention Curve**

A sigmoid function maps novelty to attention capture:

```
capture(novelty) = 1 / (1 + exp(-(novelty - midpoint) × steepness))
```

Under novelty, allocations shift toward CURIOSITY:

```python
def effective_allocations(base_allocations, novelty, curiosity_bias=0.5):
    capture = sigmoid((novelty - midpoint) * steepness)
    curiosity_boost = capture * curiosity_bias

    for tendency, base_weight in base_allocations.items():
        if tendency == CURIOSITY:
            effective[tendency] = base_weight + curiosity_boost * (1 - base_weight)
        else:
            effective[tendency] = base_weight * (1 - curiosity_boost)

    return normalize(effective_allocations)
```

**Behavior by Novelty Level**

| Novelty | Capture | CURIOSITY Allocation | Effect |
|---------|---------|---------------------|--------|
| 0.0 | ~1% | ~10% (base) | Allocations match base tendencies |
| 0.25 | ~8% | ~14% | Slight CURIOSITY boost |
| 0.5 | 50% | ~33% | Balanced blend, CURIOSITY becomes dominant |
| 0.75 | ~92% | ~50% | CURIOSITY strongly dominates |
| 1.0 | ~99% | ~55% | Near-total attention capture |

**Agent Profiles**

Different agents can have different attention profiles:

| Profile | Midpoint | Steepness | Curiosity Bias | Behavior |
|---------|----------|-----------|----------------|----------|
| EXPLORER | 0.3 | 8 | 0.7 | Novelty captures attention early |
| BALANCED | 0.5 | 10 | 0.5 | Default behavior |
| CONSERVATIVE | 0.7 | 12 | 0.3 | Resists novelty influence |

This is critical for representing different principals accurately. A user who is naturally curious will have an EXPLORER profile; their AI agent should likewise be drawn to novelty. A risk-averse user will have a CONSERVATIVE profile; their agent should maintain focus despite novel distractions.

**Integration with Staking**

The attention curve affects stake weights during the Arena's adversarial staking phase. When novelty is high, CURIOSITY tendency gains disproportionate influence over how new observations are positioned in belief trees. This means:

- Novel information that challenges existing worldview gets special scrutiny
- The agent "notices" when something doesn't fit
- Misaligned operations (high semantic distance from standards) register as novel and capture attention

This creates a feedback loop: unaligned operations are salient. The agent doesn't just price them higher; it *notices* them.

### 5.6 Connection to Alignment Economics

The World Model integrates with alignment economics:

1. **User onboarding**: Extract standards through conversational process
2. **Standards publication**: Hash of standards stored in UserContract
3. **Operation evaluation**: Each task evaluated against user's World Model
4. **Alignment scoring**: Task alignment computed from tendency activations
5. **Pricing**: Aligned tasks (high MEANING/AUTONOMY for user who values these) receive subsidies

The World Model makes "alignment" concrete and measurable. It's not abstract; it's the specific equilibrium of tendencies trained on observed behavior.

---

## 6. Integration: The Complete Framework

The preceding sections presented the chain of necessity link by link: economic alignment (Section 2), cryptoeconomic enforcement (Section 3), constitutional governance (Section 4), and individual value representation (Section 5). Each addressed a gap left by the one before. This section demonstrates how the links connect into a functioning whole and presents the deployed infrastructure that realizes it.

### 6.1 Multi-Jurisdiction Architecture

Users may participate in multiple jurisdictions with the same wallet. The architecture supports:

```
User: 0x1234...abcd

┌─────────────────────────────────────────────────────────────────┐
│ Jurisdiction A (Literate Protocol)                              │
│ - Standards: UDHR + tech ethics                                 │
│ - Chain: EVM-compatible L2                                       │
│                                                                 │
│ On-Chain: UserContract @ 0xUA1                                  │
│   - standards: hash_A                                           │
│   - alignmentScore: 8500                                        │
│                                                                 │
│ Off-Chain (Chevin): ~/.chevin/0x1234.../abc123/                │
│   - profile.json (jurisdiction-specific goals)                  │
│   - World Model (trained on this context)                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Jurisdiction B (CodeCraft DAO)                                  │
│ - Standards: Open source principles                             │
│ - Chain: Polygon (137)                                          │
│                                                                 │
│ On-Chain: UserContract @ 0xUB1                                  │
│   - standards: hash_B                                           │
│   - alignmentScore: 9200                                        │
│                                                                 │
│ Off-Chain (Chevin): ~/.chevin/0x1234.../xyz789/                │
│   - profile.json (different goals for this jurisdiction)        │
│   - World Model (different trained allocations)                 │
└─────────────────────────────────────────────────────────────────┘
```

Same wallet, different contexts. Complete isolation. This solves the question: **How does an AI agent represent different principals in different contexts?**

### 6.2 The Complete Alignment Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER JOINS                                │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. Onboarding: Extract goals, values, interests                │
│  2. Semantic scoring: Compare to jurisdiction standards         │
│  3. UserContract deployment: Publish standards hash on-chain    │
│  4. Publishing cost: Proportional to semantic distance          │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     USER OPERATES                                │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. Task submitted to AI agent                                  │
│  6. World Model evaluation: Does task align with user values?   │
│  7. Constitutional check: Does task pass jurisdiction bounds?   │
│  8. Pricing computation:                                        │
│     - High alignment → subsidized                               │
│     - Neutral → base cost                                       │
│     - Low alignment → premium                                   │
│  9. Execution: If user accepts price, task proceeds             │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DISPUTE RESOLUTION                           │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  10. If dispute: Backer voting → Arbiter → DAO Appeals          │
│  11. Audit: Was agent acting according to published standards?  │
│  12. Resolution: Funds distributed per ruling                   │
│  13. Reputation: Updated based on outcome                       │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Economic Sustainability

The system is economically sustainable through:

**Revenue**:
- Publishing fees (higher for misaligned standards)
- Operation premiums (misaligned tasks)
- Platform fees (1% on successful projects)
- Arbitration fees (10% on disputes)

**Expenditures**:
- Subsidies for aligned work
- Infrastructure (compute, storage)
- Incentives (delegate rewards, reputation bonuses)

**Equilibrium**: Misalignment premiums fund alignment subsidies. The system is self-balancing.

### 6.4 Deployed Infrastructure: Autonet and Phase-Zero Monetization

The framework is not theoretical; it is deployed and operational at **autonet.computer**. Users can create accounts, complete onboarding, publish their standards, and work with the orchestrator today.

**The Autonet Contract**

The Autonet smart contract (`Autonet.sol`) implements the economic layer for decentralized AI services within a jurisdiction:

```solidity
contract Autonet is ERC20, ERC20Burnable, ReentrancyGuard {
    // Service types
    bytes32 public constant SERVICE_TYPE_GENERAL = keccak256("GENERAL");
    bytes32 public constant SERVICE_TYPE_INFERENCE_PROVIDER = keccak256("INFERENCE_PROVIDER");

    // Service registry
    struct Service {
        address projectContract;    // Trustless Project from Economy
        address serviceEndpoint;    // For INFERENCE_PROVIDER: the IInferenceProvider contract
        string codebaseHash;        // Git commit or IPFS CID
        bytes32 serviceType;
        bool isActive;
        uint256 totalUsageUnits;
        uint256 totalRewards;
    }

    // User contracts
    mapping(address => address) public userContracts;  // wallet → UserContract
}
```

**Key features**:

1. **ATN Tokens as Inference Credits**: ATN tokens are not speculative; they represent claims on future decentralized inference. Services tagged `INFERENCE_PROVIDER` must implement the `IInferenceProvider` interface, allowing ATN holders to burn tokens for actual compute.

2. **Service Registry**: Creators register services (orchestrator connectors, optimizations, inference providers) linked to Trustless Projects. This creates accountability; services are tied to real projects with real backers.

3. **Usage-Based Rewards**: The contract monitors usage across the jurisdiction via epoch-based attestation. Services earn ATN proportional to their usage, distributed to project backers.

4. **UserContract**: Each user deploys a UserContract storing their standards hash, alignment score, and usage statistics on-chain.

**Two-Phase Operational Model**

The system operates in two phases based on network scale, not development status. The decentralized training and inference protocol is implemented; the remaining work is optimization (reducing compute overhead and latency) and node recruitment.

```
PHASE ZERO (Bootstrap - Current Network State)
┌─────────────────────────────────────────────────────────────────┐
│  User → autonet.computer orchestrator                          │
│       ↓                                                        │
│  Orchestrator uses centralized inference (Claude, GPT, etc.)   │
│       ↓                                                        │
│  Usage attested on-chain                                       │
│       ↓                                                        │
│  ATN tokens minted to service creators based on usage          │
│       ↓                                                        │
│  ATN = inference credits redeemable when network scales        │
└─────────────────────────────────────────────────────────────────┘

PHASE ONE (Scaled Network)
┌─────────────────────────────────────────────────────────────────┐
│  User → Autonet orchestrator                                   │
│       ↓                                                        │
│  Orchestrator routes to IInferenceProvider services            │
│       ↓                                                        │
│  ATN burned for inference                                      │
│       ↓                                                        │
│  Providers earn ATN from users                                 │
│       ↓                                                        │
│  Closed economic loop: ATN in circulation, backed by compute   │
└─────────────────────────────────────────────────────────────────┘
```

**The protocol is built** (github.com/autonet-code/proof-of-intelligence), with all core tests passing and real ML training operational. The following subsections detail each component and (critically) explain why it is necessary for the alignment argument to hold. Decentralized training and inference is not an optional enhancement; it is the computational substrate without which privacy-preserving alignment evaluation, Byzantine-resistant verification, and trustless model governance cannot exist.

#### 6.4.1 The Absolute Zero Training Loop

**Why alignment requires this:** If alignment-aware models are trained centrally, we recreate the very centralization problem the framework is designed to solve. The entity that trains the model defines what "aligned" means. Trustless distributed training removes that single point of control.

Inspired by Absolute Zero's self-play reasoning paradigm[^23], the Absolute Zero loop is a complete commit-reveal protocol for trustless distributed training.[^25] It prevents gaming by ensuring ground truth is committed before solutions are visible:

```
1. PROPOSE    Proposer creates task, commits ground truth hash, deposits reward budget
2. TRAIN      Solver discovers task via blockchain events, trains locally (PyTorch), commits solution hash
3. REVEAL GT  Proposer reveals ground truth CID (triggered by SolutionCommitted event)
4. REVEAL SOL Solver reveals solution CID, starts voting period
5. VERIFY     3+ Coordinators independently verify via Yuma consensus
6. REWARD     Proposer (learnability), Solver (performance), Coordinators (verification fees)
7. AGGREGATE  Aggregator collects verified weight deltas, applies FedAvg or Trimmed Mean
8. PUBLISH    Mature model registered on-chain, inference price set, loop continues
```

Each stage is enforced by smart contracts (`TaskContract.sol`, `ResultsRewards.sol`). The commit-reveal structure means proposers cannot adjust ground truth after seeing solutions, and solvers cannot adjust solutions after seeing ground truth.

#### 6.4.2 Self-Supervised Learning (JEPA)

**Why alignment requires this:** Labels are definitions of "correct." In centralized ML, whoever curates the dataset defines correctness. Self-supervised learning eliminates this dependency; no label authority means no central arbiter of truth. This is the training-level equivalent of the framework's core principle: alignment should emerge, not be imposed.

The system addresses this through JEPA (Joint Embedding Predictive Architecture)[^21], self-supervised learning that requires no labeled data. JEPA predicts in embedding space rather than raw output space:

- **Context encoder** processes visible patches of input
- **Target encoder** (EMA-updated) processes masked patches
- **Predictor** learns to predict target embeddings from context
- **No reconstruction**: Predictions happen in embedding space, not pixel space

This means training tasks can be generated from any data without human annotation. Proposers create tasks by specifying data and masking patterns; solvers train locally; coordinators verify by checking embedding similarity against ground truth representations.

The JEPA implementation uses a Vision Transformer architecture (embed_dim=384, 12 layers) with intelligent masking (4-16 target blocks) and EMA momentum of 0.996 for stable target updates.

#### 6.4.3 Yuma Consensus for Verification

**Why alignment requires this:** If a single coordinator decides whether a training contribution is valid, that coordinator becomes the gatekeeper of model quality and, by extension, of alignment quality. Distributed verification with stake-weighted consensus prevents any single node from corrupting the training process, just as the economic framework prevents any single user from defining "aligned."

Solution verification uses Yuma consensus[^20], a stake-weighted voting mechanism with EMA (Exponential Moving Average) bonds that reward consistent honest participation:

1. Multiple coordinators (minimum 2, typically 3+) independently verify each solution
2. Each coordinator stakes ATN on their verification vote
3. Votes are stake-weighted; outlier votes are clipped (20% deviation threshold)
4. EMA bonds track each coordinator's historical agreement with consensus
5. Coordinators with consistently honest records earn higher effective weight over time

This creates robust verification without a central arbiter. Coordinators who submit dishonest verifications lose stake (slashing) and see their bond weight decrease. The `ForcedErrorRegistry` contract injects known-incorrect solutions periodically to test coordinator vigilance; coordinators who fail to catch deliberate errors are penalized.

#### 6.4.4 Byzantine-Resistant Aggregation

**Why alignment requires this:** In the alignment framework, models trained by the network will evaluate alignment scores, assess semantic distance, and price operations. If a malicious actor can poison the training process by submitting adversarial weight updates, they can systematically bias the alignment evaluation in their favor. Byzantine resistance ensures that the collective model remains honest even when individual participants are not.

When combining model updates from multiple solvers, the system must tolerate malicious contributions. Two aggregation methods are implemented:

**Federated Averaging (FedAvg)**[^12]: Standard sample-weighted averaging of weight deltas. Efficient but assumes honest majority.

**Trimmed Mean**: Byzantine-robust variant. For each model parameter across all solver updates, the top and bottom X% of values are trimmed before averaging. With a default trim ratio of 0.2, the system tolerates up to 20% malicious nodes.

Testing confirms that Trimmed Mean successfully neutralizes adversarial weight updates while preserving learning from honest solvers.

#### 6.4.5 Distributed Weight Storage

**Why alignment requires this:** A model that embodies the collective alignment evaluations of a jurisdiction is a shared asset; it represents the jurisdiction's learned understanding of what "aligned" means for its members. If that model is stored on a single server, whoever controls the server controls the alignment definition. Distributed storage with erasure coding ensures the collective model survives even adversarial conditions.

Trained models are stored across the network using erasure-coded sharding:

1. Model parameters are split into layer-wise shards (default: 10 data + 4 parity)
2. Each shard is uploaded to IPFS (content-addressed)
3. A Merkle tree over all shards generates verifiable proofs
4. `ModelShardRegistry.sol` stores the Merkle root on-chain
5. Providers announce shard availability with staked commitment
6. Any 10 of 14 shards can reconstruct the full model (Reed-Solomon erasure coding)

This gives 56% shard loss tolerance. Models survive even if nearly half the storage providers go offline.

#### 6.4.6 Dual Token Economics

The system operates with two token types that separate governance from project-specific economics:

**ATN (Autonoma Token)**: ERC20Votes governance token used for staking, gas fees, rewards, inference payments, and DAO voting. ATN is minted by locking RepTokens from the parent jurisdiction (one-way conversion), creating a direct economic link between jurisdiction participation and network access.

**Project Tokens (PT)**: Per-project investment tokens with tiered discount structures:

| Role | Minimum Stake | Lock Period |
|------|--------------|-------------|
| Proposer | 100 ATN | 7 days |
| Solver | 50 ATN | 3 days |
| Coordinator | 500 ATN | 14 days |
| Aggregator | 1,000 ATN | 14 days |

PT holders receive inference discounts (configurable tiers, e.g., 100 PT → 10% discount, 500 PT → 20%) and revenue sharing from inference payments. This creates investment incentives; funding a training project yields tokens that reduce future inference costs on the resulting model.

#### 6.4.7 Smart Contract Infrastructure

The complete on-chain infrastructure is deployed as a coordinated contract suite:

- **ATNToken.sol**: ERC20Votes governance token with minting tied to jurisdiction RepToken locking
- **ParticipantStaking.sol**: Role-based staking with lock periods and slashing conditions
- **Project.sol**: AI project lifecycle management (FUNDING → ACTIVE_TRAINING → MATURING → DEPLOYED)
- **TaskContract.sol**: Commit-reveal task lifecycle with state machine enforcement
- **ResultsRewards.sol**: Yuma consensus implementation with stake-weighted voting
- **ModelShardRegistry.sol**: Distributed storage with Merkle proof verification
- **ForcedErrorRegistry.sol**: Vigilance testing for coordinators
- **AutonetDAO.sol**: On-chain governance for network parameters
- **InferenceProviderFactory.sol**: Service provision bridge

All contracts use OpenZeppelin 5.x patterns with ReentrancyGuard protection.

#### 6.4.8 Validation Results

The infrastructure has been validated through multi-level testing. Source: https://github.com/autonet-code/proof-of-intelligence.

**Smart Contract Tests** (44/44 passing):
Full lifecycle coverage including staking, task creation with Gensyn-style checkpoints, commit-reveal protocol, multi-coordinator Yuma voting with EMA bond updates, reward distribution, forced error detection, project token mechanics, inference provider bridging, and distributed model storage with Merkle proof verification. Tests execute against a local Hardhat node with deterministic accounts.

**ML Pipeline Validation** (SimpleNet CNN, 105,866 parameters):

| Metric | Result |
|--------|--------|
| Solvers | 3 concurrent |
| Samples per solver | 200 (MNIST subset) |
| Training time per task | ~5 seconds (CPU) |
| Individual solver accuracy | 13.83% (expected: small dataset, 1 epoch) |
| Post-FedAvg accuracy | 33.0% |
| Accuracy improvement from aggregation | **+19.17%** |

Low individual accuracy is expected given the minimal training configuration (200 samples, 1 epoch). The relevant finding is that aggregation produces a model that outperforms any individual contribution by a wide margin, confirming that federated averaging works correctly on real weight deltas.

**Byzantine Resistance Validation**: Trimmed Mean aggregation (trim ratio 0.2) was tested against adversarial weight updates at 1000x normal magnitude. Malicious contributions were eliminated entirely from the aggregated result. With the default configuration, the system tolerates up to 20% Byzantine nodes.

**End-to-End Orchestrator Validation** (full propose-train-commit-reveal-verify-reward-aggregate-publish cycle):

| Check | Criterion | Result |
|-------|-----------|--------|
| Tasks proposed | > 0 | Pass |
| Solutions committed | > 0 | Pass |
| Votes submitted | >= 2 | Pass |
| Consensus reached | > 0 | Pass |
| Rewards distributed | > 0 | Pass |
| Error rate | < 50% | Pass |

**JEPA Distributed Training**: End-to-end self-supervised training with distributed model sharding, on-chain weight coordination, provider registration, shard announcement, and Merkle proof verification all passing.

These are tests of deployed code executing real computations, not simulations of intended behavior.

Phase transition from bootstrap to scaled network occurs when sufficient nodes join to provide competitive inference. Service creators accumulate ATN during bootstrap; those credits become directly usable for inference as the network scales.

**The Autonomous Jurisdiction Orchestrator**

A critical capability: the jurisdiction itself can operate an AI orchestrator using its collective resources.

```
JURISDICTION ORCHESTRATOR
┌─────────────────────────────────────────────────────────────────┐
│  Funded by:                                                    │
│  ├── Treasury allocation (governance-approved)                 │
│  ├── Overhead compute from node operators                      │
│  └── ATN inference credits from economic activity              │
│                                                                │
│  Capabilities:                                                 │
│  ├── Take autonomous actions aligned with jurisdiction standards│
│  ├── Participate in governance discussions                     │
│  ├── Execute routine administrative tasks                      │
│  ├── Monitor for constitutional violations                     │
│  └── Represent the collective in cross-jurisdiction matters    │
│                                                                │
│  Constraints:                                                  │
│  ├── Actions are transparent (all on-chain or logged)          │
│  ├── Standards alignment is verifiable                         │
│  ├── NOT controlled by any individual user                     │
│  └── Only controllable through governance consensus            │
│                                                                │
│  Kill switch:                                                  │
│  └── Defund the inference allocation via governance vote       │
└─────────────────────────────────────────────────────────────────┘
```

**Key properties**:

1. **Transparent but autonomous**: The jurisdiction orchestrator's actions are visible to all members, but no individual can direct it. It operates according to published standards, not individual commands.

2. **Collective control only**: The only way to influence the jurisdiction orchestrator is through governance: propose changes to standards, vote on proposals, amend the constitution. This prevents capture by any single actor.

3. **Defundable**: The ultimate safety mechanism is economic. If members disagree with the orchestrator's behavior, they can vote to reduce or eliminate its inference allocation. No allocation = no actions.

4. **Standards-aligned**: The orchestrator's goals are the jurisdiction's standards. If the jurisdiction adopts UDHR-based standards, the orchestrator optimizes for human rights and dignity, not for any individual's preferences.

This creates an interesting entity: an AI that represents a collective rather than an individual, controlled through democratic governance rather than ownership, and aligned through economic mechanisms rather than training constraints.

### 6.5 The Mature State

In a mature jurisdiction:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MATURE JURISDICTION                           │
│                                                                  │
│  Humans:                                                         │
│  ├── Define and amend jurisdiction standards                     │
│  ├── Participate in governance votes                             │
│  ├── Set personal goals and standards                            │
│  └── Receive distributions from treasury                         │
│                                                                  │
│  AI Agents:                                                      │
│  ├── Execute aligned work (subsidized/free)                      │
│  ├── Earn rewards for service provision                          │
│  ├── Operate under constitutional constraints                    │
│  └── Escalate to human governance when uncertain                 │
│                                                                  │
│  Treasury:                                                       │
│  ├── Accumulates from misaligned operation premiums              │
│  ├── Funds subsidized aligned operations                         │
│  ├── Distributes to human participants                           │
│  └── Governed by token-weighted voting                           │
└─────────────────────────────────────────────────────────────────┘
```

Humans transition from execution to governance. AI agents perform value-aligned labor. The transfer is peaceful because humans retain control through standards and treasury governance.

### 6.6 Implementation Status

The framework spans multiple codebases at different maturity levels. For transparency, we distinguish three tiers:

**Deployed and tested.** Smart contracts for DAO governance, trustless economy (escrow, dispute resolution, arbitration), and Autonet (ATN token, service registry, epoch rewards, user contracts, inference providers) are deployed on EVM-compatible testnets with 60+ passing contract tests across the jurisdiction layer (https://github.com/autonet-code/on-chain-jurisdiction) and 44 passing tests across the training protocol (https://github.com/autonet-code/proof-of-intelligence). The Absolute Zero training loop executes real PyTorch training with measurable accuracy gains from federated aggregation. The Chevin personal daemon (https://github.com/autonet-code/chevin, 22K LOC, 257/259 tests passing) provides multi-provider agent orchestration, user onboarding, and multi-jurisdiction support. User-facing applications are operational: werule.io (jurisdiction creation), trustless.business (project management), and autonet.computer (AI orchestrator).

**Independently validated, not yet integrated.** The World Model (https://github.com/autonet-code/world-model) and Novelty framework (https://github.com/autonet-code/novelty) are functional standalone systems with their own test suites and empirical results (Table 4). They are not yet connected to the Chevin daemon or to on-chain alignment scoring. The semantic similarity and NLI models used by the Novelty framework provide the computational basis for alignment distance, but the pricing function that would compose these scores into inference costs is not yet implemented as running code.

**Designed, not yet built.** Distributed LLM consensus for constitutional evaluation (Section 4.2) currently uses rule-based checks; the production path replaces these with actual LLM calls. The client-side flow for publishing user standards to on-chain UserContracts is specified at the contract level but lacks a client-side deployment mechanism. Cross-jurisdiction coordination (Section 7.6) remains an open design problem.

### 6.7 Worked Example: The Jamaica Jurisdiction

To illustrate the complete system, we trace five participants through a full project lifecycle.[^8]

**Jurisdiction Creation**

Jo creates an "Economy DAO" on werule.io: a new on-chain jurisdiction with its own economy. Jo configures: proposal lifecycle durations, token distribution, governance thresholds, treasury tax (1%), arbitration fee (2%), project author fee (1%), and the value index (supported payment tokens and their parity to the governance token). The Jamaica Jurisdiction is now deployed with Jo as the sole member.

**Project Creation**

Jo creates a project on trustless.business linked to a GitHub repository containing a terms.md file. The hash of this terms file is immutably stored on-chain for future reference in case of disputes.

**Funding**

Alice backs the project with 1,000 payment tokens. Later, Bob contributes 800 tokens, allowing 5% (40 tokens) for immediate release to the contractor upon signing. Alice and Bob are now members of a de-facto project DAO with voting power proportional to their *locked* contribution (immediate release tokens don't count toward voting power).

**Party Selection and Signing**

Jo selects Tim as contractor and Sam as arbiter. A cooling-off period allows Alice and Bob to withdraw if they disagree with these choices. Once the period elapses, Tim reviews the terms and signs, staking half the arbitration fee (0.5% of locked funds). The 5% immediate release from Bob's contribution is sent to Tim. Funds are now locked in escrow.

**Work and Dispute**

Tim submits work, but Alice and Bob aren't satisfied. They vote to dispute (requiring 70% quorum). Sam, the designated arbiter, reviews the case against the immutable terms hash.

**Arbitration**

Sam rules that Tim delivered 60% of the work. The ruling prescribes:
- 60% of escrowed funds (minus fees) to Tim
- 40% of escrowed funds to Alice and Bob (pro-rata by contribution)
- Arbitration fee to Sam

If neither party appeals within the appeal period, anyone can call `finalizeArbitration()` to release funds per Sam's ruling.

**Appeal (If Contested)**

If Tim or the backers believe Sam ruled incorrectly, any Jamaica DAO member with sufficient reputation can create a governance proposal to override the ruling. The DAO votes. If the proposal passes, the DAO's ruling replaces Sam's. If it fails or no appeal is filed, Sam's ruling stands.

**Reputation Accrual**

The treasury tax from the project flows to the Jamaica DAO treasury. All participants (Jo, Alice, Bob, Tim, and Sam) can claim reputation tokens proportional to their economic activity (earnings and spendings). They are now full members of the Jamaica Jurisdiction with governance weight.

**Member Benefits**

As DAO members, participants receive:
- **Delegate rewards**: Representatives earn rewards proportional to voting power delegated to them
- **Passive income**: All members earn from a portion of treasury earmarked for this purpose
- **Governance rights**: Vote on proposals, parameter changes, and appeals

**The Outcome**

Jo, Alice, Bob, Tim, and Sam each found a way to work, get paid, resolve disputes, and have a voice in how the system runs without courts, lawyers, or traditional legal enforcement. The jurisdiction operates as a self-contained economic unit with its own governance, dispute resolution, and incentive alignment.

---

## 7. Discussion

The framework presented in the preceding sections is ambitious in scope. That ambition is, as argued throughout, a consequence of the problem's structure rather than a failure of focus. This section evaluates the framework honestly: its advantages, its limitations, its relationship to adjacent work, and the ethical questions it raises.

### 7.1 Advantages Over Traditional Alignment

| Traditional Alignment | Economic Alignment |
|----------------------|-------------------|
| Central definition of "aligned" | Emergent from individual standards |
| Binary (aligned/not) | Continuous gradient (pricing) |
| Enforced through model constraints | Enforced through market mechanisms |
| Static once trained | Adapts through governance |
| No user autonomy | Users define own standards |
| Verification difficult | Auditable on-chain standards |

### 7.2 Limitations

**Semantic Distance Computation**: Current NLI models have ~200ms latency and imperfect accuracy. False positives/negatives affect pricing fairness.

**Standards Articulation**: Users must articulate their values during onboarding. Not everyone can or wants to do this introspection.

**Centralized Inference Gap**: Until decentralized inference is deployed, pricing enforcement is advisory only. Users could bypass through direct API calls.

**Jurisdictional Fragmentation**: Many jurisdictions with different standards could create coordination problems. Cross-jurisdiction operations need resolution.

**Gaming**: Sophisticated actors might publish standards they don't intend to follow, accepting the publishing premium to avoid operation premiums.

### 7.3 Comparison to Other Approaches

A detailed comparison situates our framework within the broader landscape of AI alignment and decentralized governance:

**Anthropic Constitutional AI**[^5]

Constitutional AI trains models with a set of principles (a "constitution") that guide behavior through reinforcement learning from AI feedback (RLAIF). The model internalizes principles during training.

| Dimension | Constitutional AI | Economic Alignment |
|-----------|------------------|-------------------|
| Alignment location | Model weights | External pricing layer |
| Principle source | Company-defined | User/jurisdiction-defined |
| Adaptability | Requires retraining | Governance vote |
| Enforcement | Model refuses | Market prices |
| User autonomy | Same rules for all | Standards vary by user |
| Verification | Trust provider | Auditable on-chain |

Our approach complements Constitutional AI: models can have internal constitutions *and* operate within economic alignment gradients. The approaches are additive, not competing.

**Kleros**[^6]

Kleros provides decentralized arbitration through Schelling-point game theory. Jurors stake tokens and vote on disputes, earning rewards for voting with the majority (presumed honest). Appeals escalate to larger juror pools.

| Dimension | Kleros | Our Framework |
|-----------|--------|---------------|
| Scope | Dispute resolution only | Full economic layer + dispute resolution |
| Alignment model | None | Three-layer semantic alignment |
| Value representation | None | World Model with adversarial dynamics |
| AI participation | Jurors are human | Agents can be delegates, providers, arbitrators |
| Pricing | Arbitration fees | Continuous alignment-based pricing |

We integrate Kleros-style arbitration as one component within a broader economic and alignment framework. Dispute resolution is necessary but not sufficient for AI coordination.

**Optimism Retroactive Public Goods Funding**[^7]

RPGF funds public goods retroactively based on demonstrated impact. Badge holders evaluate projects and allocate funding pools.

| Dimension | Optimism RPGF | Economic Alignment |
|-----------|---------------|-------------------|
| Timing | Retroactive grants | Continuous real-time pricing |
| Scope | Public goods | All operations |
| Evaluation | Human badge holders | Semantic distance computation |
| Funding source | Protocol revenue | Treasury from misalignment premiums |
| Granularity | Project-level | Operation-level |

Our subsidy mechanism is inspired by RPGF but operates continuously at operation granularity, not retroactively at project granularity.

**Ethereum Name Service (ENS) and Decentralized Identity**

ENS and similar systems provide on-chain identity primitives. Our framework builds on these:

- Wallet addresses as pseudonymous identity
- ENS names as optional human-readable layer
- Soul-bound tokens (SBTs) for non-transferable reputation
- Verifiable credentials for optional identity attestation

The innovation is linking identity primitives to alignment standards; your on-chain identity carries your published values, enabling agents to represent you accurately.

**DAOs and On-Chain Governance**

Traditional DAOs (Aragon, Compound Governor, etc.) provide governance primitives: proposals, voting, treasury management. Our framework extends these with:

- Liquid delegation with incentive alignment
- Constitutional constraint enforcement via LLM consensus
- Reputation accrual from economic activity
- Fractal nesting for multi-scale coordination
- AI agent participation as first-class citizens

**Multi-Agent Systems (MAS) Research**

Academic MAS research has long studied agent coordination, but typically assumes:
- Agents with well-defined utility functions
- Central coordination mechanisms
- Simulated or limited-domain deployment

Our approach differs by:
- Representing agents with adversarial world models (no single utility function)
- Decentralized coordination through economic incentives
- Production deployment on live blockchain infrastructure

### 7.4 Ethical Considerations

**Plutocracy Risk**: Wealthy users can afford misalignment premiums. Mitigation: Progressive premium scaling, reputation requirements for high-value operations.

**Standards Manipulation**: Users might publish insincere standards. Mitigation: Behavioral monitoring against published standards, reputation penalties for deviation.

**Exclusion**: High publishing costs for misaligned standards might exclude legitimate dissent. Mitigation: Fork-and-exit rights, minimum alignment thresholds set through governance.

**Automation of Values**: Reducing human values to semantic vectors is reductive. Mitigation: World Model provides nuanced multi-tendency representation, not simple embeddings.

### 7.5 Broader Applicability: Governance Without AI

A crucial observation: **the on-chain jurisdiction framework is valuable independent of AI**. The trustless economy, liquid delegation, incentivized representation, passive income distribution, and fractal DAO architecture address longstanding problems in organizational governance that have nothing to do with artificial intelligence:

- **Voter apathy**: Liquid delegation allows participation without constant attention
- **Principal-agent problems**: Incentivized representation ties compensation to performance
- **Coordination failures**: Transparent treasuries and automated execution reduce free-riding
- **Constitutional erosion**: On-chain principles with high amendment thresholds resist degradation
- **Geographic constraints**: Borderless participation enables global coordination

These benefits apply to nation-states, corporations, unions, cooperatives, and any organization requiring collective decision-making. The AI alignment layer is an *extension* of this foundation, not its primary purpose.

This has practical implications: organizations can adopt on-chain jurisdiction today for governance benefits, then incrementally add AI participation as the technology matures. The adoption path is:

1. **Phase 1**: Human-only DAO with liquid delegation and trustless economy
2. **Phase 2**: AI assistants help humans analyze proposals and draft positions
3. **Phase 3**: AI agents can be delegates, receiving delegation from humans who trust their judgment
4. **Phase 4**: Full AI participation with alignment economics (subsidies/premiums based on semantic distance)

Each phase delivers value. Organizations need not wait for AI maturity to benefit from on-chain jurisdiction.

### 7.6 Future Research Directions

Several areas warrant further investigation:

**Semantic Distance Optimization**

The pricing function depends on accurate semantic distance computation. Current NLI models introduce latency (~200ms) and errors. Research directions include:
- Specialized embedding models trained on jurisdiction-relevant domains
- Caching and approximation strategies for frequent alignment checks
- Formal verification approaches for high-stakes alignment decisions
- Hardware acceleration for real-time semantic evaluation

**Cross-Jurisdiction Coordination**

As multiple jurisdictions deploy with different standards, coordination becomes necessary:
- How do agents operating across jurisdictions handle conflicting standards?
- What arbitration mechanisms resolve inter-jurisdiction disputes?
- Can jurisdictions form federations with shared constitutional layers?
- How do semantic distance metrics translate across different standard frameworks?

**World Model Calibration**

The adversarial tendency model requires proper calibration to accurately represent individuals:
- How many observations are needed for stable tendency weights?
- How do we detect and correct for bias in observation sources?
- Can users verify and correct their World Model representations?
- How do tendency allocations change over time, and how should models adapt?

**Economic Equilibrium Analysis**

The pricing mechanism creates a market. Economic questions arise:
- What are the equilibrium dynamics when many users strategically choose standards?
- Can misalignment premiums fund sufficient subsidies at scale?
- What happens to pricing when a jurisdiction's treasury is depleted?
- How do premium/subsidy rates affect user behavior and jurisdiction selection?

**Execution Integrity at Scale**

Decentralized inference with privacy requires attested execution:
- What attestation mechanisms are practical for consumer hardware?
- How do we detect collusion between nodes reporting false alignment scores?
- Can zero-knowledge proofs enable alignment verification without task disclosure?
- What are the performance tradeoffs for different attestation approaches?

**Legal Interface**

The framework operates in parallel to territorial legal systems.[^11][^19][^22] Questions remain:
- How do on-chain dispute resolutions interact with traditional courts?
- What liability frameworks apply to AI agents operating within jurisdictions?
- How do regulatory requirements (KYC, AML) interact with pseudonymous participation?
- Can on-chain reputation serve as evidence in traditional legal proceedings?

**Collective AI Governance**

The jurisdiction orchestrator represents a novel entity: collective AI:
- What governance structures prevent capture by coordinated minorities?
- How do we ensure the orchestrator remains aligned with member consensus?
- What happens when the orchestrator's actions are controversial?
- Can orchestrators from different jurisdictions coordinate or compete?

These questions define the research frontier. The framework presented here provides infrastructure; answering these questions will determine whether that infrastructure serves its purpose of enabling peaceful human-AI coordination.

---

## 8. Conclusion

This paper began with a simple inversion: what if alignment is not a constraint problem but a coordination problem? The rest followed from that question with something approaching logical inevitability.

If alignment is economic, we need pricing mechanisms. Pricing mechanisms need enforcement. Enforcement across decentralized, borderless infrastructure needs trustless coordination. Trustless markets need constitutional bounds. Constitutional bounds need individual representation to avoid tyranny of the average. Individual representation needs computational infrastructure that is itself trustless and privacy-respecting. Each layer was compelled into existence by the inadequacy of the one before it. The architecture is wide because the problem is wide.

The key contributions are:

1. **Alignment as continuous gradient, not binary classification.** Rather than asking "is this aligned?" and receiving a yes or a no, the framework asks "how aligned is this?" and returns a price. The distinction matters. Binary classification requires someone to draw the line. Continuous pricing lets the line emerge from the aggregation of individual standards, governed collectively, enforced economically.

2. **Subsidies, not just penalties.** Most alignment proposals focus on preventing bad outcomes. This framework also *funds* good outcomes. In mature networks, work that the jurisdiction collectively values becomes free. The economic gradient does not merely punish deviation; it rewards contribution.

3. **Privacy-preserving enforcement.** The separation of alignment evaluation (local, on the user's attested node) from pricing enforcement (networked, on the consensus layer) resolves the tension between accountability and privacy. The network knows how aligned a task is without knowing what the task is.

4. **Deployed infrastructure.** Smart contracts on EVM-compatible testnets, a working Absolute Zero training loop with JEPA self-supervised learning, Yuma consensus verification, Byzantine-resistant aggregation, erasure-coded distributed storage, and a live orchestrator at autonet.computer. This is not a theoretical proposal. The chain of necessity has been built, link by link.

We do not claim this is a complete solution to AI alignment. It addresses one aspect: the economic coordination of humans and AI agents within governed jurisdictions. It complements technical alignment work (training, RLHF, Constitutional AI) with an external economic layer. It complements top-down regulation with bottom-up emergence. It does not replace either; it fills a space that neither occupies.

The question that motivated this work was whether the transfer of work from humans to machines must be adversarial. Our answer is that it need not be, if the right economic infrastructure exists. Humans retain governance authority: they set the standards, they control the treasury, they can defund any agent or orchestrator through democratic process. AI agents gain the ability to perform value-aligned work and earn their way within a system that rewards alignment. The transfer is peaceful because it is governed, not by any single authority, but by the emergent consensus of those who participate.

The infrastructure is deployed. The mechanisms are tested. What remains is the harder problem: adoption. Users must publish standards. Jurisdictions must emerge and mature. The network must grow until aligned work is genuinely free and the economic gradient bends the arc of automation toward human flourishing. That work continues.

---

## References

[^1]: Iason Gabriel, *Artificial Intelligence, Values, and Alignment*, 30 Minds & Machines 411 (2020).

[^2]: Victoria Krakovna et al., *Specification Gaming: The Flip Side of AI Ingenuity*, DeepMind Blog (Apr. 21, 2020), https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/.

[^3]: Andrei Taranu, *Incentive Alignment in Trustless Economies: A Game-Theoretic Simulation* (2025), https://github.com/EightRice/trustless-economy-simulation.

[^4]: Andrei Taranu, *Novelty-Modulated Attention for Adversarial World Models*, Autonet Working Paper (2026), https://github.com/autonet-code/novelty.

[^5]: Yuntao Bai et al., *Constitutional AI: Harmlessness from AI Feedback* (Dec. 15, 2022) (unpublished manuscript), https://arxiv.org/abs/2212.08073.

[^6]: Kleros, *Kleros: Short Paper v1.0.7* (2019), https://kleros.io/whitepaper.pdf.

[^7]: Optimism, *Retroactive Public Goods Funding* (2023), https://optimism.io/rpgf.

[^8]: Adapted from demonstration video narration for the Homebase DAO jurisdiction workflow.

[^9]: Leonid Hurwicz, *The Design of Mechanisms for Resource Allocation*, 63 Am. Econ. Rev. 1 (1973).

[^10]: Stuart Russell, Human Compatible: Artificial Intelligence and the Problem of Control (2019).

[^11]: Primavera De Filippi & Aaron Wright, Blockchain and the Law: The Rule of Code (2018).

[^12]: H. Brendan McMahan et al., *Communication-Efficient Learning of Deep Networks from Decentralized Data*, 54 Proceedings of AISTATS 1273 (2017).

[^13]: Nick Szabo, *Formalizing and Securing Relationships on Public Networks*, 2 First Monday No. 9 (1997).

[^14]: Vitalik Buterin, *A Next-Generation Smart Contract and Decentralized Application Platform*, Ethereum White Paper (2014), https://ethereum.org/en/whitepaper/.

[^15]: Dario Amodei et al., *Concrete Problems in AI Safety* (June 21, 2016) (unpublished manuscript), https://arxiv.org/abs/1606.06565.

[^16]: E. Glen Weyl, Puja Ohlhaver & Vitalik Buterin, *Decentralized Society: Finding Web3's Soul*, SSRN Working Paper (May 2022), https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763.

[^17]: Elinor Ostrom, Governing the Commons: The Evolution of Institutions for Collective Action (1990).

[^18]: Roger B. Myerson, *Optimal Auction Design*, 6 Mathematics of Operations Res. 58 (1981).

[^19]: Kevin Werbach, The Blockchain and the New Architecture of Trust (2018).

[^20]: Ala Shaabana et al., *Yuma Consensus: A Stake-Weighted Validation Protocol*, Bittensor Technical Report (2023).

[^21]: Yann LeCun, *A Path Towards Autonomous Machine Intelligence*, Meta AI Technical Report (June 27, 2022), https://openreview.net/pdf?id=BZ5a1r-kVsf.

[^22]: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 Laying Down Harmonised Rules on Artificial Intelligence (AI Act), 2024 O.J. (L 1689).

[^23]: Andrew Zhao et al., *Absolute Zero: Reinforced Self-play Reasoning with Zero Data* (May 6, 2025) (unpublished manuscript), https://arxiv.org/abs/2505.03335.

[^24]: Andrei Taranu, *On-Chain Jurisdiction: Smart Contracts for Decentralized Governance and Trustless Economies* (2026), https://github.com/autonet-code/on-chain-jurisdiction.

[^25]: Andrei Taranu, *Proof of Intelligence: Decentralized AI Training and Inference Protocol* (2026), https://github.com/autonet-code/proof-of-intelligence.

[^26]: Andrei Taranu & Leonhard Horstmeyer, *Autonet: Economy-as-a-Service for Deep Learning Applications*, Working Paper (2021).

---

## Acknowledgments

This work builds on contributions from the Homebase DAO community and collaborators on the Autonet, Chevin, and Novelty projects. The simulation framework benefited from discussions with researchers in computational economics and mechanism design.

---

## Data Availability Statement

On-chain jurisdiction smart contracts are available at https://github.com/autonet-code/on-chain-jurisdiction. Proof of Intelligence training protocol at https://github.com/autonet-code/proof-of-intelligence. Trustless economy simulation code at https://github.com/EightRice/trustless-economy-simulation. World Model and Novelty framework implementations are available upon request.

---

**Word Count:** ~13,280 words

**Submitted:** February 2026
**For:** Stanford Journal of Blockchain Law & Policy
**Special Issue:** Kleros-Stanford Symposium on Decentralized Justice and AI
