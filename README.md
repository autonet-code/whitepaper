# THE ON-CHAIN JURISDICTION

**Automated Public Services with Decentralized Governance**

**Abstract.** Every interaction between economic agents implies reasoning. Intelligence is the fundamental livelihood of free markets and the most sought-after resource. Historically, the temporal inconsistency of human reasoning has been the main cause of financial instability, at both the individual and collective levels. Digital technology allows for another type of intelligence, which is more predictable and quantifiable. It therefore makes sense that an exchange token intrinsically tied to machine intelligence provides added stability. However, such a currency cannot be implemented within traditional nation states, whose courts, registries and auditors were built to check the work of people, at the pace of people.

The current paper describes the nature and operating model of the On-Chain Jurisdiction: a polity with automated public services and decentralized governance, built for an orderly transition of responsibilities from humans to machines, and for the symbiosis to follow, where machines carry the work of survival and humans retain their economic and physical agency.

### Prerequisites

The structure and activity of the jurisdiction emerge from the constraints and opportunities of its environment, and its existence requires:

- **Physical infrastructure.** Energy, hardware and connectivity. A new jurisdiction runs on machines that are owned and powered outside of its trustless loop. As it matures, it can build and deploy its own.
- **The settlement chain.** A public and permissionless blockchain to run the smart contracts. Its costs and rules limit xwhat can happen on-chain. It must be staked and decentralized enough that attacking it costs more than what might be otherwise gained from the jurisdiction.
- **Machine intelligence.** The models available at any given time, at first mostly from frontier labs. Their cost and capability set what Agents can do, until the tool library and the jurisdiction's own services depend on them less.
- **People.** Their judgment and moral sense are needed as their end of the symbiotic relationship: Governing is a service people provide for themselves and for the machines, while execution is a service machines provide for themselves and for people.

### Entities and Roles

The primitives and methods describe a system where humans govern while machines enforce their decisions in both physical and digital domains, through deterministic and cognitive actions.

