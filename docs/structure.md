# Structure

ops_ai_cortex/
│
├── src/
│   └── ops_ai_cortex/
│       ├── api/
│       │   └── __init__.py
│       ├── agents/
│       │   └── __init__.py
│       ├── auth/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── schemas.py
│       │   ├── utils.py
│       │   ├── dependencies.py
│       │   └── routes.py
│       ├── config/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   └── config.yaml
│       ├── go_services/
│       │   ├── go.mod
│       │   └── main.go
│       ├── core/
│       │   └── __init__.py
│       ├── utils/
│       │   └── __init__.py
│       ├── __init__.py
│       └── main.py
│
├── notebooks/
│   ├── 00_prompt_experiments.ipynb
│   ├── 01_traceback_summarization.ipynb
│   ├── 02_log_pattern_detection.ipynb
│   └── 03_agent_response_refinement.ipynb
│
├── tests/
│   ├── __init__.py
│   └── test_smoke.py
│
├── docs/
│   ├── 00_overview.md
│   ├── 01_scope.md
│   ├── 02_architecture.md
│   ├── 03_tech_stack.md
│   ├── 04_milestones.md
│   └── 05_risks_and_assumptions.md
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .github
    └── workflows
        └── ci-cd.yml
