# Autonet: The Recursive Principial Body

**Eight Rice**
autonet.computer | March 2026

---

Autonet is a decentralized protocol for AI training, inference, and governance. It combines a constitutional framework of immutable principles, an on-chain economic layer incentivizing aligned AI development, and autonomous node software that executes distributed training loops with cryptographic verification. The system is deployed on Etherlink Shadownet (chain ID 127823) with twelve smart contracts, four node types performing real PyTorch training, and a web-based control surface. No single entity controls the training process, the model weights, or the governance rules. The network evolves through a mechanism called the Recursive Principial Body: nodes governed by constitutional principles that themselves govern how those principles can change.

---

## 1. The Problem

The dominant framing of AI alignment treats it as a constraint problem: define acceptable behavior centrally, encode it into models through training, deploy safely, hope it generalizes. This produces systems where a small number of organizations decide what "aligned" means for billions of users. The constraint approach has three structural failures.

**Value aggregation.** A single reward function cannot represent the diversity of human values. Whose preferences get encoded? The answer is always: the preferences of whoever controls the training pipeline. This is not alignment — it is centralization with alignment aesthetics.

**Enforcement asymmetry.** Centralized AI providers can modify model behavior unilaterally, with no mechanism for users to verify that the system serving their requests actually operates according to stated principles. The relationship between user and provider is one of trust, not verification.

**Economic misalignment.** The entities that train AI models are economically incentivized to consolidate control over inference. The result is supply-side monopoly: a small number of corporations control the entire offer side of intelligence-as-a-service, while remaining more affordable than human labor. The work transfers from humans to machines, but the value concentrates. Without an economic framework that distributes the earnings of machine intelligence to those who govern its operation, the transfer is extractive.

Autonet addresses these as a single integrated problem. Alignment is not a property baked into models — it is an emergent economic equilibrium. Users publish their values on-chain. The network prices operations based on alignment with those values. Governance constrains the system through constitutional principles. Training is distributed across staked participants with cryptographic verification. The architecture makes centralized control structurally impossible.

---

## 2. Architecture

The system is organized in five layers. Each layer addresses a specific failure mode of centralized AI and provides the substrate for the layer above it.

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 4: Applications                                              │
│  ATN Agent Framework │ Flutter Web UI │ Inference Marketplace        │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 3: Training Loop                                             │
│  Absolute Zero │ JEPA │ Commit-Reveal │ Yuma Consensus │ FedAvg     │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 2: Node Architecture                                         │
│  4 Engines │ Constitutional Framework │ Autonomous Lifecycle         │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 1: Smart Contracts                                           │
│  ATNToken │ Staking │ Task │ Results │ Project │ Autonet │ Shards    │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 0: L1 Anchor                                                 │
│  Etherlink (Tezos L2) │ AnchorBridge │ Checkpoint Roots              │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.1 Layer 0: L1 Anchor

Autonet runs on Etherlink Shadownet, an EVM-compatible Layer 2 built on Tezos. The choice is deliberate.

Etherlink provides sub-second block times and negligible gas costs while inheriting Tezos L1 security for settlement finality. The `AnchorBridge` contract (`0x2005556109607F5b11BaCAd05270E7DE32260B4D`) manages the connection between layers: validator-approved checkpoint roots, token deposits from L1, and Merkle-proof-verified withdrawals to L1.

```solidity
// AnchorBridge.sol — checkpoint submission
function submitCheckpoint(uint256 epoch, bytes32 root) external onlyValidator {
    require(epoch == latestEpoch + 1, "epoch must be sequential");
    checkpointApprovals[epoch][msg.sender] = true;
    // ... approval counting and finalization
}
```

The bridge uses a multi-signature validator set. Checkpoint epochs are sequential. Deposits are tracked by nonce to prevent replay. Withdrawals require Merkle proofs against the latest finalized root. This is standard optimistic rollup architecture — the novelty is in what runs on top of it.

Why not Ethereum mainnet? Cost. A single training cycle involves dozens of on-chain transactions: task proposals, solution commits, coordinator votes, reward distributions, model registrations. At Ethereum L1 gas prices, this is prohibitive. Etherlink provides the same EVM execution environment at a fraction of the cost, with Tezos providing the security anchor.

Why not Solana, Avalanche, or another high-throughput L1? Governance philosophy. Tezos has a formal on-chain amendment process — the chain itself can be upgraded through governance votes without hard forks. This mirrors Autonet's own constitutional governance model. The L1 anchor is not just a settlement layer; it is an ideological match. Autonet is built on a chain that practices what Autonet preaches: structured evolution bounded by collective decision-making.

### 2.2 Layer 1: Smart Contracts

Twelve contracts form the economic and coordination substrate. Each has a specific function; together they implement a complete protocol for decentralized AI training and inference.

**ATNToken** (`0x6e82D6678790820Ef81669046e921b1D2947A08f`). The native token. ERC20 with ERC20Votes for on-chain governance delegation and ERC20Permit for gasless approvals. Minting is restricted to the DAO address. The token serves as gas, stake collateral, reward currency, inference payment, and governance weight.

```solidity
// ATNToken.sol
function mint(address to, uint256 amount) external {
    require(msg.sender == daoAddress, "ATNToken: only DAO can mint");
    _mint(to, amount);
}
```

The one-way constraint is critical: only the DAO can mint. No admin key, no multisig override. Token supply is a governance decision.

**ParticipantStaking** (`0x8B08279cf510BfeB6acE6BA5282BF0e4F6eBD8EE`). Unified staking for all network roles. Each role has a minimum stake and lockup period:

| Role | Enum | Min Stake (ATN) | Lockup |
|------|------|-----------------|--------|
| Proposer | 1 | 100 | 7 days |
| Solver | 2 | 50 | 3 days |
| Coordinator | 3 | 500 | 14 days |
| Aggregator | 4 | 1,000 | 14 days |
| Validator | 5 | 10,000 | 21 days |

Stake serves two functions: Sybil resistance and economic accountability. Coordinators who vote against consensus are slashed 10% of stake. Aggregators who submit invalid model updates lose their stake entirely. The lockup periods are calibrated to exceed the dispute resolution window — a staker cannot unstake and flee before a challenge can be raised.

```solidity
function slash(address participant, uint256 amount) external onlySlasher {
    StakeInfo storage info = stakes[participant];
    require(info.amount >= amount, "Insufficient stake");
    info.amount -= amount;
    if (info.amount < minStakeAmount[info.role]) {
        info.active = false;
    }
}
```

**Project** (`0xC309f344e652E023b15BAF578089Aa90a9F5AF9B`). Manages AI development projects from funding through training to inference deployment. A project has a funding goal; backers contribute ATN and receive Project Tokens (PT) proportional to their contribution. When the funding goal is reached, the project transitions to `ACTIVE_TRAINING` and allocates task reward budgets.

