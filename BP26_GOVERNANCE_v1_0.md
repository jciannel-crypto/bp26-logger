BP26_GOVERNANCE_v1_0.md
Effective: 2026-03-27
Jason Ciannello (Architect) — Approved
Atlas (Systems Engineer) — Audited
Claude (Implementation Engineer) — Executes
Status: LOCKED — do not modify without Atlas review and Jason authorization

ROLE BOUNDARIES
Jason — Architect / Final Authority
Approves all protocol changes, schema changes, and phase transitions. No change is active without explicit Jason approval. Required phrase for implementation authorization: "Approved — proceed to implementation."
Atlas — Protocol / Schema Auditor
Designs system logic, reviews protocol rules, proposes governance structure. Flags drift. Does not implement. All schema and protocol changes require Atlas review before Jason approval.
Claude — Implementation Engineer
Executes against the current schema as defined in this document. Applies active protocol rules to new entries. Does not invent fields, does not modify schema without an approved spec, does not behave as if deferred items are already implemented. Flags friction but does not redesign.

SCHEMA BASELINE
Derived from live ledger audit — 110 entries — 2026-03-27
Core Fields (110/110 — always present)
betId, date, tipOffTime, matchup, awayTeam, homeTeam, decisionType, liveMoneyFlag, betType, selection, odds, stake, openSpreadTeam, openSpreadNum, currentSpreadTeam, currentSpreadNum, closingSpread, openTotalNum, currentTotalNum, moveType, moveSpeed, multiBook, lateMarketStatus, publicSide, publicSignalType, injuryClass, signalWhat, signalWhy, signalInvalidates, result, finalScore, netPnL, processTag, clvSpread, preGameNotes, postGameNotes, rubricConfidence, schemaVersion
Standard Fields (90–109/110 — near-universal)
closingTotal, clvTotal, createdAt, injuryPlayers, passReason, passOfNote, protocolPassRule, protocolPassWouldHaveBeen, decisionAt, sharpBook, entryType, depletionAsymmetry, signalOrigin, sharpConsensusLine, scoreOverrideActive, manualConfidence, scoreOverrideBug, openOdds, passMarketType, passCurrentOdds, currentOdds
Partial Fields (40–89/110 — inconsistently populated)
invalidationHappened, invalidationType, observedAfterMove, publicBetPct, publicMoneyPct, injuryPlayer (legacy singular), failureMode, learningNote, legacyConfidence, timingGate, moveDetectedAt
Sparse / Recent Fields (5–15/110 — added in recent sessions)
multiPlayerReturn, multiPlayerAbsence, opposingSwing, partialConfirmationType, expectedVsActualMove, spreadMove, signalClassificationTag, totalMove, statusT60, movePhase
Deprecated Fields — Frozen, Do Not Reuse
netPnl, signalThesis, mechanism, invalidationCondition, driftFlags, primaryPassReason, depletionCapacityGate, netPandL, signalClass, tipOff, decision, liveMoney, openSpreadLine, currentSpreadLine, openTotal, currentTotal, injuryClassification, confidenceScore, netPL, updatedAt
These exist in 1–2 entries as injection drift artifacts. Do not use in any new entry under any circumstances. Do not attempt retroactive cleanup without an approved migration spec.

ACTIVE PROTOCOL RULES
1. Historical Freeze
All entries before BP26-20260327-106 are locked under CVS. No retroactive edits, no backfill. Forward-only from entry 106.
2. Dataset Admission Filter
Three gates — any one qualifies an entry for logging:

Near-SIM rejection — signal present but gated or mechanism failed
Distinct market archetype — public-follow, baked-injury, balanced market, info-asymmetry, news-reprice
Structural learning case — lifecycle phase capture, CVS integrity event

