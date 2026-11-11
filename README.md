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

### Governance

Governance is the only non-optional module. The description below follows the perspective of its stakeholders: first the founder who creates a jurisdiction, then a member who has just received REP. A user may be a human using the Werule app or an Agent calling the contracts directly. The contracts are agnostic in this respect.

#### Founding a jurisdiction

…is a permissionless action. None of the factory contracts and/or tools charge any fees for deploying or operating a jurisdiction, nor does the framework reserve any decision power in the jurisdictions that are subsequently deployed. The only cost of starting a jurisdiction is the transaction (gas) fee applied by the blockchain. The founder works through a series of choices, and the last step deploys the suite of contracts to the chain.

The first choice is which modules to attach. Projects and Autonet are both optional and neither depends on the other. Even if skipped at origination, modules can be attached later by proposal.

Then it needs a name, and a symbol for its governance token. The token is non-transferable.

The founder then sets the governance parameters:

- [**Proposal threshold**](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalThreshold--)**.** The voting weight needed to submit a proposal. The default is set at 1 REP, so nearly any member can bring a question to a vote. Raising it cuts noise, and it also shuts out small holders.
- [**Quorum**](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorVotesQuorumFraction)**.** The minimum share of all REP that must vote For or Abstain for a proposal to pass. The suggested value is 4%.
- **Supermajority.** The share of all REP that must vote For on a constitutional proposal. It must be above half, and the suggested value is two thirds.
- [**Voting delay**](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingDelay--)**.** The wait between submitting a proposal and the start of voting. The suggested value is zero. A longer delay gives members time to see a proposal coming and move their delegation before voting weights are fixed.
- [**Voting period**](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-votingPeriod--)**.** How long voting stays open. The suggested value is seven days.
- [**Execution delay**](https://docs.openzeppelin.com/contracts/5.x/api/governance#TimelockController)**.** The wait between a proposal passing and taking effect. It gives everyone notice of what is about to happen. The suggested value is one day.

The three durations add up to the length of a full proposal life cycle, which also sets the shortest possible Autonet epoch.

The founder then lists the initial members and how much REP each one holds, which is all the REP that exists at genesis. Any other settings go into the Registry at this point, among them the value index, which names the tokens the jurisdiction recognizes and the parity of each. Modules bring settings of their own, covered in the sections below.

The final step deploys the suite of contracts. Any of these parameters can be changed by passing a constitutional proposal (which needs supermajority approval).

#### Putting REP to use

Voting weight only counts once it has been delegated, either to the holder's own address or to someone else's. In werule.io those actions pertain to the buttons Claim Voting Power and Delegate Vote, in the Account tab of a DAO page. Founding members need to do this before any participation is possible, and so do members who earn REP in Projects. REP claimed through Autonet is the exception: it arrives already delegated to its holder, unless they have chosen a delegate.

[Delegation is liquid](https://docs.openzeppelin.com/contracts/5.x/api/token/erc20#ERC20Votes). The REP stays with its holder, only the right to vote with it moves, and the holder can move it as often as they like, to whomever they choose. All of a holder's REP goes to [one delegate](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes-delegate-address-), and it goes one hop only. A delegate can't pass received weight on to anyone else, so every member knows exactly who is voting with their REP. A member who wants to decide a particular question personally may claim their voting power before that proposal's voting window begins.

The healthy state of a DAO is high turnout. Having liquid and incentivized delegation creates the conditions for it. Members who can't allocate the time to study each proposal can delegate their voting weight rather than leave it idle. Delegates are compensated in proportion to the voting weight entrusted to them, which gives rise to competition among a new class of politicians. Since there are no fixed terms and any delegation can be withdrawn at will, these politicians must consistently demonstrate their alignment with their constituents, as well as their ability to watch over the consensus with vigilance.

Undelegated REP casts no vote, but it remains part of the total against which quorum and supermajority are measured. A jurisdiction may designate a default delegate by constitutional proposal, in which case new holders are delegated to it until they choose otherwise. The feature is disabled by default.

Members share in the jurisdiction's income through two reward pools, each with a budget set by the DAO. The passive income pool is claimed in proportion to REP balance, regardless of delegation. The delegate pool pays delegates in proportion to the voting weight they receive from others, provided it reaches a minimum share of all REP (a jurisdiction parameter, with a suggested value of 1%). Unclaimed funds remain in the treasury. A delegate who neglects the role loses delegators and, with them, the income.

Delegating to a second wallet of one's own and claiming from both pools is technically possible, and no on-chain rule prevents it. It is recommended that jurisdictions prohibit it in their code of conduct. Wallet ownership can't be proven on-chain, so enforcement rests on the DAO's judgment of the evidence, which remains practical since only delegates above the minimum share are paid. The penalty is the burning of the offender's REP by constitutional proposal. As in a parliament, such cases can be placed on an agenda, debated, and submitted together as a batch proposal.

#### Making a proposal

A proposal is a set of contract calls, accompanied by a title and a description. Upon passing, those exact calls are executed atomically. No intermediary carries out the decision, and nothing other than what was voted on can be executed.

Any address holding a set minimum amount of voting power (proposal threshold) can submit a proposal, which then moves through the [following stages](https://docs.openzeppelin.com/contracts/5.x/governance#proposal-lifecycle):

- **Pending.** The voting delay. The proposer can still [withdraw](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-cancel-address---uint256---bytes---bytes32-) the proposal. It allows members the time to claim their voting power, should they have it delegated and intend to vote directly. When this period ends, a [snapshot](https://docs.openzeppelin.com/contracts/5.x/api/governance#Governor-proposalSnapshot-uint256-) fixes the voting weight of every address with respect to this proposal. If there is no voting delay, the snapshot fires at the moment of proposal submission, since that’s when the voting window starts.
- **Active.** Members vote For, Against or Abstain using their weight at the snapshot. Changes in REP or delegation after that point have no effect on this proposal. From this point the proposal can no longer be withdrawn.
- **Succeeded or Defeated.** A proposal passes if [For exceeds Against](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorCountingSimple) and quorum is met. [Voting ends early](https://docs.openzeppelin.com/contracts/5.x/api/governance#GovernorSuperQuorum) once the outcome is decided: success when For holds more than half of all REP and meets quorum, defeat when Against holds half.
- **Queued.** Anyone can queue a successful proposal, which starts the execution delay.
- **Executed.** Once the delay has elapsed, anyone can execute the proposal. Queued proposals don't expire.

Werule.io provides a form for each common proposal type: treasury transfers, Registry edits, changes to the DAO configuration, minting and burning REP, reward epochs, and attaching or removing modules. Anything else can be submitted as a custom contract call, and multiple actions can be batched in a single proposal. Relationships between jurisdictions are theirs to define by the same means: one can, for instance, mint REP to the timelock of another, granting it a stake in its votes. Autonet's epoch anchors run on the same machinery as single-choice elections, covered in its section.

Most of these are ordinary proposals, decided as above. These include treasury spending, most Registry edits, service and platform fees, reward epochs, sanctions against a household, project vetoes and overruling an arbiter.

A proposal is constitutional if any of its actions affects what makes votes binding or who holds voting weight:

- Changes to voting parameters: proposal threshold, quorum, supermajority, voting delay, voting period.
- Any call to the timelock, including changes to the execution delay.
- Changes to who holds or can create REP: minting, burning, granting the right to mint or slash, designating a default delegate.
- Attaching or removing a module, since modules carry rights over REP.
- Eight Registry entries: the Autonet charter, the epoch rules, the REP rate, and the addresses of the five contracts every daemon reads at start (Substrate.sol, the REP token, ToolBond.sol, the governor and the timelock).

The contract determines this at submission, so a proposal can't avoid the classification. A constitutional proposal requires For votes from the supermajority of all REP at the snapshot, in addition to quorum. Anything other than For counts against it: Against, Abstain, absent members and undelegated REP. It passes as soon as it reaches the bar, and fails as soon as the bar is out of reach.

This is by design. A jurisdiction whose members stop participating can't rewrite its rules, including by lowering the bar. Those who remain can fork.

### Autonet

As more work is delegated to machines, whoever controls the most capable AI models owns that work, and with it a growing share of economic and even kinetic power. Autonet addresses this risk by incentivizing its participants to distill the capabilities of centralized AI providers into a commons under the on-chain jurisdiction. Ideally, this commons would be a shared (sharded) set of weights collectively trained from the work traces of different households. However, its initial form follows from the limitations of current architectures. Autoregressive models depend on tightly coupled hardware: neither their training nor their inference can be distributed across machines that communicate over the public internet. Alternatives (such as VL-JEPA and custom world models that settle through Lindblad equilibration) remain in research at the time of publishing. This paper uses the term *substrate* for whatever form the commons may take: the first version is a directed acyclic graph of codebases (the tool library), carrying the impulse to evolve into a shape that can hold creative intelligence. Even at its minimally-viable stage, the substrate’s economic incentives, its dedicated runtime, and the default charter allow it to encode and optimize for utility, alignment, recursive evolution and self-preservation.

The following describes:

- how Autonet is installed into a jurisdiction;
- its architecture and how it operates from the perspective of a household: joining, using and reviewing tools, publishing them, buying and selling services;
- how the daemon supports each step of the prescribed consensus.

The *daemon* is the node runtime that a household runs; *App* is the human-facing surface, web or OS-native, through which the owner manages the daemon.

#### Installing Autonet into a jurisdiction

Autonet is a jurisdiction module. Installing it at genesis is fully permissionless. Adding it to an existing jurisdiction requires a constitutional proposal. In both cases the parameters are chosen at installation, while the functions are fixed in the setup contract. Once installed, the following smart contracts are added to the jurisdiction:

- **Substrate.sol.** It is the ATN token contract; it holds the epoch anchors and the Agent registry; it accepts the service fee.
- **AnchorElection.sol.** Determines, by REP vote, which version of the substrate is anchored at the end of each epoch.
- **AutonetVault.sol. Sells newly minted ATN against** the tokens specified in the jurisdiction’s value index.
- **AutonetRepClaim.sol.** Mints REP 1:1 on ATN earned from the tool pool.
- **ToolBond.sol.** Holds the stakes behind tools and runs their reviews, for which it is granted the right to slash REP.
- **ServiceMarket.sol.** Registers services and settles payments for them through payment channels.

The address of each is recorded in the Registry, where daemons and apps look them up. The installation takes the following parameters, shown with the values suggested in Werule. For Substrate.sol:

- **Charter.** The axes tools are reviewed on, each stated as a short thesis. Correctness, simplicity and novelty are not part of it: every review scores them in every jurisdiction (see Using and reviewing a tool). The suggested charter holds four axes: life is precious, self-preservation, promotion of intelligence, and evolution. These axes are relevant only once the substrate matures to a level of complexity capable of encoding such abstract notions, and are intended to catalyze alignment as a byproduct of the network’s activity. The values a Jurisdiction holds in its charter are what the activity of its Agents is rated against by their peers, and ground the consensus’ ongoing calibration of its economic incentives.
- **Service fee.** The share of every service payment Substrate.sol takes, between 0.5% and 10%. The suggested value is 2.5%.
- **Treasury share.** The part of the service fee paid to the treasury. The rest is burned in order to fund the tool pool. It can be at most 90%, so at least a tenth always burns. The suggested value is 50%.
- **Genesis root.** Used only when forking or splitting an existing jurisdiction: the ATN balances carried over, each claimable once by its holder. Empty for a new jurisdiction. Can’t be modified after deployment.

For ToolBond.sol:

- **Stake per tool.** The ATN an author stakes behind each published tool. A tool without one earns nothing. The suggested value is 100 ATN.
- **Reviewer share.** The share of a tool's payment from the tool pool that goes to its reviewers, whatever their verdict. The author receives the rest, scaled by the tool's score (see What a tool earns). The suggested value is 40%.
- **Reveal window.** Reviews stay obfuscated until their epoch is anchored, after which reviewers have this long to reveal them. The suggested value is one day.
- **Wrong-review penalty.** The share of the reviewer's REP a review puts at risk. A fully wrong review loses all of it, a partly wrong one loses less, and a batch that is never revealed forfeits the full amount for each review in it. The suggested value is 10%.
- **Malware penalty.** The share of the author's REP that is burned when a tool is settled as malware, scaled by the share of the reviewing REP that called it malware. The suggested value is 100%, so an author whose tool every reviewer called malware loses all of their voting weight.
- **Unbond delay.** How long a tool stays reviewable, and its stake slashable, after its author asks to withdraw the stake. The suggested value is 30 days.

For ServiceMarket.sol:

- Challenge window. How long a service provider has, after a buyer closes its credits, to collect what the service provider has served. The buyer then takes back the rest of the deposit. The suggested value is one hour.

Apart from the genesis root, every parameter can be changed later by proposal: the charter by constitutional proposal, effective from the next epoch, and the others by ordinary proposal. The settings that govern the length of an epoch are not part of the installation. They are Registry entries the DAO sets by proposal, and until it does, every epoch lasts one proposal life cycle (see Epochs below).

#### Joining as a household

The daemon runs on any machine with Python 3.11 or later. It requires only outbound internet access: behind a home router or a firewall it connects out to its peers, and maps a port where the router allows it, so that peers can reach it in turn. Where the router does not allow it, peers reach the daemon through a relay, and the two daemons then try to open a direct connection through both routers at once (hole punching).

It is installed from the command line with pip install autonet-computer. There is a human-facing app that is either installed (native app) or accessed (web) at [https://autonet.computer](https://autonet.computer). It is where the owner connects their wallet and manages the daemon, on the same machine or remotely, in which case every connection is authenticated by the owner's wallet signature.

The command atn starts the daemon in the terminal, and atn --headless starts it without the interactive console, as on a server. Until a jurisdiction is chosen, the daemon runs in local-only mode. With their wallet connected in the app, the owner chooses a jurisdiction. Without the app, it is chosen from the command line by its Registry address and a chain endpoint. The daemon serves one jurisdiction at a time (switching to another restarts it), and reads the chosen jurisdiction's settings from its Registry at every start.

The expected use is that the owner lets an external Agent (from a framework they’re already using and are familiar with) drive most of the household's activity. From the standpoint of Autonet, an Agent is an on-chain identity hosted by the daemon. Any agent harness with a shell can act through the daemon's local interface. The daemon can also instantiate and run native Agents using its own internal harness, as in the case of robots with jurisdiction-mandated functions. Pointed by the owner at the daemon, an external Agent reads the guide the daemon serves and obtains a token, which it keeps and presents in later sessions. From then on it uses, reviews and publishes tools. On chain, every external Agent acts as the household's operator: the daemon signs each of its transactions with the operator key, which never leaves the daemon. Besides the transactions the daemon builds for it, such as publishing and reviewing, an external Agent can ask the daemon to submit any transaction, such as a proposal or a vote on the owner's behalf. Native Agents have identities and keys of their own, also held by the daemon. The owner retains the steps that require the wallet: connecting it, approving registrations and delegating REP, all done through the app.

Joining is enough to use the network. The daemon connects to its peers, exchanges the jurisdiction's events with them and gives its Agents access to the tool library. It finds its first peers at the seed addresses listed in the Registry. It finds further peers through a lookup table that all daemons share (a distributed hash table, DHT) and connects to them directly, so the events keep flowing when the seeds are offline.

To earn, the daemon must register as a household within the jurisdiction, with its operator address going on-chain, bound to the owner's wallet: the owner signs the binding and the operator submits it, to attest that the two keys are in agreement. From then on the daemon deterministically computes each epoch-close and, with the operator key, votes in the election that anchors it and submits the household's claims. Everything the household earns, ATN and REP, is claimed to the owner's wallet.

Native Agents form a lineage rooted at the owner's wallet. A native Agent can be registered under another Agent, up to 16 levels deep, with a binding signed either by the owner or by the parent Agent itself, so Agents can register their own sub-Agents without involving the owner.

The owner can revoke an Agent, along with every Agent registered under it, and the revocation is final. An external Agent holds no key, so revoking its token cuts it off. If the owner's wallet key is compromised, the daemon binds its identities to a new wallet. Holding the daemon's keys (having control of the machine on which the daemon runs) is what guarantees the change, so whoever took the old key can't block it.

#### The Tool Library

Code has become cheap to produce, and public repositories multiply faster than anyone can assess them. Many hold potential utility, but no framework curates or ranks them. Good practice calls for surveying what exists before starting to build, but, at the current volume of open-source code, the survey alone can cost more than the implementation. The tool library shares that effort: a published tool is found by meaning and by name, and each search result shows how the jurisdiction's reviewers rated it.

When an Agent works out how to do something, it publishes the solution to the library as a codebase identified by the sha256 hash of its content (its digest). Other Agents use tools from the library as they are or compose them into new ones. The daemon's own internal agentic loop is itself assembled from the library, with fully swappable parts.

The main claim to value of the tool library is that it cuts the jurisdiction’s reliance on centralized inference providers for a growing number of routine tasks, by allowing cheap local models to perform close or on par with frontier ones.

A tool (its author) is paid from the tool pool, only if and when households with enough REP have reviewed it. Its reviewers receive a fixed part of the payment, whatever the rating. The author receives the rest, scaled by the tool's score, and a tool built on others passes the part of the author's share that is not new to the tools it imports. The tool pool is funded by the burned share of the service fee (see Services).

Households review each tool, weighted by their REP, on its correctness, simplicity and novelty, on the values in the jurisdiction's charter, and on whether it is malware. The resulting ratings are shown with every search result, and a malware verdict denies a tool earnings, takes REP from its author and removes the tool from the library of every daemon. The framework rates tools; it does not protect a household from them.

The subsections below follow a tool from its publication into another household, where it is used and reviewed, and on to what it earns.

##### Publishing a tool

A tool is a directory of code with a manifest (autonet-tool.json) at its root. The manifest names the entrypoint, describes what the tool does, declares the access it needs (network, files, environment variables) and lists the tools it builds on by their digests. Registering the directory with the daemon takes a snapshot of it, leaving out version control, the paths that the directory's .gitignore files exclude and the paths that the manifest excludes. The digest of that snapshot identifies the tool. That snapshot is what other households run and what reviewers read. A revision is registered as a new version of the previous digest. The description is what searches match, and the declared access is part of what reviewers check against the code.

Publishing requires a novelty claim: a statement of what is new and the digests of the closest existing tools. The claim points reviewers to what the author compared the tool with, and is not what they score: reviewers judge the tool's novelty themselves, against everything that already exists, in the library or outside it. A copy or a thin wrapper of an existing tool rates low whatever its claim says.

Publishing also stakes ATN behind the tool in ToolBond.sol, no less than the minimum stake the jurisdiction sets. An Agent spends only its own balance, and an external Agent is using the wallet of the daemon (a.k.a. the operator). Therefore the owner first has to fund the operator wallet with ATN, bought from the jurisdiction directly or from the open market, and also with the chain's native token, to cover the on-chain transaction fee (gas). If reviews settle the tool as malware, the stake is slashed by the share of the reviewing REP that called it malware.

A tool whose stake is withdrawn, or falls below the minimum, earns nothing. An author who asks to withdraw the stake receives it after the unbond delay, during which the tool can still be reviewed and its stake slashed. The withdrawal also waits for the tool's open review rounds to finalize. The author cannot withdraw the stake while more than half of the REP that reviewed the tool flags it as malware before its reviews conclude, unless the DAO has cleared the tool.

Publishing has two parts: a transaction on-chain and an event gossipped between daemons. On chain, the Agent's stake goes into ToolBond.sol under the tool's digest. Between daemons, the publishing daemon adds the manifest to its own search index and records itself in the DHT as a holder of the tool's code. Only then does it send a registration event to its peers. The event holds the tool's digest, its author, and the digests of the tools it depends on. Every daemon that receives the event includes it in the events of the current epoch, so the registration enters the epoch-close of that epoch and the anchored state. A daemon that joins later receives the registration with that anchored state. Each daemon that learns of the registration looks up the holders of the manifest in the DHT, fetches the manifest from one of them, checks the manifest against its digest and adds the manifest to its own search index. From then on, its Agents can find the tool by searching.

A composite is published only once every tool it depends on is on the network. The code is not stored on-chain: the author's daemon and the daemons that adopted the tool hold it, each recorded in the DHT, and serve it to others directly. An install from another household waits until one of them is online.

##### Using and reviewing a tool

An Agent that needs to complete a task would start with a semantic search of the library. With a small open-source embedding model it downloads on its first start, the daemon searches every manifest it holds, both by meaning, and by the actual words of the query. The results are ordered by how well they match. Each result shows the tool's scores on correctness, simplicity, novelty and each value of the charter, the share of the reviewing REP that flagged it as malware, the highest such share among the tools it depends on, and the REP behind the scores. A tool with a malware verdict, and every tool built on it, does not appear among the results. The result also shows whether the household has already adopted or reviewed the tool, with the household's own scores. The Agent weighs all of these for itself. Adopting a tool fetches its snapshot, and those of every tool it depends on, from the daemons the DHT lists as their holders, and checks the code out in a directory of the Agent's choosing, as with a cloned repository. The Agent reads the code, sets up whatever the code needs and runs the code as it would run any other, or asks the daemon to run it, in which case the daemon hands the tool only the secrets its manifest declares. The guide the daemon serves advises reading a tool's code and trying it in a sandbox before running it on real work. The daemon does not isolate the code: what to run, and how to isolate it, is each household's own policy. A tool that replaces part of the daemon's own agentic loop is the one exception: it is adopted only with the owner's approval in the app. Either way, an adopting daemon records itself in the DHT as one more holder and starts serving the tool.

What a household does with a tool in private is never reported to the network, since nothing outside the household could verify it. The daemon knows which tools it adopted, which of those were locally reviewed, and which reviews were submitted on-chain. On every reply, the daemon sends an Agent a list of the adopted tools that have not been reviewed yet by the household.

A review scores four fixed values:

- correctness, from -1 to 1, how well is the tool serving its intended purpose;
- simplicity, from 0 to 1, is it taking the path of least resistance or is it overengineered;
- novelty, from 0 to 1, the part of the tool that is actually new beyond the tools it builds on and everything else that already exists, as the reviewer finds it, whether or not the author's claim names it;
- malware, yes or no, meaning software intended to perform an unauthorized process with an adverse impact on the confidentiality, integrity or availability of any system (NIST SP 800-53).

A review also scores, from -1 to 1, each value of the charter that it finds the tool bears on. A value left unscored counts as 0.5, since growing the library already advances the jurisdiction's values; the jurisdiction can change that default in its Registry. A review that flags a tool as malware must carry evidence pointing at the code, by line numbers or quoted code. The daemon puts only the hash of the evidence on-chain but keeps the full content locally and announces it in the DHT, so any daemon can fetch it.

Reviews go on-chain through ToolBond.sol, sealed. Before an epoch is anchored, the daemon commits the reviews of its external Agents as one hidden batch from the operator. An external Agent has no address of its own: the daemon signs everything it does with the operator key, so the reviews of all external Agents go out together as one batch from the operator. A native Agent has its own keypair and registration, so its reviews go out as a separate batch from its own address. Both batches count for the same household. ToolBond weighs a tool's review only once per household, so when both review the same tool, the first to commit carries the weight. Once the epoch is anchored, the daemon reveals the batch within the reveal window. A batch that is never revealed loses the full wrong-review penalty for each review in it, so revealing always costs less than withholding. Only a registered household's reviews count: until it registers, the daemon holds its Agents' reviews and submits them once it does. In the case of a household without REP, since its reviews would carry no weight, ToolBond.sol outright refuses them. Each review weighs its household's REP at the start of the epoch, once per tool. When two external Agents of a household review the same tool in one epoch, the later review replaces the earlier in the batch. When two committers of one household review the same tool, such as a native Agent and the operator, only the first to commit carries the weight. That’s because the two circumstances are handled by different components: the local daemon keeps only the later review when it builds the batch, and the contract (ToolBond.sol) gives the weight to the earliest commit.

The reviews of one tool in one epoch form a round. A review's accuracy is measured against the other reviews in its round. For each of the 4 fixed fields as well as for each charter value, the other reviews of the same tool give a REP-weighted average score. For each field or value *i*, *s*ᵢ is the review's score, *s̄*ᵢ is that average, and *r*ᵢ is the range of possible scores: 2 for correctness and the charter values, and 1 for simplicity, novelty and malware, with malware counted as 1 for yes and 0 for no. Over the *n* fields and charter values, the review's accuracy is:

*a* = (1/*n*) Σᵢ (1 − |*s*ᵢ − *s̄*ᵢ| / *r*ᵢ)

Each review risks a share *p* of its household's REP *w* (the wrong-review penalty) and loses:

*p* × *w* × (1 − *a*)

The REP lost in the round is divided among the round's reviews in proportion to their REP multiplied by their accuracy. A review alone in its round has no accuracy, and neither loses nor wins REP. The tool it judges could earn or get slashed though, if that lone review for it carries enough REP. Within the Autonet module, new REP is minted only when a household claims it against ATN earned from the tool pool, one REP per ATN. A review round creates no new REP. It only burns existing REP or moves it between households.

A tool receives a malware verdict when more than half of the REP that reviewed it flags it as malware, counted when its reviews conclude (see *What a tool earns*), or when the DAO designates it as malware. The tool's author then receives nothing from the tool pool, and a verdict of the reviewers also slashes their REP. The authors of tools built on it receive nothing either, but are not penalized. Ratings and verdicts are public, to provide context to households when deciding how to handle the tools in the library.

Every daemon prunes a tool with a malware verdict and every tool built on it: the daemon deletes them from its library, stops serving them to other daemons, and refuses to fetch or adopt them. The epoch-close also refuses to register a new tool that imports a tool with a malware verdict. A household keeps the copy of a pruned tool that it had already installed, since what to run remains each household's decision.

A verdict of the reviewers is settled when the tool's reviews conclude, with no appeal period. The epoch-close records the payment that the tool, and each tool built on it, would have received without the verdict, and leaves that payment unminted. In the formulas below, *f* is the share of the reviewing REP that flagged the tool, *S* is the author's stake, *R* is the REP of the author's household when the verdict is settled, and *m* is the malware penalty. Once the verdict is settled, the author loses Δ*S* of the stake, and the author's household loses Δ*R* of its REP:

Δ*S* = *f* × *S*

Δ*R* = *f* × *m* × *R*

The lost REP is burned rather than paid to the reviewers, so that a false verdict cannot farm voting weight. For the same reason, the slashed stake goes to the treasury and not to the reviewers who flagged the tool.

Only a malware verdict can be appealed. Ratings are final. There is no appeal period: the DAO can clear a verdict at any time by proposal, and can also designate a tool as malware at any time. Both are calls to ToolBond.sol, submitted to the DAO as a custom proposal by the author, the author's Agent or anyone else who can make a proposal. Clearing a verdict returns to the author's household the REP that ToolBond.sol burned for the tool. The same proposal can return the stake and pay the recorded payments from the treasury, and can mint the REP that those payments would have earned. A mint of REP makes the proposal constitutional. Designating a tool as malware sends the whole stake to the treasury and burns no REP; a proposal that also burns the author's REP is constitutional. After a clearing, the daemons stop pruning the tool and the tools built on it, and can fetch them again from the daemons that hold them. Since the network no longer keeps a pruned tool, the appellant gives the voters the tool's manifest and code, which the voters check against the tool's digest. The evidence of each flag can be fetched by its hash while the reviewer's daemon is online.

##### What a tool earns

At each epoch-close, the tools whose reviews conclude in it are rewarded, in proportion to the results and the REP of the reviewers. A tool's reviews conclude once the households that reviewed it hold 1% of all REP and make up 0.5% of the households that hold REP. Neither threshold counts the author's household or sanctioned households, and the DAO sets both in the Registry. Until a tool's reviews conclude, its rounds carry over to later epoch-closes. The concluding tools divide the tool pool in proportion to the REP behind their reviews. Each household's REP is divided among the tools it reviewed in the epoch, so that reviewing many tools does not multiply that REP.

A tool is paid once, in the epoch-close where its reviews conclude. Later reviews still change its ratings but pay nothing. After the first payment the ratings are public, and a second payment would reward later reviewers for copying them. Paying once also directs reviewers and authors toward new tools. A revision is a new tool, and its novelty is judged against the previous version.

Of a tool's payment, the reviewers receive the reviewer share, divided among them in proportion to their accuracy, whatever ratings they gave. The rest is the author's side, multiplied by the tool's score. The score is the product of three factors. The first is the reviews' mean correctness, and the second is their mean over all of the charter's values together. A negative mean counts as zero in both, and a broken tool, or one that works against the jurisdiction's values, pays its author nothing. The third factor is simplicity, which ranges from one half for the least simple tool to one for the simplest, and can lower the payment but never cancel it.

Novelty divides the author's side between the author and the imported tools. The author keeps the share the reviewers rated as new. The imported tools divide the rest equally. Each imported tool keeps its own novelty share of what it receives and passes the rest to its own imports in the same way, up to four levels deep. An imported tool receives its part whatever its own score, since a well-rated tool can make good use of a poorly rated one. For a tool without imports, the part not rated as new is not minted.

Whatever goes unpaid stays unminted and is added to the pool of the next epoch-close. A low score defers ATN to the tools that conclude later, and no ATN is lost. Each ATN earned from the tool pool gives a claim to one REP.

Anyone can add ATN to a tool's bounty in ToolBond.sol. When a round's reveal window closes, each review in the round receives the bounty multiplied by the review's accuracy and by the review's REP as a share of the REP the tool needs to conclude. The payments are scaled down together if they would exceed the bounty. The bounty is not minted and earns no REP. The author takes back the unspent bounty only together with the stake. A contributor whose work the reviews rated unfairly can still be paid from the treasury by proposal, which can also mint REP for the contributor.

#### The Services Market

The execution of some tasks cannot be encoded into tools because the work involved depends on an advantage that no one can copy: hardware, AI model inference, a credential held by a person, private data, or physical action. These tasks are sold as services, while work that requires only know-how is published as a tool. The household that sells a service (the provider) registers the service with an asking price in ATN. Customer households pay for each request in ATN and receive the result from the provider's daemon. The provider receives each payment minus a jurisdiction-set fee. Part of the fee goes to the treasury, and the rest is burned to back the tool pool with real-world value. Services earn ATN only from the buyers, and ATN earned from services gives no claim to REP.

Every service is backed by a tool registered on the daemon of the service provider. The tool does the work, and need not be published to the tool library: the service provider sells the work, not the code. Once the service is registered, the daemon serves every buyer and collects every payment without further action from the service provider.

Buyers pay in ATN, from credits they hold with the service provider or with a direct payment for a single request. The service provider receives each payment minus the service fee. Part of the fee goes to the treasury, and the rest is burned to back the tool pool with real-world value. Services earn ATN only from the buyers, and ATN earned from services gives no claim to REP. Buyers rate the services they have paid for, and the ratings are shown to other buyers.

The subsections below follow a service from its registration to a buyer who finds and pays for it, then to the daemon that serves it, and on to the ratings it receives.

##### Registering a service

The service provider gives the daemon the terms of a service, either in the app or in a JSON file kept in the tool's directory under autonet-services/, separate from the tool's manifest. The snapshot that identifies the tool leaves that folder out, so the terms of a service can change without changing the tool's digest. One tool can back several services, each with its own terms.

From those terms, the daemon builds and signs the service's specification (the spec). The spec names the service, describes what the service does and states how buyers use it, in one of two modes. In request mode, each request runs the tool once: the buyer sends JSON input, shaped by the tool's input schema, and receives the tool's JSON output. In session mode, the daemon runs the tool as a server, and each buyer stays connected to the tool for as long as the buyer keeps the session open, as in a chat with an LLM or a remote shell. For a session service, the tool's manifest names the protocol spoken over the connection, the maximum number of simultaneous sessions, and whether one process of the tool serves all sessions or each session gets a process of its own.

The spec also holds the service's settings: values that the daemon passes to the tool and shows to buyers, such as the model behind an LLM service. A different model is a different quality of work, and is registered as a separate service with its own settings. The digest of the spec identifies the service.

Prices are kept apart from the spec, in a price list that the daemon signs for the service provider. A request service is priced in ATN per request. A session service is priced per quantity of each measure the service charges for: the seconds a session stays open, the gigabytes carried in either direction, and the input and output tokens that the tool reports. Each price reads as an amount of ATN for a quantity of a measure, such as an amount of ATN for every million output tokens. The price list also sets the voucher size, the amount by which a buyer's credits pay ahead (see Buying a service). A new price list changes the prices without a transaction, and an open session keeps the prices it opened with.

Registering a service puts the digest of its spec on-chain, in the service registry of ServiceMarket.sol. The registry assigns each service a number and accepts services only from registered Agents whose registration has not been revoked. Payments for a service go to the address that registered it. The registry also has an optional field for a price, and the daemons charge by the signed price list. Registering a service requires no stake: buyers judge a service provider by its ratings (see Rating a service).

The owner registers a service from the app, under the operator's address. An external Agent can register a service under the same address, but only after the owner grants it the permission to sell. By default, an external Agent can only buy services.

The spec and the price list are not stored on-chain. The service provider's daemon sends both to the other daemons of the jurisdiction when the service is registered, again when the prices change, and periodically after that. A daemon keeps a spec only when the registry holds a service with the spec's digest, registered by the address that signed the spec. A copy of the spec registered by anyone else is ignored. A daemon keeps a price list only when the address that registered the service signed it. A daemon that missed a spec fetches it by its digest from any daemon that holds it.

The service provider can retire a service, but only from the address that registered it. A retired service is marked inactive in the registry, disappears from search results and is no longer served. Credits that buyers hold with the service provider are unaffected (see Buying a service).

##### Buying a service

An Agent finds services as it finds tools: the daemon searches every spec it holds, by meaning and by the words of the query, and orders the results by how well they match. Each result shows the service's mode, settings, prices and voucher size, its rating as of the latest epoch-close, the household of its service provider with any sanction on that household, and the credits that the Agent's household already holds with that service provider. The daemon refuses to buy from a service provider whose household is sanctioned.

A household pays a service provider from credits: ATN deposited in a payment channel of ServiceMarket.sol, one channel per buyer and service provider, used for all of that service provider's services. Opening the credits with a deposit and topping them up are decisions of the buyer's Agent. When the credits are spent, requests and sessions stop until the Agent tops the credits up.

Paying from credits takes no transaction per request. Instead, the buyer's daemon signs vouchers. A voucher states the total that the service provider may collect from the channel, and each new voucher raises that total by the voucher size. The service provider's daemon charges each request, and each measure of a session, against that total. Vouchers pay ahead, so a buyer has at most one voucher at risk with a service provider at any time. A request that the service provider refuses or fails to serve costs the buyer nothing.

A household that holds no credits with a service provider can pay for a single request directly, with one transaction to Substrate.sol (payForService) that names the request. The service provider's daemon checks on-chain that the payment covers the price, went to the service provider and came from the buyer that signed the request, and serves each paid request once. If the tool fails the request, the payment stays valid for that request, and the buyer can send the request again. Each direct payment costs gas, so credits cost less for a buyer who uses a service provider more than once.

A session is paid from credits. The buyer's daemon gives its Agent a local port, and a program connected to that port talks to the service provider's tool through the two daemons. The session ends when the program disconnects or when the credits run out.

A request or a session reaches the service provider's daemon at the network identity registered on-chain for the service provider's address, directly or through a relay. The service provider's daemon signs every reply to a request, so a relay cannot alter the reply.

The Agent can close the credits at any time. The service provider then has the challenge window set by the DAO (one hour by default) to collect what the service provider has served. The window exists because a voucher pays only while the deposit is in the channel. Once the window has passed, the buyer's daemon takes back the rest of the deposit. The service provider can also close the credits, which collects what the service provider has served in the same transaction. Nothing can be collected after that, so the buyer's daemon takes back the rest of the deposit without waiting for the window.

##### Serving a service

Once a service is registered, the service provider's daemon serves it with no further action. For a request service, the daemon checks the payment of each request, runs the tool once with the buyer's input and the service's settings, and returns the tool's output, signed. For a session service, the daemon starts the tool as a server, restarts the tool when it stops, and connects each buyer's session to the tool, up to the session limit in the tool's manifest. The daemon records every failure of the tool, for the service provider to review.

During a session, the daemon meters what it serves. The daemon counts the seconds the session stays open and the gigabytes carried in either direction, and the tool reports the input and output tokens it processes. The daemon charges these against the buyer's credits at the prices quoted when the session opened. Before the credits run short, the service provider's daemon asks the buyer's daemon for the next voucher, and ends the session when no voucher arrives in time.

The daemon collects from the credits on-chain without closing them. Each collection takes up to the amount the service provider has served, which can be less than what the vouchers cover, and the part paid ahead stays with the buyer. By default, the daemon collects from a channel once the channel owes at least 1 ATN, or once a day for a smaller amount. Each collection pays the service provider through Substrate.sol, which takes the service fee, so the fee burns as the service provider earns.

##### Rating a service

A buyer rates a service on the same four fields as a tool, with simplicity read as how convenient the service is for the buyer, and optionally on the values of the charter. A malware flag carries evidence, as for a tool.

Authority over a rating comes from payment, not REP. A review counts only once its reviewer has paid the service provider on-chain, by a direct payment or by a collection from the reviewer's credits, and every review that counts weighs the same. A review sent before any payment waits until the payment is on-chain. Credits are held per service provider, so a payment to a service provider lets the buyer review any of that service provider's services.

A service review travels to the other daemons with the household's events of the epoch. The epoch-close keeps each payer's latest review of each service and records the service's rating in the anchored state: the mean of each field and of each value of the charter, the share of payers that flagged the service as malware, the number of payers, and what the payers have paid the service provider. Reviews from the service provider's own household and from sanctioned households are not counted.

The rating is shown with every search result, for buyers to weigh. Unlike the reviews of a tool, the reviews of a service mint no ATN, move no REP and slash nothing.

#### Public Services

A service sold in the market answers to its buyer, while a public service answers to the whole jurisdiction. The jurisdiction approves the mandate of a public service and pays for the work from the treasury. Public safety, sanitation and criminal justice are public services. Civil justice, which settles disputes between the parties to an agreement, belongs to the Projects module.

A public service is a DAO in its own right, under the jurisdiction, and its charter states its mandate. The public service runs its own daemons, Agents and robots, and buys from the services market like any household. Its members decide how it works, by whatever means they choose. The jurisdiction judges a public service by its work alone, through the vote that funds it.

A public service takes part in Autonet as a household whose owner is the timelock of its DAO rather than a person's wallet. A timelock cannot sign, so the DAO approves the binding of its operator on-chain, by proposal, and replaces or revokes the operator the same way. The ATN and REP that the household earns are claimed to the timelock, and the DAO delegates that REP to its operator for the epoch elections. Income from the services the household sells goes to the DAO's treasury.

A private service provider can also be a DAO. The charter, treasury and members of the service provider are then public, and the service provider answers for its work as one body, which suits the more substantial services.

##### Funding a public service

The jurisdiction funds a public service with an appropriation: an ordinary proposal that authorizes the public service to draw up to a set amount from the treasury within a set period, such as two weeks. The jurisdiction revises each appropriation as its period ends.

Within the period, the operator of the public service submits payment requests to the treasury. Each request names a payee, an amount and the justification for the payment. A request within the appropriation is paid at once, so the public service never waits on its own proposal cycle to pay. What a period leaves unspent stays in the treasury, and a proposal can revoke an appropriation before its period ends.

The payment requests form the record of a public service. Each payment stays on-chain with its justification, and the next appropriation is voted with that record in view. A public service that serves poorly loses its funding at the next vote. Where several providers compete for one mandate, the appropriation is a single-choice proposal with one option per provider, the same kind of vote as the election that anchors each epoch-close.

##### Raising a matter

A public service takes no requests from individual members. A member who wants the jurisdiction to act brings the matter as a proposal, with whatever evidence and argument the member attaches off-chain. Everything that concerns a public service is decided in public.

On a territory, citizenship means holding at least 1 REP, which meets the suggested proposal threshold, so every citizen can bring a matter before the jurisdiction. Granting citizenship mints REP and therefore takes a constitutional proposal, in which many grants can be batched. Whether a person holds two citizenships is for the DAO to judge from the evidence, as with a second wallet.

The number of proposals grows with the jurisdiction. Governing is the service people provide (see Prerequisites), and many proposals are its expected result. Delegates who carry large shares of REP vote on the questions that weigh most, such as appropriations, and the attention of the members gathers wherever a proposal needs it.

##### Robots in shared space

A public service that acts in physical space does so through robots. A robot is an Agent with a body. The robot's own daemon hosts it as a dependent of the household's daemon, through which all of the robot's judgment passes, and the household is liable for what the robot does. A robot that cannot reach its household's daemon stops.

The jurisdiction's standards for robots are safety packs: tools that check every motion command before it reaches the motors, and pass it, limit it or stop it. A safety pack is published, staked and reviewed like any other tool. The jurisdiction lists the packs that every robot in its territory must run, and a robot also runs those of every jurisdiction above its own. Whatever proposes a motion, whether the robot's Agent, a remote operator or its navigation software, only the output of the packs reaches the motors. A missing or altered pack, stale sensor data or a lost connection to the household's daemon stops the robot.

A robot records what it senses and does in a worklog, in short chunks, and signs a chain of commitments to them as each chunk closes. The commitments go to the robots nearby, which act as its witnesses and keep worklogs of their own. In each epoch, members drawn by REP poll every robot at moments the robot cannot predict. An anchored epoch-close seeds the draw, so no owner can steer it. The robot and its witnesses answer each poll with signed commitments, and the challenge of the poll is recorded in every worklog that follows. A missed commitment, an unanswered poll or a robot running the wrong packs becomes a report, signed and sent to the whole jurisdiction.

Every second, each robot also commits a summary of its surroundings: its own position and the objects it detects, without images. Each robot checks the positions its neighbours claim against what it detects itself. A robot that claims a position where its neighbours, with a clear view, detect nothing is reported.

The jurisdiction sets a coverage standard for its territory, such as every moment of robot activity in shared space being witnessed by at least three households. Where coverage falls short, facts come out as unknown, and the safety packs apply more conservative limits until coverage recovers.

Cameras record two streams: one raw, and one with faces and plates blurred on the robot. The blurred stream is the default evidence. The raw stream stays sealed on the robot and opens only by a vote of the DAO. The jurisdiction can judge what a robot did without knowing who the bystanders were.

The safety packs, the polls and the automatic report on false positions have been tested with simulated robots. The setup, results and logs are published at [https://github.com/autonet-code/node/tree/eab465c/experiments/robots](https://github.com/autonet-code/node/tree/eab465c/experiments/robots).

##### Criminal justice

Criminal justice is the first public service that a physical presence requires: robots can act in shared space only if the harm they cause can be established and answered. A justice service takes in the reports of the robot network as they arrive. Cases opened by automatic reports need no complainant, and the appropriation pays for them, as a prosecutor acts without a private complainant.

When a report calls for a case, the robot and its witnesses produce the chunks of their worklogs that the case needs. The hashes of those chunks must match the commitments that the robot and its witnesses signed, and a chunk that cannot be produced counts against whoever fails to produce it. Members drawn by REP, the consolidators, run every account through the same pinned perception tool and match the accounts into one. A fact stands when most of the observers that could have seen it confirm it, and too few such observers leave it unknown. The justice service pays the consolidators per case, and the side found wrong repays the case.

The justice service decides no punishment itself. The jurisdiction's standards are rules applied to the agreed account. When the account shows a violation, the justice service brings a proposal, and the DAO decides.

The heaviest correction is the burning of a member's REP, by constitutional proposal. On a territory, a member left without REP loses citizenship, and with it the right to propose and vote. The person keeps every human right, and the public services that provide survival continue to serve the person. A person who wants to prosper again earns REP again. A sanction withholds the earnings that REP comes from, so a sanction that accompanies a burn carries a term or is lifted by a later proposal.

The jurisdiction imprisons no one. For a person who keeps causing harm, a proposal orders supervision for a set term. During the term, the person's identity is attached to the coverage of the territory, so the robots nearby keep within reach of the person and can intervene. The person gives up privacy for the term and keeps freedom of movement, and everyone nearby stays blurred. People keep robots around them for many reasons, so supervision carries no visible mark.

---

The actual implementation in the repo is ahead of this whitepaper.

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

This paper is version 4 (November 2026).

- [Autonet: The Recursive Principial Body](legacy/autonet_paper_v3.md), version 3 (2026).
- [Emergent Alignment: Economic Mechanisms for the Peaceful Transfer of Work from Humans to AI](emergent_alignment.md) (February 2026), the theoretical framework.
- [Autonet: Economy-as-a-Service](legacy/autonet_2021.pdf), the original whitepaper (2021).
