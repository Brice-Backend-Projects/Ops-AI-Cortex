# System Architecture – OpsAICortex

## High-Level Overview
OpsAICortex is composed of modular backend services that ingest operational data, apply AI reasoning, and deliver summarized intelligence to collaboration channels.

### Core Flow
1. **Event Ingestion:**  
   The Go microservice listens to GitHub and CI/CD webhooks and forwards structured payloads to the FastAPI core.
2. **Processing & Storage:**  
   FastAPI parses incoming data, stores metadata in PostgreSQL, and queues reasoning tasks via Redis.
3. **AI Reasoning Layer:**  
   Queued tasks are processed by the AI agent engine powered by Claude 3.x (or GPT-4), which interprets logs and produces summaries.
4. **Notification Layer:**  
   Summaries are formatted and sent to Slack using structured message templates.  Post-MVP versions will support Microsoft Teams and Discord.
5. **Dashboard & API:**  
   A lightweight FastAPI UI provides configuration and insight visualization.

## Component Diagram

```mermaid
flowchart TD
    A[GitHub / CI/CD Pipelines] -->|Webhook Events| B[Go Service<br>(Event Ingestion & Metrics)]
    B -->|HTTP / JWT| C[FastAPI Core<br>(Task Routing & API Layer)]
    C --> D[Redis Queue<br>(Async Job Management)]
    C --> E[PostgreSQL DB<br>(Config, History, Results)]
    D --> F[AI Reasoning Engine<br>(Claude 3.x / GPT-4)]
    E --> F
    F -->|Summaries / Actions| G[Slack Integration<br>(MVP Channel)]
    G --> H[Future Integrations<br>Teams / Discord]
```

```text
                   ┌────────────────────────────┐
                   │        GitHub / CI/CD      │
                   │    (Actions, Pipelines)    │
                   └──────────────┬─────────────┘
                                  │ Webhook Events
                                  ▼
                   ┌────────────────────────────┐
                   │        Go Service          │
                   │ (Event Ingestion & Metrics)│
                   └──────────────┬─────────────┘
                                  │ HTTP / JWT
                                  ▼
                   ┌────────────────────────────┐
                   │       FastAPI Core         │
                   │ (Task Routing & API Layer) │
                   └───────┬────────┬───────────┘
                           │        │
                           │        │
                           ▼        ▼
          ┌────────────────────────┐   ┌────────────────────────┐
          │       Redis Queue       │   │     PostgreSQL DB      │
          │ (Async Job Management)  │   │ (Config & History)     │
          └────────────┬────────────┘   └────────────┬───────────┘
                       │                             │
                       │ AI Tasks                    │ Results / Past Summaries
                       ▼                             ▼
           ┌───────────────────────────────┐          │
           │     AI Reasoning Engine       │◄─────────┘
           │ (Claude 3.x / GPT-4 via API)  │
           │  - Log & traceback analysis   │
           │  - Root cause identification  │
           │  - Fix recommendations        │
           └────────────┬──────────────────┘
                        │ Summaries / Actions
                        ▼
          ┌────────────────────────────────┐
          │        Slack Integration        │
          │ (MVP Notification Channel)      │
          │ Future: Teams / Discord Hooks   │
          └────────────────────────────────┘
```

## System Context / Deployment Diagram

*See the “System Context” diagram below for the broader AWS deployment view. It illustrates how OpsAICortex components interact with AWS services, CI/CD systems, communication tools, and AI model APIs to deliver real-time operational intelligence.*

```mermaid
flowchart TD
    subgraph Users
        U1[Developer / PM User<br>Slack Notifications & Dashboard]
    end

    subgraph ExternalTools
        G1[GitHub / CI/CD Pipelines<br>Webhook Events]
    end

    subgraph AWS[OpsAICortex – AWS Deployment]
        A1[App Runner<br>FastAPI + Go Containers]
        A2[RDS PostgreSQL]
        A3[Redis (Elastic Cache)]
        A4[AWS Secrets Manager]
        A5[Claude 3.x / GPT-4 APIs]
        A6[AWS CloudWatch / IAM]
    end

    subgraph Comms[Communication Layer]
        C1[Slack – MVP]
        C2[Microsoft Teams – Future]
        C3[Discord – Future]
    end

    G1 --> A1
    A1 --> A2
    A1 --> A3
    A1 --> A4
    A1 --> A5
    A1 --> C1
    C1 --> U1
    U1 -->|Feedback / Commands| C1
    A6 --> A1
    C1 --> C2
    C1 --> C3
```