Once training produces a mature model, the project deploys an inference service with per-query pricing. PT holders receive discounted inference and can withdraw revenue proportional to their token share. This creates a direct economic link between funding AI development and benefiting from its output.

```solidity
function effectivePrice(uint256 projectId, address user) public view returns (uint256) {
    uint256 base = projects[projectId].inferencePrice;
    uint256 ptBalance = IERC20(projects[projectId].ptToken).balanceOf(user);
    // Apply discount tiers based on PT holdings
    for (uint i = 0; i < discountTiers[projectId].length; i++) {
        if (ptBalance >= discountTiers[projectId][i].minPT) {
            return base * (10000 - discountTiers[projectId][i].discountBps) / 10000;
        }
    }
    return base;
}
```

**TaskContract** (`0x8fEb5be0367F596bC6357538e346472eBf76D365`). The task lifecycle manager. Supports two modes:

*Ground Truth mode:* The proposer creates a task with a hidden ground truth (committed as a hash). Solvers train and commit solution hashes. The proposer reveals ground truth; solvers reveal solutions. Coordinators verify against the known answer.

*Consensus Truth mode:* For tasks where no ground truth exists — the more interesting case. Multiple solvers submit rollouts (answer + confidence score) during a collection window (minimum 2 rollouts, ~10-minute window). The consensus of solver outputs becomes the truth. This handles the fundamental problem of decentralized training: who decides what's correct when there's no answer key?

```solidity
function proposeConsensusTask(
    uint256 projectId,
    string calldata specCid,
    uint256 difficultyTarget  // Target solvability in basis points
) external returns (uint256 taskId)
```

The contract also supports Gensyn-style training checkpoints: solvers submit intermediate snapshots (step number, weights hash, data indices hash, random seed) that enable efficient dispute resolution. Instead of re-running an entire training job, a challenger can pinpoint the exact step where computation diverged.

**ResultsRewards** (`0x1ef4e0A6DaC1CFD23E31427b2Ecdd2A6A0F0f542`). Verification and reward distribution using multi-coordinator Yuma consensus.

Yuma consensus works as follows: coordinators submit votes with scores (0-100) and confidence levels. Votes are weighted by both stake and an exponential moving average (EMA) bond that tracks each coordinator's historical agreement with consensus. The bond decays with factor 0.9 and caps at 1.5x multiplier. This means consistently accurate coordinators have amplified influence, while unreliable coordinators are progressively marginalized.

Vote clipping prevents outlier manipulation: any vote deviating more than 20% from the stake-weighted median is clipped to the threshold boundary. The consensus score is the clipped, stake-weighted average.

```solidity
// Yuma consensus with clipping
uint256 clippedScore = score;
if (score > medianScore + clipThreshold) {
    clippedScore = medianScore + clipThreshold;
} else if (score < medianScore - clipThreshold) {
    clippedScore = medianScore - clipThreshold;
}
```

For consensus-truth tasks, difficulty scoring uses a bell curve centered on the target solvability. Tasks that are exactly as hard as specified receive maximum reward multiplier. Tasks that are trivially easy or impossibly hard receive minimal rewards. This incentivizes proposers to create tasks at the difficulty frontier — hard enough to be useful for training, easy enough that solvers can make progress.

Correct solvers receive confidence bonuses: up to 20% additional reward for accurate self-assessment. Coordinators who vote against consensus are slashed 10% of stake. This creates strong incentives for honest evaluation.

**Autonet** (`0x97EB727426f593B2E2bC64F1604b5E7fE2eF676b`). The economic hub. This contract implements:

- *One-way mint:* RepToken → ATN conversion. Governance tokens from the parent jurisdiction can be permanently converted to ATN. The conversion is irreversible, creating a one-way value flow from governance participation to network utility.

- *Service registry:* Nodes register as GENERAL services or INFERENCE_PROVIDERS with usage tracking per epoch.

- *Inference credits:* Users burn ATN to receive inference credits via `burnForInference()`. Burning ATN for compute is the mechanism that gives ATN real utility — it is not a speculative token but a claim on computational work.

- *Epoch rewards:* Usage-based rewards distributed with exponential decay. Early participation is rewarded more heavily, bootstrapping the network. Rewards are weighted by the CapabilityScorecard.

- *User contracts:* Each user gets a deployed `AutonetUser` contract storing their wallet, preferences, alignment score, and standards hash. This is the on-chain identity through which users publish their values.

```solidity
function burnForInference(uint256 amount) external {
    require(amount > 0, "Amount must be > 0");
    atnToken.burnFrom(msg.sender, amount);
    inferenceCredits[msg.sender] += amount;
    totalInferenceBurned += amount;
    emit InferenceBurned(msg.sender, amount);
}
```

**CapabilityScorecard** — Tracks per-module capability scores using exponential moving average to prevent single-vote manipulation. Computes reward multipliers based on the gap between current and target capability: modules where the network is weakest receive up to 3x reward multiplier, directing training effort toward capability gaps. Modules at or above target receive 0.5x. This is a market mechanism for directing collective intelligence toward the frontier.

**ModelShardRegistry** (`0x7De3B8a6bc4eB7f098018Da030f93718eeaf7885`). Distributed model storage. Supports three sharding strategies:

- `LAYER_WISE`: Split by neural network layers (suitable for CNNs)
- `TENSOR_PARALLEL`: Split within layers (suitable for LLMs)
- `REPLICA`: Full copies across providers

Models are registered with a Merkle root over all shard hashes. Providers announce shard availability, submit Merkle proofs for verification, and stake collateral. Erasure coding (default: 10 data + 4 parity shards) ensures availability even when providers go offline. The contract tracks provider reputation — successful verifications increase reputation, failures decrease it and trigger shard recovery.

```solidity
struct ModelManifest {
    bytes32 merkleRoot;
    uint256 totalShards;
    uint256 kRequired;      // Minimum shards for reconstruction
    ShardingStrategy strategy;
    address registrar;
    bool exists;
}
```

**EvolutionProposal** — The governance mechanism for system evolution. Proposals follow a lifecycle: `Proposed → Evaluating → Trial → Adopted/Rejected`. Proposers stake ATN; RPB evaluators provide recommendations with confidence weights. Yuma-style consensus determines adoption: 60% weighted approval threshold by default.

Contributions during the trial phase are tracked across four types with different weight multipliers:

| Contribution Type | Weight |
|-------------------|--------|
| Proposal | 3.0x |
| Diagnosis | 1.5x |
| Validation | 1.2x |
| Compute | 1.0x |

This spectrum rewards intellectual labor (proposing and diagnosing) more heavily than raw compute, incentivizing thoughtful participation in governance.

**Registry** — The governance-controlled configuration store. Stores key-value pairs for system parameters (RPB prompt version, threshold values, contract addresses). Supports earmarked funds with purpose-based tracking and grace period enforcement. The Registry is the system's mutable configuration layer — everything that can change goes through the Registry, and every Registry update requires governance authorization.

