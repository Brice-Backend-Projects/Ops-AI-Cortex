# 🧩 OpsAICortex Build Plan — Phased Technical Checklist

A structured, docs-first roadmap for building the **OpsAICortex** system from architecture scaffolding through AWS deployment and AgentKit integration.

---

## **Phase 0 – Environment & Architecture Setup (Current)**

**Goal:** Establish structure, environment, and baseline readiness for development.  
**⏱️ Duration:** 1 week  
**👤 Owner:** Brice  
**Dependencies:** None

### Checklist
- [x] Create `src/ops_ai_cortex/` scaffold and subfolders  
- [x] Create `notebooks/`, `docs/`, `tests/`, `.github/workflows/`  
- [x] Set up virtual environment (`uv`, `poetry`, or `conda`)  
- [x] Create base `pyproject.toml` or `requirements.txt`  
- [ ] Configure `.env` template and `config.py` loader pattern  
- [ ] Initialize logging utility in `utils/logger.py`  
- [ ] Draft README and architecture diagrams  

**📦 Deliverables**
- Functional local VE  
- Directory tree ready for imports  
- Logging + config loader templates  

---

## **Phase 1 – Core Backend Initialization**

**Goal:** Make FastAPI application run locally with minimal endpoints and configuration.  
**⏱️ Duration:** 2 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 0 complete

### Checklist
- [ ] Create `main.py` entrypoint and `create_app()` factory  
- [ ] Add configuration loader (`core/config.py`)  
- [ ] Integrate environment variables via `pydantic.BaseSettings`  
- [ ] Add `/health` and `/version` endpoints  
- [ ] Write `test_smoke.py` for healthcheck  
- [ ] Create `.env.development` and `.env.example`  
- [ ] Add `Dockerfile` (local run only)  

**📦 Deliverables**
- Locally running FastAPI app with smoke tests  
- Containerizable backend  
- Config and environment pattern established  

---

## **Phase 2 – Database & Models**

**Goal:** Implement persistent layer for storing events, summaries, and configuration.  
**⏱️ Duration:** 2–3 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 1 complete

### Checklist
- [ ] Define ORM models: `Repo`, `Event`, `Summary`, `User`  
- [ ] Configure SQLAlchemy + session handling  
- [ ] Initialize Alembic migrations  
- [ ] Create test endpoint for DB insert (`POST /event`)  
- [ ] Write unit tests for CRUD operations  
- [ ] Connect Redis for queue validation  

**📦 Deliverables**
- Working Postgres connection + models  
- Migration scripts  
- Test coverage for DB layer  
- Redis running locally  

---

## **Phase 2.5 – Authentication & Authorization Layer**

**Goal:** Implement secure user identity management, JWT authentication, and role-based access for both API and dashboard.  
**⏱️ Duration:** 2 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 2 (DB operational, `User` model exists)

### Checklist
- [ ] Add `auth/` package under `src/ops_ai_cortex/`  
  - `auth/routes.py` – register/login/logout endpoints  
  - `auth/models.py` – user schema + password hash  
  - `auth/utils.py` – token generation & validation helpers  
- [ ] Implement JWT auth (`PyJWT` or `fastapi-jwt-auth`)  
- [ ] Add password hashing (`bcrypt`)  
- [ ] Create OAuth2 flow (GitHub + Slack optional)  
- [ ] Add dependency injection `get_current_user()`  
- [ ] Enforce role-based access control (admin, viewer)  
- [ ] Write pytest suite for login, token refresh, permissions  

**📦 Deliverables**
- Secure auth system (JWT + hashing)  
- RBAC enforced on API routes  
- Optional OAuth2 integration  
- Tests for auth & restricted routes  

---

## **Phase 3 – Webhook & Queue Integration**

**Goal:** Build the ingestion + async task pipeline for incoming GitHub events.  
**⏱️ Duration:** 2 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 2.5 complete (auth ready for secured webhooks)

### Checklist
- [ ] Implement `/webhooks/github` endpoint  
- [ ] Parse event payload (repo, branch, job_name, status)  
- [ ] Queue event in Redis for async processing  
- [ ] Add background worker (`core/worker.py`)  
- [ ] Log job lifecycle events  
- [ ] Write test suite for enqueue/dequeue  

**📦 Deliverables**
- Asynchronous queue system  
- End-to-end GitHub → Redis → DB flow (no AI yet)  
- Logging verification for event handling  

---

## **Phase 4 – AI Reasoning Engine**

**Goal:** Integrate Claude API for summarization and reasoning from logs.  
**⏱️ Duration:** 3–4 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 3 complete

### Checklist
- [ ] Create `agents/reasoning_engine.py`  
- [ ] Add provider abstraction (Claude ↔ GPT-4)  
- [ ] Implement initial prompt template  
- [ ] Store AI results in DB  
- [ ] Add token usage + latency logging  
- [ ] Mock/stub API for local testing  

**📦 Deliverables**
- Operational AI summarization pipeline  
- Logs → Summary workflow  
- Controlled model-switching logic  

---

## **Phase 5 – Slack Notification Layer**

**Goal:** Deliver generated summaries directly to team channels.  
**⏱️ Duration:** 2 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 4 complete

