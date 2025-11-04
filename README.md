# 🧠 OpsAICortex  
## AI-Driven Operational Intelligence and Coordination Platform

| Branch | Build Status | Python | Go | Project Status |
|---------|---------------|--------|----|----------------|
| **main** | [![Main Build](https://github.com/Brice-Backend-Projects/OpsAICortex/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/Brice-Backend-Projects/OpsAICortex/actions/workflows/ci-cd.yml) | ![Python Version](https://img.shields.io/badge/python-3.12-blue.svg) | ![Go Version](https://img.shields.io/badge/go-1.23-lightblue.svg) | ![Status](https://img.shields.io/badge/status-in%20development-orange) |
| **dev** | [![Dev Build](https://github.com/Brice-Backend-Projects/OpsAICortex/actions/workflows/ci-cd.yml/badge.svg?branch=dev&event=push)](https://github.com/Brice-Backend-Projects/OpsAICortex/actions/workflows/ci-cd.yml)
 | – | – | – |


---

## 🚀 Overview
**OpsAICortex** is an AI-powered backend platform that transforms DevOps data into actionable insight.  
It continuously monitors CI/CD pipelines, interprets logs and tracebacks through advanced reasoning models, and posts clear, concise summaries directly into team communication channels.

The system serves as the **cortex** for modern engineering operations—an intelligent orchestration layer that brings together automation, observability, and communication.

Built with **FastAPI**, **Go**, and **LangChain**, OpsAICortex is designed to demonstrate what applied AI looks like when it’s embedded inside production-grade backend systems.

---

## 🎯 Vision
OpsAICortex bridges the gap between DevOps automation and human decision-making.  
By applying large language models (LLMs) such as **Claude 3.x** and **GPT-4** to operational data, the platform enables engineering leaders and project managers to:

- Detect failures across multiple repositories  
- Understand root causes instantly  
- Receive recommended fixes within seconds  
- Collaborate on incidents directly in Slack  

OpsAICortex turns noisy log data into narrative clarity—empowering teams to move faster with confidence.

---

## 🧩 System Concept
The platform listens to CI/CD events (initially via **GitHub Actions**) and routes them through an asynchronous pipeline:
1. **Event Ingestion** → Go microservice receives webhook payloads.  
2. **Processing Layer** → FastAPI core stores and queues analysis tasks in Redis.  
3. **AI Reasoning Engine** → Claude or GPT-4 interprets logs and tracebacks.  
4. **Summarization & Delivery** → Slack receives a readable summary with potential fixes.  
5. **History & Correlation** → PostgreSQL retains results for trend analysis and dashboard reporting.

Future updates will expand the communication layer beyond Slack, adding **Microsoft Teams** and **Discord** for broader collaboration.

---

## 🧭 Deployment Target
OpsAICortex is architected for **AWS App Runner**, leveraging:
- **PostgreSQL (RDS)** for persistence  
- **Redis (Elasticache)** for queue management  
- **AWS Secrets Manager** for secure credential storage  
- **CloudWatch** for metrics and observability  

This design aligns with real-world DevOps infrastructure patterns while maintaining modular portability.

---

## 🧪 AI Research & Prototyping
AI summarization logic and pattern-detection routines are prototyped within the `/notebooks` directory.  
These notebooks serve as the experimental foundation for the production AI agents located in `src/ops_ai_cortex/agents/`.  

Key exploratory notebooks:
- `00_prompt_experiments.ipynb` – summary style & tone comparisons  
- `01_traceback_summarization.ipynb` – structured exception analysis  
- `02_log_pattern_detection.ipynb` – clustering similar build failures  
- `03_agent_response_refinement.ipynb` – improving Slack response clarity  

---

## 🧱 Architecture Snapshot

```text
GitHub → Go Service → Redis Queue → FastAPI Core → Claude/GPT → Slack
                                      │
                                      └─ PostgreSQL (state, history)
```

> See `/docs/02_architecture.md` for detailed component and system-context diagrams.

---

## 🔍 Development Status
OpsAICortex is currently in **active development**.  
The architecture, documentation, and foundational AI modules are being established before integration testing begins.  

All design artifacts, architecture diagrams, and milestone plans are available in the `/docs` directory.

---

## 📘 Documentation Index
| File | Description |
|------|--------------|
| [`00_overview.md`](docs/00_overview.md) | Executive summary and vision |
| [`01_scope.md`](docs/01_scope.md) | MVP scope and success criteria |
| [`02_architecture.md`](docs/02_architecture.md) | System and AWS deployment architecture |
| [`03_tech_stack.md`](docs/03_tech_stack.md) | Languages, frameworks, and tools |
| [`04_milestones.md`](docs/04_milestones.md) | Phase roadmap from MVP to production |
| [`05_risks_and_assumptions.md`](docs/05_risks_and_assumptions.md) | Risk assessment and mitigation strategy |

---

## 🧭 Author
**OpsAICortex** is a professional-grade backend project by *Brice Nelson*, focused on demonstrating scalable AI integration within DevOps ecosystems.

For more of Brice’s work in backend and applied AI engineering, visit:  
👉 [https://www.devbybrice.com](https://www.devbybrice.com)

---

> *“Intelligence is not about automation — it’s about understanding. OpsAICortex brings that understanding to operations.”*