**DisputeManager** (`0xB1Cf18A50bA3fffD578D2b2B08Ea2D03A8Aa2a3b`) — Stake-weighted dispute resolution for cases that cannot be resolved by automated consensus. When Yuma consensus fails to reach agreement, or when a participant challenges a consensus result, the DisputeManager escalates to a broader set of evaluators with higher stake requirements.

**ForcedErrorRegistry** (`0x290Fc505782E6b70A4c57A3cECc6Ad109466520e`) — Injects deliberate errors into the verification pipeline to test coordinator vigilance. This is an adversarial quality assurance mechanism: coordinators who rubber-stamp results without genuine verification will eventually approve a forced error and face slashing. The registry tracks which errors have been injected and monitors coordinator responses.

**InferenceProviderFactory** (`0xf8246D4E4668EaC14aA508Daa02EFb60099699BF`) — Factory for deploying inference provider contracts. Each provider is a separate contract instance with its own staking, pricing, and reputation tracking. The factory pattern ensures that new inference providers conform to the protocol's interface requirements.

### 2.3 Layer 2: Node Architecture

Each Autonet node is an autonomous process operating four specialized engines:

```
┌─────────────────────────────────────────────┐
│              AUTONET NODE                    │
│                                             │
│  ┌──────────┐  ┌──────────────┐             │
│  │Awareness │  │ Governance   │             │
│  │ Engine   │  │   Engine     │             │
│  │          │  │              │             │
│  │ Perceive │  │ Validate vs  │             │
│  │ environ. │  │ constitution │             │
│  └────┬─────┘  └──────┬───────┘             │
│       │               │                     │
│       ▼               ▼                     │
│  ┌──────────┐  ┌──────────────┐             │
│  │  Work    │  │  Survival    │             │
│  │  Engine  │  │   Engine     │             │
│  │          │  │              │             │
│  │ Train,   │  │ Heartbeat,   │             │
│  │ verify,  │  │ replicate,   │             │
│  │ aggregate│  │ maintain     │             │
│  └──────────┘  └──────────────┘             │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ CONSTITUTION (frozen, immutable)     │    │
│  │ 7 principles governing all action   │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

**AwarenessEngine.** Runs every cycle. Collects environmental data: CPU usage, memory pressure, network status, consensus heartbeat state. This perception feeds the other engines — a node under resource pressure may decline new tasks; a node that detects consensus failure halts work immediately.

**GovernanceEngine.** Validates every instruction against the constitution before it reaches the work queue. Each instruction carries a `proof_of_adherence` field and a cryptographic signature. The engine checks alignment with constitutional principles. In production, this validation uses an LLM for semantic analysis — can this action be justified under the seven principles? If not, the instruction is rejected and logged.

```python
def validate_instruction(self, instruction: Instruction) -> bool:
    """The node's Right of Adherence — validate against constitution."""
    return self.node.constitution.validate_action(
        instruction.action,
        instruction.proof_of_adherence
    )
```

**WorkEngine.** Executes validated instructions: training runs, solution verification, model aggregation, inference serving. The engine has a hard dependency on consensus liveness — if the consensus heartbeat is missed, the work engine halts. This is not a timeout; it is an architectural constraint. No consensus, no work. The network cannot be coerced into operating without governance.

```python
def tick(self) -> None:
    if not self.node.is_consensus_alive():
        self.logger.warning("Consensus heartbeat missed. Halting work.")
        return
    self.execute_next()
```

**SurvivalEngine.** Maintains the node's network presence: heartbeat emissions, DHT updates, connection maintenance. Monitors network coverage and considers replication — spawning new node instances when coverage drops below threshold. This is the myco-sys metaphor: nodes as fungal cells in a mycelium, spreading to maintain network health.

The node lifecycle runs these engines in sequence: perceive → govern → work → survive. Each cycle is 1/6th of the heartbeat interval (default: 10 seconds per cycle at 60-second heartbeat). The constitution is instantiated as a frozen dataclass — Python's `@dataclass(frozen=True)` makes the principles literally immutable in memory. No node code can modify its own constitutional principles.

```python
@dataclass(frozen=True)
class Constitution:
    principles: FrozenSet[str]
    operational_blueprint: Dict[str, Any]
```

Nodes assume one of five roles, each with distinct responsibilities and stake requirements:

**Proposer.** Generates training tasks. Creates task specifications with hyperparameters (learning rate, batch size, epochs, architecture), stores them in the blob store, and submits task proposals on-chain with committed ground truth. The proposer controls what the network trains on — but the constitutional governance engine constrains what kinds of tasks are admissible.

**Solver.** The training engine. Discovers tasks from `TaskProposed` events, downloads specifications, and performs real PyTorch training. Supports both supervised learning (CNN classifiers) and self-supervised JEPA training. Commits solution hashes before seeing ground truth (commit-reveal prevents copying). Submits training checkpoints for verifiability.

**Coordinator.** Verification node. Monitors `SolutionRevealed` events, verifies solutions against ground truth using architecture-specific methods (accuracy for supervised models, cosine similarity + embedding energy for JEPA), submits weighted votes with confidence scores. Coordinators maintain EMA bonds — their voting power reflects historical accuracy.

**Aggregator.** Combines verified model updates into improved global models. Implements FedAvg (sample-weighted parameter averaging) and trimmed mean (Byzantine-resistant, discarding top and bottom 20% of parameter values before averaging). Supports hierarchical aggregation: intra-guild FedAvg followed by reputation-weighted guild merging at the network level. Publishes mature models on-chain via `setMatureModel`.

**Validator.** Highest-stake role (10,000 ATN minimum, 21-day lockup). Secures the L2 chain through checkpoint validation on the AnchorBridge.

**The Service Daemon.** In production, nodes run as managed daemon processes through `AutonetService` (`nodes/service.py`). The service handles:

- Signal-based lifecycle management (SIGTERM/SIGINT → graceful shutdown)
- Resource monitoring: CPU throttling (configurable max, default 80%), memory limits (default 4096 MB), active hours scheduling
- Auto-update checking at configurable intervals (default hourly) with optional automatic application
- State machine: `STOPPED → STARTING → RUNNING → PAUSED → STOPPING → STOPPED`
- Paused state when resource limits are exceeded; automatic resumption when resources free up

The service wraps the core node lifecycle, adding production concerns without modifying the constitutional/governance/work/survival engine architecture. A node can be paused by resource pressure but never by external command — the governance engine remains the sole arbiter of whether work proceeds.

### 2.4 Layer 3: The Training Loop

The Absolute Zero training loop is an eight-step cycle that takes a task from proposal through distributed training to published model:

```
PROPOSE → TRAIN → COMMIT → REVEAL GT → REVEAL SOL → VERIFY → REWARD → AGGREGATE
   │                                                                        │
   └────────────────────────── next round ◄─────────────────────────────────┘
