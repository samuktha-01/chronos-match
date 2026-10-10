# ChronosMatch: Zero-Copy High-Frequency Trading Engine

A high-performance trading engine foundation designed for ultra-low latency, zero-copy message handling, and deterministic order execution.

## Status

Project Foundation & Initialization phase. Core architecture and environment setup established.

## Features & Roadmap

- **Zero-Copy Architecture**: Shared memory and cache-aligned memory layout for minimal serialization overhead.
- **Deterministic Matching Engine**: Price-time priority order book execution.
- **Lock-Free Ring Buffer**: High-throughput message queuing between ingestion and execution threads.
- **Python & Cython/C Extension Layer**: Python developer ergonomics paired with C-speed critical path execution.
- **Telemetry & Telemetry Guardrails**: Granular latency tracing and metrics.

## Repository Structure

```text
Chronos-match/
├── .env.example              # Template environment configuration
├── .gitignore                 # Exclusion rules for caches, venvs, and build outputs
├── pyproject.toml             # Project metadata, build system, and pytest configuration
├── requirements.txt           # Minimal dependencies for local development
├── README.md                  # Project overview and developer instructions
├── docs/
│   └── architecture.md        # Architectural design documentation
├── src/
│   └── chronosmatch/          # Core package source tree
│       └── __init__.py        # Package initialization and version
└── tests/
    └── test_project_setup.py  # Environment, packaging, and import tests
```

## Getting Started

### Prerequisites

- Python 3.12+
- Git

### Virtual Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies in editable mode:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   ```

### Running Tests

Execute the test suite using `pytest`:
```bash
pytest
```
