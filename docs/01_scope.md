# Project Scope – OpsAICortex

## In Scope (MVP)
- Integration with **GitHub Actions** for build and test event ingestion.  
- Parsing of logs and tracebacks using **Claude 3.x** for summarization.  
- AI-generated root-cause explanations and suggested fixes.  
- Real-time delivery of incident summaries to **Slack channels** via webhook.  
- Simple configuration dashboard (FastAPI) for connecting projects and channels.  
- Secure storage of credentials (GitHub, Slack) using environment variables and AWS Secrets Manager.  
- Core backend implemented in **Python (FastAPI)** with **Go microservice** for concurrency and monitoring.

## Future Expansion
- **Microsoft Teams and Discord** integrations for cross-platform notifications.  
- Support for **Jira** and **Linear** to open or update incident tickets automatically.  
- Integration with observability tools (Datadog, Prometheus, Sentry).  
- Enhanced correlation engine for identifying recurring failure patterns.  
- Role-based access control and team analytics dashboard.  
- Deployment automation templates for multi-environment rollouts.

## Out of Scope (MVP)
- Real-time build execution or direct code modification.  
- Long-term log retention beyond summarized insights.  
- Model training or fine-tuning pipelines (OpsAICortex consumes pre-trained LLM APIs).  
- Multi-tenant SaaS hosting (initial release targets single-organization deployment).

## Success Criteria
- AI summaries reduce average incident triage time by 50%.  
- 95% accuracy in identifying root causes across test cases.  
- System reliably delivers summaries within 30 seconds of event ingestion.  
- Slack summaries are contextually relevant and human-readable.