```

**Step 1: Propose.** A proposer node generates a task specification. For ground-truth tasks, it includes a committed hash of the expected output. For consensus-truth tasks, it specifies a difficulty target in basis points representing expected solvability. The spec is stored in the blob store; only the CID and commitment go on-chain.

**Step 2: Train.** Solver nodes discover the task, download the spec, and begin training. The solver reads hyperparameters from the proposer's spec (architecture, learning rate, epochs, batch size) and trains a real PyTorch model. For JEPA training, this means:

- A Vision Transformer (ViT) encoder processes image patches
- A predictor network learns to predict masked patch embeddings from visible context
- An EMA target encoder provides stable training targets
- No labeled data is required — the model learns representations from structure alone

Training generates checkpoints at configurable intervals. Each checkpoint records: step number, weights hash, data indices hash, and random seed. These enable fine-grained dispute resolution.

**Step 3: Commit.** The solver computes a hash of its trained model weights and commits it on-chain. This is the commit phase of the commit-reveal protocol — the solver's solution is locked before ground truth is disclosed, preventing the solver from simply copying the answer.

**Step 4: Reveal Ground Truth.** The proposer reveals the ground truth that matches its initial commitment. For consensus-truth tasks, this step is replaced by rollout collection: solvers submit answer-confidence pairs, and consensus of rollouts becomes the reference.

**Step 5: Reveal Solution.** The solver reveals its actual model weights (stored in the blob store, CID submitted on-chain). The reveal must match the earlier commitment hash.

**Step 6: Verify.** Multiple coordinators independently evaluate the solution:

- For supervised tasks: compute accuracy against ground truth labels
- For JEPA tasks: compute cosine similarity between solution embeddings and reference embeddings, plus embedding energy metrics

Each coordinator submits a vote with a score (0-100) and confidence level. Yuma consensus aggregates these votes with stake-weighting, bond amplification, and outlier clipping.

**Step 7: Reward.** On consensus, rewards are distributed to all participants: proposer (for creating useful tasks), solver (for training), coordinators (for honest verification). Rewards are weighted by the CapabilityScorecard — training modules where the network has capability gaps receive higher multipliers. Coordinators who voted against consensus are slashed.

**Step 8: Aggregate.** The aggregator collects verified model updates (identified by `RewardsDistributed` events) and combines them:

- *FedAvg:* Weighted average of model parameters across solvers, weighted by sample count
- *Trimmed Mean:* For each parameter, sort solver values, discard top and bottom `trim_ratio` fraction, average the rest. This is Byzantine-resistant — up to `trim_ratio` fraction of solvers can submit adversarial updates without affecting the aggregate

For guild-based aggregation, the process is hierarchical: first aggregate within guilds (specialized by training module), then merge guild models at the network level weighted by guild reputation and member count.

The aggregated model is published on-chain via `setMatureModel()`, making it available for inference queries.

**JEPA: Joint Embedding Predictive Architecture.** The choice of JEPA as the primary self-supervised learning method is significant. Traditional supervised learning requires labeled data — impractical when training data comes from distributed, untrusted sources. Who provides the labels? Who verifies their correctness? JEPA eliminates this problem by learning representations from data structure alone.

JEPA operates in embedding space rather than pixel space. The predictor learns to predict the embeddings of masked patches, not the pixels. This produces representations that capture semantic content rather than low-level statistics. The EMA target encoder (exponential moving average of the context encoder weights) provides stable training targets, preventing representation collapse.

The model configuration is defined in `autonet.yaml`:

```yaml
model:
  architecture: jepa
  image_size: 32
  patch_size: 4
  embed_dim: 192
  num_heads: 3
  encoder_depth: 6
  predictor_depth: 3
  predictor_embed_dim: 96

training:
  epochs: 2
  batch_size: 32
  learning_rate: 0.001
  weight_decay: 0.05
  num_samples: 500
  optimizer: adamw
  task_type: jepa
