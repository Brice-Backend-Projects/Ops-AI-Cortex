
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
- AI_PROVIDER = "claude" for short prompts, "gpt-4" for longer ones. 
- AI_API_KEY = <key> for Claude, <key> for GPT-4.


## Communication Integrations
| Platform | Status | Description |
|-----------|---------|-------------|
| Slack | ✅ MVP | Summaries delivered via webhook |
| Microsoft Teams | 🔜 Planned | Future integration for enterprise users |
| Discord | 🔜 Planned | Optional for open-source community use |

## Infrastructure
- **AWS App Runner** – primary deployment target for API and microservices.  
- **AWS Secrets Manager** – stores credentials and API keys.  
- **AWS CloudWatch** – logs and metrics.  
- **Docker Compose** – local development environment orchestration.

## Development Environment
- Local environment managed via `uv` or `poetry`.  
- Testing through GitHub Actions CI/CD.  
- Conda environment optional for notebook experimentation.

