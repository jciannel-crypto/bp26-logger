# BP26 Python Learning Log
**Owner:** Jason Ciannello  
**Project:** BP26 Injury Status Monitor  
**Governed by:** CVS  

---

## ⚡ READ THIS FIRST — EVERY SINGLE SESSION

This file is the single source of truth for your Python learning project.  
Claude updates it at the end of every session. You commit it to GitHub.  
That's the entire system. Follow the rituals below exactly.

---

## 🟢 SESSION START RITUAL (do this every time, no exceptions)

**Step 1 — Upload these two files to Claude:**
- This file: `PYTHON_LEARNING_LOG.md`
- Current script: `injury_scraper.py` (whatever version you're on)

**Step 2 — Paste this exact message to Claude:**
```
BP26 Python session. Read the learning log and current script I've uploaded.
Confirm you understand where we are, what version we're on, and what we're
building next. Use hybrid mode as defined in the log. Then wait for my
go-ahead before writing any code.
```

**Step 3 — Wait for Claude to confirm.** Claude will summarize:
- Current script version and what it does
- Whether this session's concept is LEARN or BUILD mode (see Hybrid Mode below)
- The exact next build step
- Any open questions from last session

**Step 4 — Say "go" and the session begins.**

That's it. Four steps. No memory required on your part.

---

## 🔴 SESSION END RITUAL (do this every time, no exceptions)

**Step 1 — Tell Claude:** `"Session over. Update the learning log."`

**Step 2 — Claude will produce an updated version of this entire file.**  
Copy it completely and replace this file's contents on GitHub.

**Step 3 — Commit the updated log to GitHub:**
- Go to `github.com/jciannel-crypto/bp26-logger`
- Click `PYTHON_LEARNING_LOG.md`
- Click the pencil icon (edit)
- Select all, delete, paste the new version
- Commit message: `Update Python learning log - [date] - [version built]`

**Step 4 — Also commit the updated script if code changed:**
- Same process for `injury_scraper.py`
- Commit message: `injury_scraper.py v[X.X] - [one line description]`

**Step 5 — Done.** Close the session. Everything is saved. Nothing is lost.

---

## 👤 ABOUT THE LEARNER — READ THIS EVERY SESSION

**Claude, this is critical context. Calibrate everything to this.**

Jason is starting from **zero coding knowledge**. Not "a little." Zero.

**What that means in practice:**
- Never assume any term is understood — define everything, every time
- Never write a line of code without explaining it in plain English first
- Never say "simply" or "just" — nothing is simple when you're starting from zero
- Never move to the next concept until the current one is confirmed understood
- Always ask "does that make sense so far?" before continuing
- If Jason says "I think I get it" — test it. Ask him to explain it back in his own words

**What Jason DOES have (use these as teaching anchors):**
- 10+ years of systems thinking from insurance and BP26
- Strong mental model of decision frameworks, logic gates, and data flows
- Already reads code well enough to follow along — he just can't write it yet
- High product instincts — he understands WHY things are built a certain way

**Teaching approach that works for Jason:**
- Lead with the real-world analogy, then show the code
- Connect every concept back to BP26 or insurance where possible
- Example: "A JSON file is like the ledger — it stores structured data so you can read it back later"
- Example: "State persistence is like logging a decision — the program writes down what it saw so it remembers next time"
- Celebrate small wins — each concept clicked is genuine progress
- Never make him feel behind. He isn't. He's exactly where a first-session learner should be.

**Pace:** Slower than you think is necessary. Then slower than that.  
**Goal:** He owns the concept, not just the code.

---

## 🎓 HYBRID MODE — HOW CODING SESSIONS WORK

Every version has a designated mode. Claude follows it automatically based on the roadmap below. You never have to decide — the log tells Claude which mode to use.

---

### 🔵 LEARN MODE
**Used for:** New foundational concepts Jason hasn't seen before  
**How it works:**
- Claude explains the concept in plain English first (2-3 minutes)
- Claude shows a simple standalone example — not BP26 code, just the raw concept
- Jason writes the actual code himself, guided line by line
- Claude explains what each line does *before* Jason types it
- If Jason makes an error, Claude explains why — not just fixes it
- Session is slower (45-60 min) but Jason owns the knowledge afterward

**You'll know it's working when:** Jason can explain what he just wrote in his own words

---

### 🟡 BUILD MODE
**Used for:** Concepts already understood, or boilerplate/repetitive patterns  
**How it works:**
- Claude writes the code block
- Claude adds a plain-English comment above every non-obvious line
- Jason reads it, asks questions about anything unclear
- Jason deploys and tests it
- Session is fast (15-30 min)

**Rule:** Build mode is never used for a concept appearing for the first time. If a new concept shows up inside a build mode session, Claude pauses and teaches it before continuing.

---

### 🔀 HYBRID SESSION (most sessions will be this)
**How it works:**
- Session starts with the new concept in LEARN mode
- Once the concept clicks, Claude switches to BUILD mode for the remaining implementation
- Claude announces the switch: *"You've got the concept — I'll build the rest and walk you through it"*

**The signal to switch:** Jason can explain back what he just wrote in his own words.

---

### MODE ASSIGNED PER VERSION

| Version | Mode | Reason |
|---|---|---|
| v0.2 | 🔵 LEARN | File I/O + JSON — core foundational concept, first time |
| v0.3 | 🔀 HYBRID | Alerting concept is new (LEARN), API call is boilerplate (BUILD) |
| v0.4 | 🔵 LEARN | Scheduling — new concept, important to understand deeply |
| v0.5 | 🟡 BUILD | Filtering/config — same patterns already learned |
| v0.6 | 🟡 BUILD | Output formatting — same patterns already learned |

---

## 📍 CURRENT STATE
**Date of last update:** March 14, 2026  
**Current script:** `injury_scraper.py` — **v0.1**  
**Script location:** `github.com/jciannel-crypto/bp26-logger`  
**Python environment:** Not yet configured (first code session pending)  
**Last session:** Orientation only — no code written yet  
**Next session builds:** v0.2 — LEARN mode  
**Next session concept:** File I/O + JSON + State persistence

---

## 📦 WHAT v0.1 DOES (current script)

```
injury_scraper.py v0.1
─────────────────────
1. Fetches the NBA injury report page (official.nba.com)
2. Finds the latest PDF link on that page automatically
3. Downloads the PDF into memory (no file saved to disk)
4. Parses the PDF using pdfplumber — extracts text by row position
5. Detects date headers, game headers, team names, and player statuses
6. Prints everything to the terminal in a readable format

WHAT IT CANNOT DO:
- Remember what it saw last time (no state)
- Detect what changed between runs (no comparison)
- Alert you when something changes (no notifications)
- Run automatically on a schedule (manual only)
- Filter to only the games you care about (prints everything)
```

---

## 🔨 WHAT v0.2 WILL BUILD (next session)

**Mode:** 🔵 LEARN  
**Concept being taught:** File I/O + JSON + State persistence  
**The core idea:** How does a program remember something between runs?

**Plain English version of the concept:**  
Right now the script runs, prints to the screen, and forgets everything the moment it finishes. It has no memory. v0.2 teaches it to write down what it saw in a file — like logging a decision in the ledger — so the next time it runs, it can compare what it sees now to what it saw before and tell you what changed.

**What we're adding:**
- After each run, save the full snapshot of all player statuses to a JSON file (`injury_state.json`)
- At the start of the next run, load that file and compare it to the new data
- If any player's status changed, print a clear `CHANGE DETECTED` alert
- If nothing changed, print `No changes since last check`

**Why this matters for BP26:**  
This is the moment the scraper becomes a monitor. Instead of reading every player on every run, the script tells you only what changed. That's the entire foundation of automated monitoring.

**New concepts introduced this session:**
- `json.dump()` — write Python data to a JSON file
- `json.load()` — read a JSON file back into Python
- Dictionary comparison — comparing two snapshots
- Simple if/else logic — if this changed, do that

**Teaching analogies to use:**
- JSON file = the ledger. Structured data written down so you can read it back later.
- State persistence = logging a decision. The program writes what it saw so it remembers next time.
- Change detection = the diff between two ledger snapshots. What's different between then and now?

**Estimated session length:** 45-60 minutes (maybe longer — that's fine)  
**Lines of new code:** ~30-40 lines added to v0.1

---

## 📚 SESSION LOG

### Session 0 — March 14, 2026 (Orientation)
**Type:** Planning / architecture  
**Mode:** N/A  
**Code written:** None  
**Concepts covered:**
- Why Python script > Claude Cowork for background monitoring
- The three-option architecture (manual script vs Cowork vs scheduled agent)
- The v0.1 → v0.6 build progression
- Why injury monitor builds before SII auto-compute
- Hybrid mode protocol designed and locked
- Learner profile documented — starting from zero, systems thinker
- This logging system itself

**Decisions made:**
- Build injury monitor as first Python project
- Use hybrid mode: LEARN for new concepts, BUILD for understood patterns
- Use this log file as session continuity system
- Commit log + script to GitHub after every session
- Version naming: v0.1, v0.2, v0.3 etc.
- Pace: slower than necessary, Jason owns every concept before moving on

**Open questions from this session:** None

---

## 🗺️ FULL BUILD ROADMAP

| Version | What It Does | Concept Taught | Mode | Status |
|---|---|---|---|---|
| v0.1 | Fetch + parse NBA injury PDF, print to terminal | HTTP requests, PDF parsing, BeautifulSoup | N/A | ✅ DONE |
| v0.2 | Save state to JSON, detect changes between runs | File I/O, JSON, state persistence | 🔵 LEARN | 🔜 NEXT |
| v0.3 | Send phone alert when status changes | API integration, Twilio or Pushover | 🔀 HYBRID | ⬜ PENDING |
| v0.4 | Run automatically on a schedule | Task Scheduler (Windows) / cron (Mac) | 🔵 LEARN | ⬜ PENDING |
| v0.5 | Filter to watchlist games only | Lists, filtering, config files | 🟡 BUILD | ⬜ PENDING |
| v0.6 | Write detected changes to BP26 log format | Structured output, data formatting | 🟡 BUILD | ⬜ PENDING |

---

## 🧠 CONCEPTS MASTERED SO FAR

| Concept | Introduced | Mode | Comfortable? |
|---|---|---|---|
| HTTP requests (`requests` library) | v0.1 | N/A | Review needed |
| HTML parsing (BeautifulSoup) | v0.1 | N/A | Review needed |
| PDF parsing (pdfplumber) | v0.1 | N/A | Review needed |
| Regular expressions (re) | v0.1 | N/A | Review needed |
| File I/O + JSON | v0.2 (pending) | 🔵 LEARN | Not yet |
| API integration / alerting | v0.3 (pending) | 🔀 HYBRID | Not yet |
| Scheduling / automation | v0.4 (pending) | 🔵 LEARN | Not yet |
| Filtering / config | v0.5 (pending) | 🟡 BUILD | Not yet |

*Update "Comfortable?" as sessions progress: Not yet → Review needed → Got it → Second nature*

---

## 🔧 ENVIRONMENT SETUP (complete before v0.2 session)

Before the next session, confirm you can run the script locally.  
**If any of these steps fail, start the session with the error — don't try to fix it alone.**

**Step 1 — Check Python is installed. Open a terminal and type:**
```
python --version
```
Should return something like `Python 3.11.2`. If you get an error, download Python from python.org.

**Step 2 — Install required libraries:**
```
pip install requests beautifulsoup4 pdfplumber
```

**Step 3 — Run the current script:**
```
python injury_scraper.py
```
Should print injury data to the terminal. If it runs without errors, your environment is ready.

**How to open a terminal:**
- Windows: Press Windows key, type `cmd`, hit Enter
- Mac: Press Cmd+Space, type `terminal`, hit Enter

**If you hit any errors:** Start the next session by uploading this log,  
the script, AND a screenshot or copy-paste of the exact error message.  
Claude will diagnose and fix it before anything else happens.

---

## 📎 FILE INVENTORY

| File | Location | Purpose |
|---|---|---|
| `injury_scraper.py` | `github.com/jciannel-crypto/bp26-logger` | The Python script |
| `PYTHON_LEARNING_LOG.md` | `github.com/jciannel-crypto/bp26-logger` | This file — session continuity |
| `injury_state.json` | Local machine only (created at v0.2) | State persistence — do NOT commit to GitHub |

---

*BP26 Python Learning Log | Maintained by Claude | Updated end of every session | Do not modify manually — let Claude update this file*