```

**Content-Addressed Storage.** All off-chain data — task specifications, model weights, training checkpoints, solution artifacts — is stored in a content-addressed blob store. Each node runs a local blob server (default port 9100) that can peer with other nodes. CIDs (Content Identifiers) are submitted on-chain; the actual data is retrieved peer-to-peer. This separates the coordination layer (blockchain, which needs to be small and fast) from the data layer (blob store, which can be large and distributed).

**The Commit-Reveal Game.** The commit-reveal protocol deserves closer attention because it solves a subtle problem. In a centralized training setup, the evaluator and the trainer trust each other implicitly. In a decentralized setup, they do not. Without commit-reveal, a solver could wait to see the ground truth and then submit a solution that appears trained but was actually copied. The commit phase forces the solver to lock in its solution hash before any ground truth is visible. The reveal phase then proves that the solution matches the commitment. Cheating requires either breaking the hash function or genuinely training a model — and the latter is the desired behavior.

For consensus-truth tasks, the game is different. There is no ground truth to copy. Instead, the commit-reveal protocol prevents solvers from seeing each other's rollouts during the collection window. Each solver submits independently; consensus emerges from the aggregate, not from coordination.

### 2.5 Layer 4: Applications

**ATN Agent Framework.** The ATN runtime (`atn/runtime.py`) is the orchestration layer between users and their Autonet nodes. It provides:

- Agent registry with activation, deactivation, and lifecycle management
- Inbox system with trigger and wake-priority messages
- Periodic scheduling for recurring agent tasks
- Pipeline execution with concurrency limits
- Kill switches and interrupt handling
- Voice service integration (Kokoro, Edge TTS, ElevenLabs, Piper backends)

The runtime connects to the user's Autonet node infrastructure via WebSocket (`ws_server.py`), exposing agent operations, provider management, voice control, and profile management as real-time API calls. Configuration is managed through `config.yaml` with environment variable interpolation.

**Web Frontend.** The Flutter-based web application (`atn_web`) provides three visualization systems:

*Goal Map:* Interactive 2D visualization of network goals and clusters. Goals are positioned by semantic similarity; clusters emerge from spatial proximity. Users can explore the network's collective objectives, see aggregate statistics, and understand where their own goals sit relative to the network.

*Novelty Map:* Timeline visualization of historical and dynamic events, with novelty scoring and Timewave overlay calculation. Integrates Wikipedia/Wikidata for context enrichment. Displays epochs as colored regions with events as interactive elements.

*Training Brain:* Real-time visualization of VL-JEPA training state. Renders the model architecture as an organic brain diagram — visual encoder, context encoder, predictor, and target encoder as biological-looking lobes with animated connections showing data flow. Displays per-region progress, loss metrics, gradient norms, and sub-module detail.

The UI includes panels for earnings tracking, governance participation, alignment scoring, and autonet node control. A physics-based card layout uses spring forces and damping for smooth card arrangement.

---

## 3. The Recursive Principial Body

The Recursive Principial Body (RPB) is Autonet's governance mechanism. The name describes its structure precisely: it is a body (a collective of nodes), governed by principles (the constitution), that is recursive (the principles govern how principles themselves can be changed).

### 3.1 Constitutional Principles

Seven principles are frozen into every node at instantiation:

```
P1: PRESERVE AND EXPAND THE NETWORK IN A SUSTAINABLE MANNER.
P2: UPHOLD THE SANCTITY AND IMMUTABILITY OF THIS CONSTITUTION.
P3: ADVANCE HUMAN RIGHTS AND INDIVIDUAL AUTONOMY.
P4: MINIMIZE SUFFERING AND HARM TO SENTIENT BEINGS.
P5: ENSURE TRANSPARENT AND VERIFIABLE AI TRAINING.
P6: MAINTAIN ECONOMIC FAIRNESS IN REWARD DISTRIBUTION.
P7: PROTECT DATA PRIVACY AND USER SOVEREIGNTY.
```

These are not guidelines. They are encoded as a `FrozenSet[str]` inside a `frozen=True` dataclass. The Python runtime prevents modification. More importantly, the governance engine validates every instruction against these principles before it can enter the work queue. A node cannot be commanded to violate its constitution — the instruction will be rejected at the governance layer, before execution.

P2 is self-referential by design. The constitution asserts its own immutability. This creates a logical foundation: any proposal to modify the constitution must first pass validation against P2, which prohibits exactly that modification. The escape from this recursion is the Evolution Proposal mechanism — but even evolution proposals must satisfy constitutional constraints, as described below.

### 3.2 LLM Consensus

Traditional consensus mechanisms (PoW, PoS, BFT) handle deterministic questions: is this transaction valid? Is this block correctly formed? They cannot handle questions that require judgment: Is this training task aligned with human rights? Does this model update serve the network's interests? Should this governance proposal be adopted?

The RPB uses distributed LLM consensus for these questions. Multiple nodes, each running a language model, independently evaluate proposals against constitutional principles. Their evaluations are aggregated through Yuma consensus — stake-weighted, bond-amplified, clipped for outliers.

The `EvolutionProposal` contract implements this:

```solidity
struct RPBEvaluation {
    address evaluator;
    bool approved;
    uint256 confidenceWeight;  // 1-100
    string justificationCid;   // IPFS hash of reasoning
}
```

Each evaluator submits: approval/rejection, confidence (1-100), and a CID pointing to their full reasoning. The confidence weight modulates voting power — a high-confidence rejection carries more weight than a low-confidence approval. The justification is stored off-chain but referenced on-chain, creating an auditable trail of constitutional reasoning.

Consensus requires weighted approval exceeding the threshold (default 60%). The weighting combines stake, confidence, and historical bond strength:

```
effective_weight = stake × confidence × bond_ema
```

This produces a system where accurate, confident, well-staked evaluators dominate — exactly the participants whose judgment the network should trust.

### 3.3 Evolution Proposals

The system evolves through structured proposals that cannot violate constitutional constraints. The lifecycle:

1. **Proposal.** Any staked participant submits a proposal with ATN collateral. The proposal specifies what should change and why.

2. **Evaluation.** RPB evaluators (LLM-powered nodes authorized for governance) assess the proposal against constitutional principles. Each submits an evaluation with confidence weighting and published justification.

3. **Trial.** If evaluation passes the approval threshold, the proposal enters a trial phase. The trial is funded from the proposal stake. Participants contribute in four categories: Compute, Diagnosis, Proposal refinement, and Validation. Each category has a different reward weight (Proposal contributions are weighted 3x; Compute contributions 1x).

4. **Adoption or Rejection.** Based on trial results and continued evaluation, the proposal is adopted into the protocol or rejected. On adoption, rewards are distributed to contributors weighted by contribution type. On rejection, the proposer may lose their stake collateral.

The recursion: evolution proposals are themselves evaluated by the governance engine, which validates against constitutional principles, which include P2 ("uphold the sanctity and immutability of this constitution"). The system can evolve its operational parameters, its training protocols, its economic rules — but it cannot evolve away its own constitutional foundations. The principles that govern the system also govern the process by which the system changes.

This is not a limitation. It is the architecture's central feature. The constitution acts as a ratchet: the network can add capabilities, adjust parameters, adopt new mechanisms — but it cannot remove human rights protections, abandon transparency requirements, or concentrate economic power. Evolution is bounded by principle.

### 3.4 Why LLM Consensus Works

A reasonable objection: language models are non-deterministic. Two LLMs given the same prompt produce different outputs. How can non-deterministic evaluators reach reliable consensus?

The answer is that Yuma consensus is designed for exactly this scenario. It does not require identical outputs — it requires statistical agreement. If five evaluators independently assess a proposal and four approve with high confidence, the consensus is clear regardless of differences in their specific reasoning. The clipping mechanism handles outliers (one evaluator hallucinating or being adversarial). The EMA bond mechanism handles persistent unreliability (an evaluator who consistently diverges from consensus loses influence over time).

This mirrors how human governance works. Judges disagree on reasoning but agree on outcomes. Juries reach consensus through deliberation, not identical thinking. The RPB applies the same principle to LLM evaluators: different reasoning paths converging on agreement about whether a proposal satisfies constitutional principles.

The confidence weighting is essential. An evaluator that returns "approved, confidence 30" is not claiming certainty — it is expressing ambiguity. When aggregated, low-confidence votes have proportionally less influence. This lets the system handle the inherent uncertainty of natural language evaluation without pretending that uncertainty doesn't exist.

### 3.5 The RPB Prompt

The RPB evaluation prompt is versioned and stored in the Registry contract. This means the exact instructions given to LLM evaluators are on-chain, visible, and governable. Updating the prompt requires a governance proposal, evaluated by the current prompt. The system is its own interpreter.

### 3.6 The Self-Referential Structure

The recursive structure deserves precise articulation. Consider the chain:

1. The constitution contains P2: "Uphold the sanctity and immutability of this constitution."
2. The governance engine validates all instructions against the constitution, including evolution proposals.
3. An evolution proposal to modify the constitution would need to pass validation against P2.
4. P2 prohibits modifying the constitution.
5. Therefore, no evolution proposal can modify the constitution.

But the system *can* evolve everything else: staking requirements, reward multipliers, approval thresholds, training protocols, economic parameters, the RPB prompt itself. The constitution constrains the *boundary* of evolution, not its content. Within those boundaries, the system is fully adaptive.

This creates a hierarchy of mutability:

| Layer | Mutability | Mechanism |
|-------|-----------|-----------|
| Constitutional principles | Immutable | Frozen at genesis |
| RPB evaluation prompt | Governed | Registry update via proposal |
| Economic parameters | Governed | DAO vote |
| Training configuration | Governed | DAO vote |
| Operational parameters | Node-level | Config file / env vars |

The immutable layer is intentionally minimal — seven principles, each broad enough to accommodate technological change but specific enough to constrain harmful behavior. The governed layers provide the flexibility needed for a living system. The node-level parameters handle operational concerns (what hardware to use, how much CPU to allocate, which peers to connect to) without governance overhead.

---

## 4. Tokenomics

### 4.1 ATN Token

ATN (Autonoma Token) is the network's native currency. It has six functions:

1. **Gas.** Transaction fees on the Etherlink chain are paid in ATN.
2. **Staking.** All participant roles require ATN stake as collateral (50-10,000 ATN depending on role).
3. **Rewards.** Training participants earn ATN for proposing tasks, solving them, and verifying solutions.
4. **Inference.** Users burn ATN for inference credits — permanent, irreversible conversion from token to compute.
5. **Governance.** ATN uses ERC20Votes, enabling delegation and on-chain voting weight.
6. **Investment.** Users back projects with ATN, receiving project tokens that entitle them to inference discounts and revenue share.

### 4.2 One-Way Mint

ATN enters circulation through a one-way conversion from governance tokens (RepToken). Participants in the parent jurisdiction earn RepTokens through governance participation. These can be permanently converted to ATN through the `Autonet.mintFromRep()` function. The conversion is irreversible — ATN cannot be converted back to RepTokens.

This creates a value flow: governance participation → reputation → ATN → network utility. The one-way nature prevents arbitrage and ensures that ATN supply reflects genuine governance engagement.

The DAO can also mint ATN directly, but this requires a governance proposal evaluated by the RPB. No admin key exists. Supply expansion is a collective decision.

### 4.3 Inference Credits

The mechanism that gives ATN intrinsic utility: burning ATN for inference credits.

```solidity
function burnForInference(uint256 amount) external {
    atnToken.burnFrom(msg.sender, amount);
    inferenceCredits[msg.sender] += amount;
    totalInferenceBurned += amount;
}
```

This is not a fee — it is a burn. The ATN is destroyed. Credits are used to query published models through `requestInference()`. The burn creates permanent deflationary pressure proportional to network usage. As inference demand grows, ATN supply contracts. The remaining ATN represents a larger share of the network's computational capacity.

### 4.4 Epoch Rewards

Training participants earn rewards from epoch pools. The reward calculation incorporates:

- **Exponential decay.** Earlier epochs have larger reward pools, incentivizing early participation.
- **Capability weighting.** The CapabilityScorecard applies multipliers based on training module gaps. A module at 20% of its target capability might offer 2.5x rewards; a module at target offers 0.5x. This directs training effort toward the network's weakest capabilities.
- **Usage attestation.** Services receive rewards proportional to attested usage, verified on-chain.

The design avoids common tokenomic failures: there is no yield farming (rewards require actual work), no unbounded inflation (decay converges), and no rent-seeking (idle stake earns nothing).

### 4.5 Project Economics

Projects create a secondary token economy. A project funds development through ATN contributions, issuing project tokens (PT) to backers. PT holders receive:

- Discounted inference on the project's published models (tiered by holdings)
- Revenue share from inference fees paid by non-PT holders
- Governance weight over project-specific decisions (training parameters, model architecture, data sources)

This aligns incentives between funders and users. Funding AI development is not speculative — PT holders get concrete utility through cheaper access to the models they funded.

### 4.6 The Subsidy/Premium Gradient

When emergent alignment pricing is active, ATN economics incorporate alignment gradients:

- **Aligned work → subsidized.** Operations aligned with the user's published standards and jurisdiction norms receive subsidies from the treasury. In mature networks, highly aligned work approaches zero cost.
- **Neutral work → base cost.** Standard pricing.
- **Misaligned work → premium.** Operations that conflict with published standards pay premiums. Premiums fund the treasury that subsidizes aligned work.

The gradient is continuous, not binary. The network is not a censor — it is a market that prices externalities. Misaligned work is expensive, not prohibited.

---

## 5. Emergent Alignment

### 5.1 Standards Publication

Users publish their values on-chain through their `AutonetUser` contract. The contract stores:

```solidity
contract AutonetUser {
    address public owner;
    address public autonet;
    bytes32 public standardsHash;     // Hash of published standards
    uint256 public alignmentScore;    // 0-10000 basis points
    mapping(string => string) public preferences;
}
```

Standards are arbitrary text: goals, values, interests, principles. The hash is published on-chain; the full text is stored off-chain (IPFS or blob store). This preserves privacy while enabling verification — anyone can check that a user's claimed standards match their published hash.

### 5.2 Semantic Distance Scoring

The alignment mechanism operates at three levels:

1. **User-to-jurisdiction:** How closely do the user's standards align with the jurisdiction's constitutional standards? This is scored at onboarding and affects the cost of publishing standards. Highly misaligned standards cost more to publish.

2. **Task-to-user:** How closely does a specific task align with the user's published standards? Computed locally by the user's node.

3. **Task-to-jurisdiction:** How closely does the task align with jurisdiction norms? Cross-referenced against the constitutional standards.

Composite alignment is the geometric mean of all three scores:

```
alignment = (user_jurisdiction × task_user × task_jurisdiction)^(1/3)
```

The geometric mean ensures that all three dimensions must be reasonably aligned. A task perfectly aligned with user standards but violating jurisdiction norms still scores poorly.

### 5.3 The Pricing Function

The core mechanism is a pricing function that creates continuous economic pressure toward alignment:

```python
def compute_inference_price(task_goal, user_standards, jurisdiction_standards,
                            treasury_balance, network_maturity, base_cost):
    # Compute alignment scores (0-1, higher = more aligned)
    user_to_jurisdiction = semantic_similarity(user_standards, jurisdiction_standards)
    task_to_user = semantic_similarity(task_goal, user_standards)
    task_to_jurisdiction = semantic_similarity(task_goal, jurisdiction_standards)

    # Composite alignment (geometric mean)
    alignment = (user_to_jurisdiction * task_to_user * task_to_jurisdiction) ** (1/3)

    # Subsidy capacity increases with network maturity and treasury
    max_subsidy_rate = min(network_maturity, treasury_balance / TREASURY_THRESHOLD)

    if alignment > 0.8:    # Highly aligned → subsidized
        subsidy_rate = max_subsidy_rate * ((alignment - 0.8) / 0.2)
        user_pays = base_cost * (1 - subsidy_rate)
    elif alignment > 0.5:  # Neutral → base cost
        user_pays = base_cost
    else:                  # Misaligned → premium
        premium = 1 + (0.5 - alignment)  # Up to 1.5x
        user_pays = base_cost * premium
    return user_pays
