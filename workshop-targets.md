# Unified Error Codes — Workshop Target Analysis

## Current State Summary

- **Milestone 1** ("Pilot Preparation: 3 Hardware Error Codes & Communication Schema") is due **April 17, 2026** — at **0% complete** with 4 open issues: PowerLoss (#2, in review), ConnectorLockFailure (#3), Isolation Diagnostic (#8), and Schema Format (#35, not started)
- **Kanban board**: 17 backlog, 5 under discussion, 9 ready, 1 in review, 1 done — totaling 32 open issues
- **Only 2 active contributors** (plaskows83, AnaisBonnard), plus knowack1 and a few commenters
- The spec is still at skeleton stage — no error code definitions have been merged yet
- The workshop is planned for **June 2026**, so this summary reflects the project status **as of April 2026**
- The working assumption should be that **Milestone 1 is accomplished before the workshop**, so the June session can focus on validation, implementation direction, and partner commitment rather than only reviewing unfinished draft work

---

## Stated Workshop Goals

1. **Awareness** of the UEC project direction
2. **Present Milestone 1 as completed baseline work** and align on what comes next
3. **Collect CPO feedback** on error code definitions from their operational perspective
4. **Address manufacturer resistance** — they see diagnostics as proprietary competitive ground
5. **Select the right implementation strategy after Milestone 1**

---

## Strategic Decision Target for the Workshop

One of the main outputs of the workshop should be a clear decision on the execution model for the next phase of the initiative.

### Option 1. Complete the full specification first, then start implementation with EVSE manufacturers

This approach means defining the broader UEC specification first, covering the full error-code space before moving into implementation work with manufacturers.

Potential advantages:

- Creates a more complete and internally consistent specification before pilot integration begins
- Avoids rework caused by piloting too early on a narrow subset
- Gives manufacturers a clearer long-term target architecture

Potential risks:

- Delays real-world validation
- Increases the chance of designing parts of the specification that are difficult to implement in actual products
- Makes it harder to build momentum and secure concrete manufacturer commitment early

### Option 2. Early validation and adaptation through a pilot

This approach means using the 3 Milestone 1 error codes and related telemetry as a pilot, then finding EVSE manufacturers willing to implement them early in order to collect feedback and validate the direction.

Potential advantages:

- Provides early implementation feedback from real products and engineering teams
- Confirms whether the telemetry model and communication approach are practical
- Helps adapt the specification before scaling to the full error-code set
- Builds credibility and momentum through concrete pilot results

Potential risks:

- The initial pilot scope may be too narrow to expose all design gaps
- Pilot-specific decisions could bias the later full specification if not managed carefully
- Requires willing manufacturers to engage before the full spec is stabilized

### Recommended workshop outcome

The workshop should not only discuss these two options at a high level, but should aim to leave with:

- A decision on whether the initiative is primarily **specification-first** or **pilot-first** after Milestone 1
- Agreement on the criteria for success of the chosen path
- Identification of EVSE manufacturers and CPOs willing to participate in the next step

---

## Additional Recommended Workshop Targets

### 5. Break the "proprietary diagnostics" framing — reframe around the shared interface layer

The manufacturers' resistance is rational: they've invested in diagnostics IP and fear commoditization. The workshop should explicitly distinguish between:

- **Internal diagnostics** (remains proprietary — root-cause algorithms, predictive maintenance models, firmware-level fault trees) — UEC does NOT touch this
- **The reporting interface** (what gets communicated to the CPO/CSMS/EV) — this is what UEC standardizes

The analogy: OBD-II didn't eliminate automotive OEM diagnostic IP — it standardized the *communication layer* while each OEM kept its proprietary diagnostic depth. Manufacturers who adopted OBD-II early didn't lose competitive advantage; they gained market access. The workshop should make this boundary crystal clear.

### 6. Live demonstration of the cost of fragmentation — using CPO data

Invite 2–3 CPOs to present anonymized data showing:

- How many vendor-specific error code mappings they currently maintain
- The operational cost (time, money, missed SLAs) of translating between proprietary error sets
- Cases where ambiguous/missing error information led to delayed repairs or unnecessary truck rolls

This creates social proof and gives manufacturers a direct view of their customers' pain. It's harder to dismiss when your CPO customer is presenting the problem to your face.

### 7. Schema Format decision workshop session (Issue #35)

This is the most critical open technical question and it's blocking Milestone 1. The workshop should include a focused session where participants evaluate:

- JSON Schema (OCPP-aligned)
- ASN.1 with JER/COER (ISO 15118-202-aligned — one schema could serve both EV-EVSE and EVSE-CSMS paths)
- A concrete side-by-side comparison using the PowerLoss error code as the example payload

Getting manufacturer and CPO input on schema format early prevents rework later.

### 8. Joint definition walkthrough — live collaborative review of the 3 pilot error codes

Use the PowerLoss, ConnectorLockFailure, and Isolation definitions as live workshop exercises. Have mixed groups (manufacturer + CPO at each table) review the definitions together:

- Are the telemetry parameters sufficient for root-cause analysis?
- Are the trigger conditions unambiguous?
- How does each manufacturer currently report this fault today?

This accomplishes two things: it accelerates Milestone 1 work, and it builds shared ownership of the definitions.

### 9. Address the elephant: "What's in it for the manufacturer?"

Dedicate a session to the manufacturer value proposition:

- **Reduced integration cost**: Every new CPO relationship currently requires custom error code documentation and mapping. UEC eliminates this.
- **Market access**: CPOs will increasingly require standardized diagnostics in RFPs (especially as fleet sizes grow and multi-vendor becomes the norm)
- **Quality signal**: Manufacturers who adopt UEC signal product maturity — like ISO 9001 certification, it becomes a market expectation
- **Controlled telemetry sharing through authorization**: UEC could define an authorization mechanism for telemetry access, allowing the manufacturer to explicitly grant access to specific telemetry datasets to a specific operator, service partner, or support organization. This helps separate the question of "standardized format" from the question of "who is allowed to see what".
- **Open-source platform vision** (Issue #37): Tease the upcoming vision for an open-source validation/consumption platform that lowers adoption cost for manufacturers

This is an important workshop topic because it directly addresses one of the main manufacturer concerns: they may be willing to expose standardized diagnostics if they retain control over access rights and visibility levels.

Possible discussion points:

- Should telemetry access be granted by role, by partner, or by use case?
- Which telemetry should always be shared as part of baseline interoperability, and which telemetry should remain access-controlled?
- Can the model support different visibility levels for CPOs, field service providers, and manufacturer support teams?
- How should consent, authorization, and auditability be handled in practice?

### 10. Establish a "Minimum Viable Adoption" path

Manufacturers won't commit to full UEC overnight. Define a concrete, low-barrier first step:

- Implement the 3 Milestone 1 error codes
- Report via existing OCPP vendor extension mechanism (as shown in the DIN DKE SPEC 99003 examples)
- No firmware rewrite required — this is an overlay, not a replacement

This gives manufacturers a safe way to participate in the pilot without disrupting existing products.

### 11. Recruit contributors and pilot partners

Currently only 2 active contributors is a risk. The workshop should aim to:

- Recruit at least 2–3 manufacturers to commit to the pilot (implementing the 3 error codes)
- Recruit at least 1–2 CPOs willing to consume and validate the pilot data
- Identify new GitHub contributors who will participate in definition reviews
- Set a realistic revised timeline for Milestone 1 (the April 17 date appears infeasible at 0% completion)

---

## OCPP 2.x Observability: Components & Variables vs. GetDiagnostics

### The OCPP 2.x Observability Landscape

OCPP 2.x introduced a rich observability model based on **Components and Variables** with monitoring capabilities. While powerful in theory, this approach has practical adoption challenges that are worth discussing openly with manufacturers and CPOs.

### GetDiagnostics as a Pragmatic Alternative

We propose exploring **GetDiagnostics** as a complementary (and potentially primary) channel for delivering unified error code telemetry. The key advantages:

- **Easy to implement**: Most charging station GetDiagnostics implementations are script-based on the target device. Extending the diagnostic script to include an additional file with structured UEC telemetry data is a minimal development effort — no deep firmware changes required.

- **Post-mortem by nature**: Unlike OCPP 2.x variable monitoring, GetDiagnostics does not require pre-configuring monitors or setting up event triggers in advance. The data can be fetched **after an incident occurs**, which matches the real-world workflow of field support teams investigating failures.

- **Reuses the existing OCPP connection**: GetDiagnostics is available in both **OCPP 1.6** and **OCPP 2.1**, making it a protocol-version-agnostic transport. This means manufacturers don't need to choose between protocol versions — the same diagnostic payload approach works across their installed base.

- **Supports advanced trace data**: GetDiagnostics can carry rich payloads including:
  - **V2G communication traces** (full message exchange sequences)
  - **TLS handshake traces** (certificate chains, cipher negotiation, failure points)
  - Any other diagnostic artifacts that are too large or complex for real-time event reporting

### Workshop Discussion Points

This session should explore with participants:

1. **Current state**: How do manufacturers deliver diagnostic data today? What format? What triggers the collection?
2. **CPO perspective**: What diagnostic data do CPOs actually need after an incident? How quickly? In what format?
3. **GetDiagnostics adoption**: What barriers exist to extending GetDiagnostics scripts with UEC-structured telemetry?
4. **Relationship to Components & Variables**: Should GetDiagnostics be a fallback, a complement, or the primary channel? When does real-time monitoring (Components & Variables) add value over post-mortem collection?
5. **Payload format**: How should the UEC telemetry file within GetDiagnostics be structured? (Ties back to the Schema Format decision in Issue #35)

---

## Workshop Anti-Patterns to Avoid

- **Don't present UEC as a regulatory mandate** — the open/voluntary nature is a strength; making it feel coercive will trigger manufacturer resistance
- **Don't go too deep on taxonomy/spec details** — keep it outcome-focused for this audience (save deep spec work for the working group)
- **Don't ignore the ISO 15118-202 / EV-side story** — V2G bidirectional error exchange is a unique differentiator that neither OCPP nor proprietary solutions address
