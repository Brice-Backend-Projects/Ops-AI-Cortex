# Risks and Assumptions – OpsAICortex

## Technical Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-------------|---------|-------------|
| **LLM Response Inconsistency** | Medium | High | Implement temperature control and fallback to deterministic templates. |
| **API Rate Limits** | Medium | Medium | Add request batching and provider rotation (Claude ↔ GPT-4). |
| **Latency During Summarization** | Low | Medium | Asynchronous queue processing; optimize prompt token length. |
| **Slack API Changes** | Low | Low | Version-pin Slack SDK and maintain abstract interface for future platforms. |
| **AWS Deployment Misconfigurations** | Medium | Medium | Use IaC templates and CI validation; maintain dev/test environments. |

## Operational Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-------------|---------|-------------|
| **Credential Mismanagement** | Low | High | Store secrets in AWS Secrets Manager; enforce rotation policies. |
| **Integration Token Expiry** | Medium | Medium | Add auto-renewal hooks for OAuth tokens. |
| **Multi-team Notification Noise** | Medium | Low | Implement per-channel filters and configurable severity levels. |

## Assumptions
- Teams primarily use **GitHub Actions** and **Slack** for DevOps workflow.  
- LLM reasoning tasks are completed within API limits (<30 seconds typical).  
- Claude 3.x or GPT-4 APIs remain accessible with compatible SDKs.  
- AWS account configured with minimal IAM roles for secure deployment.  
- Future integrations will maintain consistent webhook event structures.

## Future Risk Mitigation
- Continuous evaluation of LLM output accuracy with validation datasets.  
- Expansion to support self-hosted LLM endpoints if enterprise compliance requires.  
- Establish governance around AI-generated recommendations (human-in-the-loop verification).