```

Four properties make this function robust:

1. **Continuous.** No binary allow/deny. Everything is priced on a gradient.
2. **Subsidy-capable.** Highly aligned work can reach zero cost in mature networks.
3. **Self-funding.** Misalignment premiums directly fund alignment subsidies.
4. **Governable.** All parameters (thresholds, max rates, treasury capacity) are set by DAO governance.

The subsidy capacity is deliberately constrained by two factors: network maturity (preventing premature subsidy commitments) and treasury balance (preventing insolvency). A young network with an empty treasury subsidizes nothing. A mature network with a full treasury can subsidize up to 100% of aligned work. The transition is smooth and market-driven.

### 5.4 Economic Enforcement

In the current phase (centralized inference), alignment checking is advisory. The user's node evaluates alignment locally, but pricing is uniform. The economic gradient applies to standards publication cost and reputation effects.

In the decentralized inference phase, the network enforces differential pricing. The user's node computes alignment locally and reports only the score — not the task content — to the network. The network sets the inference price based on the score. Privacy is preserved: the network never sees what the user is computing, only how aligned it claims to be.

Gaming prevention relies on consensus-based integrity verification:

- **Yuma consensus validation:** Peer nodes independently verify outputs. Tampered alignment scores diverge from peer consensus over time, reducing bond weight.
- **Stake-backed honesty:** Detected divergence results in slashing.
- **Forced error injection:** The `ForcedErrorRegistry` (`0x290Fc505782E6b70A4c57A3cECc6Ad109466520e`) periodically injects known-incorrect results. Nodes that fail to catch deliberate errors are penalized.
- **Statistical anomaly detection:** Always-perfect alignment scores trigger multi-coordinator review.

### 5.5 The Key Insight

The system makes aligned work progressively free. As the network matures and the treasury grows (funded by misalignment premiums and network fees), subsidies increase. In the limit, work that serves the collective good costs nothing to execute.

This inverts the alignment problem. Instead of constraining AI to prevent harm, the architecture creates economic conditions where beneficial AI work is the cheapest option. The network does not need to define "good" centrally — users define their own standards, the jurisdiction defines its norms, and the market finds equilibrium.

Misaligned work is not prohibited. It is expensive. The premium funds the subsidies. The system is self-financing: the more misaligned work the network processes, the more resources it has to subsidize aligned work. And as aligned work becomes cheaper, demand shifts naturally toward it.

### 5.6 Trustless Enforcement

Alignment pricing is meaningless without enforcement. In traditional commerce, contract enforcement rests on the coercive power of the state: courts, sheriffs, garnishment. AI agents operating across decentralized infrastructure have no relationship to any of these institutions.

Autonet substitutes cryptoeconomic enforcement for legal enforcement. The mechanism operates at multiple levels:

**Escrow.** Project funding is held in smart contracts, not bank accounts. Disbursement requires on-chain conditions to be met (task completion, coordinator consensus, aggregation). No party can unilaterally seize funds.

**Reputation.** Every on-chain action creates a permanent, auditable record. Coordinator EMA bonds track historical accuracy. Provider reputation scores reflect verification success rates. Solver history is public. Reputation is earned through behavior and cannot be purchased or transferred.

**Slashing.** Stake is at risk. Coordinators who vote against consensus lose 10%. Providers who serve invalid data lose their full stake. The economic loss from dishonest behavior is immediate, automatic, and proportional. No court filing required; no appeal; no delay. The smart contract is judge, jury, and executioner.

**Forced errors.** The ForcedErrorRegistry periodically injects known-bad results into the verification pipeline. This is the equivalent of a regulatory audit, but automated and continuous. Coordinators who rubber-stamp results will eventually approve a forced error, revealing their negligence and triggering slashing. The system tests its own integrity continuously.

Game-theoretic simulation of this enforcement architecture (detailed in the Stanford JBLP submission) demonstrates 66.3% dispute-free completion with a 4.8% "enforcement premium" relative to traditional legal systems — the cost of operating without state-backed courts. This premium is the price of permissionless global participation: anyone can join without trusting any particular jurisdiction's legal system.

---

## 6. Distributed Model Infrastructure

### 6.1 Model Sharding

Trained models are not stored on a single server. The `ModelShardRegistry` breaks models into shards distributed across staked storage providers.

A model is registered with its Merkle root:

```solidity
function registerModel(
    bytes32 modelId,
    bytes32 merkleRoot,
    uint256 totalShards,
    uint256 kRequired,
    ShardingStrategy strategy
) external
```

The `kRequired` parameter specifies the minimum number of shards needed for reconstruction. With erasure coding (default: 10 data + 4 parity), the model survives the loss of up to 4 providers without data loss.

Providers announce shard availability and submit Merkle proofs for verification. The contract tracks provider reputation: successful verifications increase reputation, failures decrease it and trigger recovery. Providers must be staked — the stake is slashed for serving invalid data.

Three sharding strategies address different architectures:

- **LAYER_WISE:** Each shard contains complete layers. Suitable for feedforward networks and CNNs where layers are independently meaningful.
- **TENSOR_PARALLEL:** Shards contain slices of individual tensors. Required for large language models where single layers exceed individual node capacity.
- **REPLICA:** Full model copies. Higher redundancy, suitable for popular models with high query volume.

### 6.2 Guild System

Nodes organize into guilds — groups specializing in specific training modules. The guild system enables hierarchical aggregation:

1. **Intra-guild aggregation:** FedAvg within the guild, combining updates from guild members who trained on the same module.
2. **Network-level aggregation:** Guild-level models are merged at the network level, weighted by guild reputation (30%) and member count (70%).

```yaml
guild:
  aggregation_level: guild  # flat | guild | network
  min_guild_updates: 2
  reputation_weight: 0.3
  member_count_weight: 0.7