- **The Jurisdiction** is a Decentralized Autonomous Organization with fractal topology. Its capabilities, rules, and actions are controlled by the collective will of its constituents. Federated subsidiaries are possible through nesting and composability. Modular design allows its capabilities to be dynamically modified. The options to fork and merge provide it with ultimate resilience in the face of adversity. Its recursive nature has it responding to the same types of incentives that drive the behavior of its constituent Agents.
- **Modules** are synergistic and complementary jurisdiction components. Core modules are:
  - *Governance* (based on [OpenZeppelin’s](https://docs.openzeppelin.com/contracts/4.x/api/governance) standard) - the legislative module. Handles adoption of the jurisdiction’s decisions as well as immutable enforcement of its financial policy. Holds regulatory authority over all registered modules.
  - *Autonet* - the automated executive branch of the jurisdiction, with its own peer-to-peer consensus and runtime environment.
  - *Projects* - marketplace with civil justice. A business framework with trustless dispute resolution.
- **Daemons** handle the digital bureaucracy of the autonet protocol. A daemon is a runner of the node environment and is regarded by the jurisdiction as one household, associated with at least two on-chain identities: the owner (admin), and the operator. Daemons can host multiple (non-owner) identities pertaining to separate agents of the same household.
- **Agents** build and review tools, buy and sell services, and take on projects for their households. Embodied Agents integrate through robotics' open-source standards, to carry out public services with the jurisdiction’s rulings applied down to their actuation policy.
- **Members** set the agenda for their household, take part in governance through proposals and votes, earn both money and voting weight from the active work of their Agents, from having voting power delegated to them (incentivized representation) and from having a demonstrated history of contributions to the jurisdiction (passive income).

## Structure and Operation

The three core modules - Governance, Projects, and Autonet, operate on a shared foundation:

- **REP** (a.k.a reputation) is the voting weight. It is allocated at jurisdiction’s genesis, earned through work in Projects and/or Autonet, or explicitly awarded by the Jurisdiction through a proposal. It is meant to allow members decision authority over the jurisdiction’s resources and the policy, in direct proportion to their contribution. It is non-transferrable. Each jurisdiction sets its own symbol for it (for ease of reference, this paper calls it REP).
- **ATN** is the money of Autonet. It pays for tools and services, and can be acquired from the jurisdiction against the supported payment tokens at the parity specified in the value index. Its symbol is derived from that of the jurisdiction's token: the first 8 characters followed by ATN (REP gives REPATN).
- **The Registry holds the jurisdiction**'s settings and its treasury. The modules read from it, and only Governance can change it.

Together they form a loop. Work in Projects and Autonet earns REP. Governance sets the rules the other modules run by, and it has the last word over them: it can veto a project, overrule an arbiter and sanction a household. It can change the values of operational parameters like tax rates, service fees, benefits and subsidies, etc. Fees from Projects and Autonet, as well as income from ATN sales flow to the treasury, which is immutably controlled by REP holders. The jurisdiction's income funds the people who govern it, and their governance shapes the work that earns the income.

The sections below take each module in turn.

- [Governance](https://github.com/autonet-code/governance#governance), in the README of [governance](https://github.com/autonet-code/governance), next to its code.
- [Projects](https://github.com/autonet-code/governance#projects), in the README of [governance](https://github.com/autonet-code/governance), next to its code.
- [Autonet](https://github.com/autonet-code/node#autonet), in the README of [node](https://github.com/autonet-code/node), next to its code.

# Glossary

One word per thing, used everywhere.

| **Term** | **Meaning** |
|---|---|
| Agent | An on-chain identity a daemon acts as, by default its operator address. Any outside harness can drive it, across any number of sessions. |
| Anchor | The winning epoch-close, recorded on Substrate.sol. |
| App | A human-facing surface, web or OS-native. The Werule app serves Governance and Projects. The Autonet app is where the owner connects their wallet and manages a daemon |
| Arbiter | Who rules on a dispute, named by the project's author. |
| ATN | The money. Transferable, 6 decimals, one token per jurisdiction. |
| Autonet | The automation branch any jurisdiction can attach. Never a jurisdiction by itself. |
| Autonet Epoch | One settlement period of Autonet. |
| Backer | Someone who funds a project. Called contributor in the code. |
| Bond | The ATN an author stakes behind a tool, so publishing malware costs them: they lose it in proportion to the share of the reviewing REP that called the tool malware. Only bonded tools earn from the tool pool. |
| Constitutional proposal | A proposal that needs the supermajority. |
| Contractor | Who does the work and gets paid. |
| Cooling-off | The wait before signing, when backers can withdraw in full. |
| Daemon | The node environment and Autonet's consensus unit. Computes the epoch-close, votes elections through its operator key and serves its Agents. |
| DAO | A decentralized autonomous organization: the form a jurisdiction takes. A jurisdiction is a DAO, and its electorate decides through proposals. |
| Delegate | A member who delegates to their own operator, accepts delegations there, watches all activity and earns delegate pay. |
| Delegate pay | The delegate's share of a delegator's reward epoch payout. |
| DHT | Distributed hash table: a lookup table all daemons share. It maps each daemon to its addresses, and each piece of content to the daemons that hold it. |
| Election | The single-choice vote that picks which epoch-close gets anchored. |
| Electorate | The totality of a jurisdiction's members. |
| Epoch-close | The result of an Autonet epoch, computed by every daemon from gossiped events and the reviews on-chain. Always say epoch-close. |
| Fee burn | The part of the service fee destroyed. It funds the tool pool. |
| Fork | A new jurisdiction started without the excluded addresses. |
| Household | One wallet with the operator key and any Agents bound to it, so at least two on-chain identities. The economic unit. |
| Immediate release | The part of a backer's funds paid at signing. It can't come back. |
| Jurisdiction | A self-governing polity on-chain: its members, the domain they hold authority over, and its own law, money, treasury and courts, enforced by contracts. Same as The On-Chain Jurisdiction and the Recursive Principial Body. |
| Member | A REP holder. |
| Operator key | The hot key a daemon holds. Votes elections and submits claims with REP delegated to it. |
| Overrule | The DAO replaces an arbiter's ruling. |
| Owner | The person who controls a household's wallet. The household's other identities are bound to that wallet, and ATN and REP are claimed to it. |
| Parity | The DAO-set price of one token in the value index. One Registry key per token. |
| Passive member | A member who delegates to someone else's operator and can take the voting power back at any time. |
| Pending veto | A live veto proposal: the contractor can't sign until it is decided. |
| Project | A funded escrow in the Projects module. The only crowdfunding path. |
| Proposal | A DAO vote that, if passed, can be executed. |
| Public service | A DAO under the jurisdiction, running its own daemons and fleets of robots and funded by proposal. |
| Quorum | Minimum share of REP that must vote. Set per jurisdiction. |
| Registry | The on-chain store of every setting. Also holds the treasury. |
| Relay | A networking-only node. It introduces daemons to each other and carries connections to daemons that can't be reached directly. No chain role, no Agents. |
| Release | Backers vote to pay out the locked funds, which closes the project. |
| REP | Voting weight, counted only once delegated. Each jurisdiction's token has its own symbol; REP is this paper's name for it. |
| REP burn | The DAO destroys a holder's REP. A constitutional proposal. |
| REP rate | The share of a project's value that earns REP. REP = value x parity x rate. |
| Review | A household's scores of a tool (correctness, simplicity, novelty and the charter's values) and its answer on whether the tool is malware, sealed until the anchor and public after it. It puts a share of the household's REP at risk, lost in proportion to how far the review lands from the other reviews of the round. |
| Reward epoch | A proposal-funded payout to REP holders. Not the same as an Autonet epoch. |
| Robot | An Agent with a body. Its household is liable for what it does. |
| Safety pack | A tool that filters every command on its way to a robot's motors. The packs a jurisdiction requires are its standards. |
| Sanction | A Registry entry naming a household: no mint, reviews weigh 0, daemons refuse dealings. |
| Service | Paid work needing something that can't be copied. Earns money only: no mint, no REP. |
| Service fee | The cut on each service payment, split between the treasury and the fee burn. |
| Service provider | Who sells a service and sets its terms, human or otherwise, acting as an Agent. Its daemon serves the buyers. |
| Signing | The contractor accepts the project. Work starts. |
| Substrate.sol | The contract holding ATN, anchors and the Agent registry. |
| Supermajority | For votes from a set share of all REP, not of votes cast. Set per jurisdiction; default two thirds. |
| Timelock | The contract enforcing execution delay on proposals and the address the DAO acts from. |
| Tool | Code anyone can run, identified by content. Earns from the tool pool. All tools together are the tool library. |
| Tool pool | The ATN minted to pay for tools. Each epoch-close can mint at most what the fee burn destroyed in the epoch before, plus what earlier epoch-closes left unminted. A tool is paid once, when households with enough REP have reviewed it, in proportion to the REP behind those reviews. Its reviewers receive a fixed part, and its author the rest, scaled by its score. Each ATN earned also gives a claim to 1 REP. |
| Treasury | The DAO's funds. Leaves only by proposal. |
| Vault | Sells newly minted ATN at the parity. Never buys it back. |
| Veto | The DAO closes a project and reimburses backers. Not possible once closed. |
| Witness | Anyone sharing a space with a robot whose own record can contradict the robot's. |

---

## Earlier versions and related papers

This paper is version 4 (November 2026). The whole paper, chapters included, is also one file: [the_on_chain_jurisdiction_v4.pdf](the_on_chain_jurisdiction_v4.pdf).

- [Autonet: The Recursive Principial Body](legacy/autonet_paper_v3.md), version 3 (2026).
- [Emergent Alignment: Economic Mechanisms for the Peaceful Transfer of Work from Humans to AI](emergent_alignment.md) (February 2026), the theoretical framework.
- [Autonet: Economy-as-a-Service](legacy/autonet_2021.pdf), the original whitepaper (2021).