### Checklist
- [ ] Implement Slack webhook client (`utils/slack_client.py`)  
- [ ] Design message templates (title, summary, action links)  
- [ ] Configure channel mapping per repo in DB  
- [ ] Trigger Slack notifications after summary creation  
- [ ] Add error handling for API limits  
- [ ] Validate via test Slack workspace  

**📦 Deliverables**
- Fully automated Slack delivery  
- Configurable channels  
- Tested message formatting  

---

## **Phase 6 – Go Service (Event Ingestion & Metrics)**

**Goal:** Enable concurrent webhook ingestion and observability.  
**⏱️ Duration:** 3–4 weeks  
**👤 Owner:** Brice  
**Dependencies:** FastAPI core + Slack layer stable

### Checklist
- [ ] Build HTTP listener for GitHub webhooks in Go  
- [ ] Forward payloads securely to FastAPI with JWT  
- [ ] Expose `/metrics` for Prometheus  
- [ ] Add healthcheck + readiness probes  
- [ ] Integrate structured logging  
- [ ] Dockerize Go service  

**📦 Deliverables**
- Working Go sidecar service  
- Observability metrics  
- Secure internal JWT communication  

---

## **Phase 7 – Deployment & CI/CD**

**Goal:** Containerize, automate, and deploy to AWS App Runner.  
**⏱️ Duration:** 3–4 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phases 1–6 functional

### Checklist
- [ ] Create production `Dockerfile` and `docker-compose.yml`  
- [ ] Configure GitHub Actions (lint → test → build → deploy)  
- [ ] Deploy to AWS App Runner  
- [ ] Connect AWS RDS Postgres, Secrets Manager, CloudWatch  
- [ ] Verify IAM policies and env secrets  
- [ ] Document deployment flow  

**📦 Deliverables**
- AWS-hosted OpsAICortex  
- CI/CD automation  
- Centralized logging + secret management  

---

## **Phase 8 – Dashboard & Insights**

**Goal:** Provide visualization and configuration interface for summaries.  
**⏱️ Duration:** 3 weeks  
**👤 Owner:** Brice  
**Dependencies:** Backend + auth stable (Phases 2.5 + 7)

### Checklist
- [ ] Add FastAPI template UI or React frontend  
- [ ] Display summary history, repo status, filters  
- [ ] Integrate authentication (RBAC)  
- [ ] Polish for presentation/demo  
- [ ] Document feature roadmap  

**📦 Deliverables**
- Usable dashboard  
- Demo-ready UI with secure access  

---

## **Phase 9 – AgentKit Integration & Future Expansion**

**Goal:** Connect Cortex with AgentKit ecosystem and finalize v1.  
**⏱️ Duration:** 4–5 weeks  
**👤 Owner:** Brice  
**Dependencies:** Phase 8 complete

### Checklist
- [ ] Implement wrapper adapter to interact with AgentKit  
- [ ] Benchmark latency + reliability  
- [ ] Add model routing layer (Claude, GPT-4, Ollama)  
- [ ] Extend documentation (`agent_integration_flow.md`)  
- [ ] Record video demo + publish devbybrice.com write-up  

**📦 Deliverables**
- AgentKit-integrated architecture  
- Modular intelligence layer  
- Published technical showcase  

---

## 🧱 **Estimated Total Duration**
≈ **26–29 weeks (~6–7 months)**  
_Docs-first, architecture-before-implementation cadence._

---

## 📊 **Progress Tracker**

| Phase | Title | Duration | Status | % Complete | Notes |
|-------|--------|-----------|----------|-------------|--------|
| 0 | Environment & Architecture | 1 wk | 🟢 In Progress | 70% | Folder structure done |
| 1 | Core Backend Init | 2 wks | ⚪ Not Started | 0% | Config & health next |
| 2 | Database & Models | 3 wks | ⚪ Not Started | 0% | Schema foundation |
| 2.5 | Auth/Authz Layer | 2 wks | ⚪ Not Started | 0% | JWT + RBAC setup |
| 3 | Webhook & Queue | 2 wks | ⚪ Not Started | 0% | Secured webhooks |
| 4 | AI Reasoning Engine | 4 wks | ⚪ Not Started | 0% | Claude/GPT integration |
| 5 | Slack Notification | 2 wks | ⚪ Not Started | 0% | Webhook templates |
| 6 | Go Service & Metrics | 4 wks | ⚪ Not Started | 0% | Concurrent ingestion |
| 7 | Deployment & CI/CD | 4 wks | ⚪ Not Started | 0% | AWS App Runner |
| 8 | Dashboard & Insights | 3 wks | ⚪ Not Started | 0% | Post-MVP UI |
| 9 | AgentKit Integration | 5 wks | ⚪ Not Started | 0% | Final wrap |

---

## ✅ **Deliverables Summary**

- FastAPI + Go microservice architecture  
- Redis + PostgreSQL persistence  
- Secure JWT/OAuth2 auth layer  
- Slack-integrated AI summarization  
- AWS App Runner CI/CD deployment  
- Modular AgentKit integration  
- Dashboard UI + documentation for portfolio showcase  

---

_Authored by Brice Nelson — November 2025_