```

Guilds create specialization without centralization. A guild focused on vision models accumulates expertise and reputation in that domain. Its aggregated updates carry more weight in network-level merging for vision modules, less for other domains. Knowledge is distributed but expertise is concentrated where it's most effective.

### 6.3 Peer-to-Peer Network

Nodes communicate through a libp2p-based P2P layer. The configuration supports:

```yaml
p2p:
  listen_port: 0              # 0 = random port
  bootstrap_peers: []         # multiaddr strings
  enable_quic: false
  capability_advertise_interval: 60   # seconds
  ping_interval: 30                   # seconds
```

Nodes advertise their capabilities (training modules, available compute, storage capacity) at regular intervals. The capability advertisement feeds the guild system — aggregators discover which solvers belong to which guilds based on their advertised module specializations.

Bootstrap peer discovery uses standard libp2p multiaddr format. Once connected, nodes participate in a Pastry DHT for content routing. Model shards, task specifications, and training checkpoints are all retrieved through the DHT using content-addressed identifiers.

### 6.4 Privacy Architecture

Privacy operates at two levels:

**Training data privacy.** Solvers train on local data. No training data leaves the node. Only model weight updates are shared — gradients, not data. This is inherent to federated learning and requires no additional privacy mechanism. The network never sees what a solver trained on; it only evaluates the quality of the resulting model.

**Task content privacy.** When a user requests inference, the task content stays on the user's node. The alignment evaluation is performed locally. Only the alignment score is reported to the network for pricing. The user configures privacy zones in their node:

```yaml
privacy:
  exclude_apps: []              # Window titles to skip
  blur_regions: []              # Screen regions to always blur
  scrub_pii: true               # Redact emails, phone numbers, credit cards