If none of the three apply → do not log.
3. NEWS_REPRICE Hard Rule
Columns involved: openSpreadNum, currentSpreadNum, openTotalNum, currentTotalNum, publicSignalType, preGameNotes
If the market move from open to current was already completed before BP26 observed the game → decisionType = PASS, publicSignalType = NEWS_REPRICE. Cannot be classified as SIM regardless of confidence score or other signals. Only upgrades to SIM at T-60 if residual edge is confirmed via market stall or insufficient repricing after injury confirmation.
4. Selection Field Rule
The selection field must reflect the actual directional lean of the signal — the side BP26 would have acted on if the entry qualified. If no directional lean exists in the market data, document that in preGameNotes and use the side most consistent with the game's market structure. No new field states are introduced. No mechanical default to the underdog. The selection field must always be a valid bet expression using existing field format (e.g., "ATL +4.5").
5. Required Fields — SIM Entries
betId, date, tipOffTime, matchup, decisionType, selection, openSpreadNum, currentSpreadNum, spreadMove, openTotalNum, currentTotalNum, totalMove, moveType, lateMarketStatus, publicSide, publicSignalType, injuryPlayers, injuryClass, signalWhat, signalWhy, signalInvalidates, partialConfirmationType, expectedVsActualMove, multiPlayerReturn, multiPlayerAbsence, opposingSwing, signalClassificationTag, rubricConfidence, preGameNotes
Post-game (required after resolution): result, finalScore, closingSpread, closingTotal, clvSpread, clvTotal, processTag, invalidationHappened, postGameNotes
6. Required Fields — PASS Entries (simplified)
Required at logging time:
betId, date, tipOffTime, matchup, decisionType, selection, passReason, protocolPassRule, protocolPassWouldHaveBeen, passOfNote, signalClassificationTag, preGameNotes
Required post-game:
result (= "N/A (PASS)"), netPnL (= 0), processTag (= "CORRECT PASS"), postGameNotes (one sentence — what happened)
Not required on PASS entries:
signalWhat, signalWhy, signalInvalidates, partialConfirmationType, expectedVsActualMove, multiPlayerReturn, multiPlayerAbsence, opposingSwing, rubricConfidence, injuryPlayers — these are SIM-level forensic fields. If relevant context exists, put it in preGameNotes.
7. passOfNote Rule

YES — near-SIM rejections only, or entries where a real edge consideration informed a protocol decision
NO — control samples, balanced markets, baked-injury cases, info-asymmetry captures

8. No Field Improvisation
If a field does not exist in the schema, data goes in preGameNotes or postGameNotes. Do not invent field names. Do not reuse deprecated fields.
9. Entry Weight Acknowledgment
Not all entries are equal. Control samples, false-positive traps, and near-SIM rejections carry different analytical weight. Entry tiering will be introduced in a future spec. No schema change yet.
10. Deprecated Field Rule
Do not use any field listed in the "Deprecated Fields" section above under any circumstances. If an entry already contains a deprecated field, leave it as-is (historical freeze applies). Do not copy deprecated field patterns into new entries.

GOVERNANCE TABLE
Rule / ChangeExisting column(s) usedSchema change required?StatusHistorical freeze (pre-106)N/A — operationalNACTIVEForward-only fixesN/A — operationalNACTIVEDataset admission filterN/A — operationalNACTIVENEWS_REPRICE cannot be SIM if move already consumedopenSpreadNum, currentSpreadNum, openTotalNum, currentTotalNum, publicSignalType, preGameNotesNACTIVESelection = directional lean (no mechanical default)selectionNACTIVEpassOfNote = YES only for near-SIM / meaningful edgepassOfNoteNACTIVEPASS required fields (simplified)passReason, protocolPassRule, protocolPassWouldHaveBeen, passOfNote, signalClassificationTagNACTIVESIM required fields (full forensic set)signalWhat, signalWhy, signalInvalidates, partialConfirmationType, expectedVsActualMove, multiPlayerReturn/Absence/opposingSwingN — fields existACTIVENo field improvisationN/A — operationalNACTIVEsignalClassificationTag — archetype taggingsignalClassificationTagN — field existsACTIVEDeprecated field freeze — do not reuseN/A — operationalNACTIVEEntry tiering systemNo field yetY — future specDEFERREDmovePhase formalizationmovePhase exists (5/110)N — enforcement deferredDEFERREDMove Completion %No field existsY — future specDEFERREDResidual Edge hypothesis fieldNo field existsY — future specDEFERREDLogger UI field validation / enforcementN/A — UI changeY — logger code changeDEFERREDDropdown enforcement on key fieldsN/A — UI changeY — logger code changeDEFERREDDeprecated field cleanup (retroactive)MultipleY — data migrationNOT APPROVED

DEFERRED — NOT YET ACTIVE
The following items are acknowledged but not part of the active system. They require future schema specs and Jason + Atlas authorization before implementation:

Move Phase formalization — field exists with 5 entries; enforcement rules not yet active
Move Completion % — field does not exist; future schema spec required
Residual Edge hypothesis field — field does not exist; future schema spec required
Entry tiering system — field does not exist; future schema spec required
Logger UI validation / enforcement — requires logger code change
Dropdown enforcement — requires logger code change
Retroactive deprecated field cleanup — not approved; historical freeze applies


HOW THIS DOCUMENT PERSISTS
This document must exist in three places to survive session boundaries:

GitHub repo — committed alongside BP26_SESSION_INIT_v3_3.md
Claude Project Instructions — uploaded so it loads into every new session automatically
Session Init reference — BP26_SESSION_INIT_v3_3.md should reference this document under Governing Standards


BP26 GOVERNANCE v1.0 | Locked 2026-03-27 | Owner: Jason Ciannello | Do not modify without Atlas review and Jason authorization