```text
                                ┌────────────────────────────┐
                                │     Developer / PM User    │
                                │ (Views Slack Notifications │
                                │   and Project Dashboards)  │
                                └──────────────┬─────────────┘
                                               │
                                               ▼
                              ┌─────────────────────────────────┐
                              │         Communication Layer      │
                              │   Slack (MVP), Teams, Discord    │
                              └────────────────┬─────────────────┘
                                               │ Webhooks / API Calls
                                               ▼
               ┌────────────────────────────────────────────────────────┐
               │                    OpsAICortex (AWS)                   │
               │                                                        │
               │  ┌──────────────────────────────┐   ┌────────────────┐ │
               │  │        App Runner            │   │     RDS        │ │
               │  │ (FastAPI + Go Containers)    │   │ (PostgreSQL)   │ │
               │  └──────────────┬───────────────┘   └──────┬─────────┘ │
               │                 │                           │          │
               │                 ▼                           ▼          │
               │   ┌───────────────────────┐     ┌────────────────────┐ │
               │   │     Redis (Elastic)   │     │ AWS Secrets Manager│ │
               │   │  Async Queues & Cache │     │   API Keys / Tokens│ │
               │   └───────────┬───────────┘     └─────────┬──────────┘ │
               │               │                             │          │
               │               ▼                             │          │
               │   ┌────────────────────────────┐             │         │
               │   │ Claude 3.x / GPT-4 APIs    │◄────────────┘         │
               │   │   External AI Providers    │                       │
               │   └────────────────────────────┘                       │
               │                                                        │
               │   AWS CloudWatch → Logs / Metrics / Traces             │
               │   AWS IAM → Roles & Permissions                        │
               └────────────────────────────────────────────────────────┘
                                               │
                                               ▼
                                ┌────────────────────────────┐
                                │     GitHub / CI/CD Tools   │
                                │  (Triggers Webhook Events) │
                                └────────────────────────────┘
```

## Key Components
| Component | Language | Purpose |
|------------|-----------|----------|
| **FastAPI Core** | Python | Main orchestration layer and API interface |
| **AI Agent Engine** | Python (LangChain) | Handles reasoning, summarization, and suggestion generation |
| **Go Microservice** | Go | Handles concurrent event ingestion, metrics, and health monitoring |
| **Redis** | N/A | Task queue and cache for AI job coordination |
| **PostgreSQL** | N/A | Persistent storage for configuration, results, and history |
| **Slack Integration** | N/A | Communication layer for notifications |
| **AWS Deployment** | Infrastructure | Containerized via Docker and deployed on AWS App Runner |

## 🧪 AI Research & Prototyping Layer
AI behavior and summarization logic are developed and validated in Jupyter notebooks before production integration.  
This ensures that prompt engineering, model selection, and reasoning accuracy are iterated rapidly without disrupting backend stability.

**Referenced Notebooks:**
- `00_prompt_experiments.ipynb` – testing summarization style and accuracy  
- `01_traceback_summarization.ipynb` – analyzing CI/CD errors and exception text  
- `02_log_pattern_detection.ipynb` – identifying recurring failure types  
- `03_agent_response_refinement.ipynb` – tuning language tone for Slack summaries  

See the `/notebooks` directory for detailed experimentation results and findings.

## Security & Authentication
- Internal API communication uses **JWT-based authentication** between Go and FastAPI.  
- OAuth2 via **GitHub** and **Slack** for external integrations.  
- All secrets stored securely in **AWS Secrets Manager**.

## Deployment Overview
- Each service is containerized with Docker.  
- Deployed to AWS App Runner for simplicity and automatic scaling.  
- Logging and metrics routed through CloudWatch.  
- Future iterations may adopt ECS or EKS for advanced orchestration.

## Scalability Considerations
- Asynchronous processing via Celery/RQ workers.  
- Horizontal scaling on the FastAPI layer to handle parallel AI calls.  
- Model reasoning configurable to use Claude or GPT-4 based on context length and cost.