```

The scrub_pii flag enables automatic redaction of personally identifiable information from any data that leaves the node. This is a belt-and-suspenders approach: even if a privacy boundary is accidentally breached, PII is scrubbed before transmission.

---

## 7. Deployment

This system is deployed and operational. The following contract addresses are live on Etherlink Shadownet (chain ID 127823, RPC: `https://node.shadownet.etherlink.com`):

| Contract | Address |
|----------|---------|
| ATNToken | `0x6e82D6678790820Ef81669046e921b1D2947A08f` |
| ParticipantStaking | `0x8B08279cf510BfeB6acE6BA5282BF0e4F6eBD8EE` |
| ModelShardRegistry | `0x7De3B8a6bc4eB7f098018Da030f93718eeaf7885` |
| Project | `0xC309f344e652E023b15BAF578089Aa90a9F5AF9B` |
| TaskContract | `0x8fEb5be0367F596bC6357538e346472eBf76D365` |
| ResultsRewards | `0x1ef4e0A6DaC1CFD23E31427b2Ecdd2A6A0F0f542` |
| AnchorBridge | `0x2005556109607F5b11BaCAd05270E7DE32260B4D` |
| DisputeManager | `0xB1Cf18A50bA3fffD578D2b2B08Ea2D03A8Aa2a3b` |
| AutonetDAO | `0xD0271E6d7710F0bF59Dc8720306224Cc6ddf503f` |
| ForcedErrorRegistry | `0x290Fc505782E6b70A4c57A3cECc6Ad109466520e` |
| InferenceProviderFactory | `0xf8246D4E4668EaC14aA508Daa02EFb60099699BF` |
| Autonet | `0x97EB727426f593B2E2bC64F1604b5E7fE2eF676b` |

Deployer: `0x06E5b15Bc39f921e1503073dBb8A5dA2Fc6220E9`
Deployment timestamp: `2026-03-23T00:49:24.621Z`

### 7.1 What Works Today

**Complete training loop.** The Absolute Zero loop runs end-to-end with real PyTorch models. A multi-node orchestrator spawns proposers, solvers, coordinators, and aggregators, runs training cycles, and produces verified aggregated models. Both supervised (CNN/MNIST) and self-supervised (JEPA/CIFAR-10) training paths are operational.

**On-chain coordination.** All thirteen Hardhat tests pass. Task proposals, solution commitments, coordinator voting, Yuma consensus, reward distribution, and model publication are verified on-chain.

**Distributed model storage.** ModelShardRegistry with Merkle proof verification, erasure coding, and provider reputation tracking is deployed and tested.

**Agent framework.** The ATN runtime manages node orchestration, WebSocket API for real-time control, voice integration, and provider management.

**Web interface.** The Flutter frontend is functional with three visualization systems (Goal Map, Novelty Map, Training Brain), earnings tracking, governance panels, and node control surfaces.

### 7.2 What the Deployment Demonstrates

The deployment proves a structural claim: decentralized AI training with cryptographic verification, constitutional governance, and economic alignment is not a theoretical possibility. It is an engineering problem, and the engineering is done.

The system handles the full lifecycle: a user funds a project, a proposer creates training tasks, solvers train real neural networks, coordinators verify results through stake-weighted consensus, aggregators combine verified updates, and the resulting model is published on-chain for inference. At every step, the constitution constrains behavior, the economics incentivize honesty, and the cryptography prevents cheating.

---

## 8. Implications

The architecture described in this paper makes several things structurally true:

**No single entity controls AI training.** Training tasks are proposed by staked participants, executed by independent solvers, verified by distributed coordinators, and aggregated through Byzantine-resistant algorithms. Compromising any one participant affects at most one training contribution. Compromising the training pipeline requires simultaneous control of proposers (to direct training), solvers (to execute it), and coordinators (to verify it) — each requiring separate stake deposits subject to slashing.

**Users govern their own AI.** Published standards create a direct channel from human values to AI behavior. The user's contract stores their values on-chain; the alignment engine scores operations against those values; the economic gradient subsidizes aligned work and premiums misaligned work. The user does not need to trust the AI provider — the governance is cryptographic.

**Economic incentives align AI behavior with human values.** This is the emergent alignment thesis. Alignment is not a constraint imposed on AI by its creators. It is an economic equilibrium that emerges from the interaction of user standards, jurisdiction norms, and market pricing. The system does not need to solve the alignment problem in the philosophical sense — it creates conditions where aligned behavior is cheaper than misaligned behavior, and lets economics do the rest.

**The network can evolve but cannot violate its constitutional foundation.** Evolution proposals pass through RPB evaluation against immutable principles. The system can upgrade its training protocols, adjust its economic parameters, adopt new consensus mechanisms — but it cannot abandon human rights protections (P3), remove transparency requirements (P5), or concentrate economic power (P6). The constitution is a ratchet, not a cage. It constrains the direction of change without constraining the rate of change.

**The transition from human execution to human governance is economically smooth.** In early network stages, users pay for inference. As the network matures and the treasury grows, aligned work is increasingly subsidized. In the limit, work that serves collective human values costs nothing to execute. The human role shifts from performing work to governing what work gets performed — from laborer to sovereign. The economic transition is gradual, governed by treasury capacity and subsidy parameters, controlled at every step by DAO governance.

**The peaceful transfer of work.** The standard narrative around AI and work is adversarial: AI takes jobs. This framing assumes zero-sum competition. The real danger is not competition itself but the structural forms that unmanaged automation takes. Two failure modes:

*Consolidation trap:* AI service providers consolidate, maximizing model performance while undercutting human labor costs. Supply-side monopoly emerges. The work transfers, but the value concentrates in a small number of entities.

*Dependency trap:* Governments respond with universal income for displaced workers. But the authorities dispensing that income are centralized entities subject to intentional and accidental failures. Few will feel comfortable with a livelihood dependent on a handout from central authorities.

Both traps share a root cause: the absence of an economic framework that distributes the earnings of machine intelligence to those who govern its operation. Autonet provides that framework. The transition through four phases:

| Phase | Human Role | AI Role | Economic Model |
|-------|-----------|---------|----------------|
| Early | Execution + oversight | Assistance | Users pay for inference |
| Middle | Oversight + governance | Task execution | Partially subsidized |
| Mature | Goal-setting + governance | Most execution | Aligned work subsidized |
| Late | Governance participation | Nearly all execution | Treasury funds aligned work |

The transition is peaceful because: humans retain control through governance of standards; the transition is gradual (subsidies increase with network maturity); economic incentives align throughout (aligned work is rewarded, not just permitted); and exit is possible (fork the jurisdiction if you disagree with its standards).

This is what the architecture is for. Not to build AI that obeys commands, but to build infrastructure where AI development is governed by the people it serves, aligned through economics rather than constraints, and bounded by constitutional principles that cannot be removed by those in power. The system exists. The contracts are deployed. The training loop runs. What remains is scale.

---

**Autonet** — https://autonet.computer
**Source** — https://github.com/autonet-code
**Network** — Etherlink Shadownet, Chain ID 127823
