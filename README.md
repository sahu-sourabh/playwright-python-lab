# Playwright Python Lab: Hybrid AI-SDET 🚀
An R&D Repository for Asynchronous Quality Engineering & Agentic Testing.

[![Playwright Tests](https://github.com/sahu-sourabh/playwright-python-lab/actions/workflows/main_pipeline.yml/badge.svg)](https://github.com/sahu-sourabh/playwright-python-lab/actions/workflows/main_pipeline.yml)

## 🏗️ Modern Modular Architecture
This lab is built using a **Domain-Driven Design (DDD)** approach to ensure scalability and separation of concerns:
- **`core/`**: The engine room containing Custom Async API Clients and Browser configurations.
- **`pages/`**: Page Object Models (POM) representing the application state and UI interactions.
- **`infra/`**: Infrastructure as Code, including Docker-compose and environment utilities.
- **`configs/`**: Centralized environment-specific settings and secret management.
- **`data/`**: Structured test data and Pydantic models for API request/response validation.
- **`legacy/`**: Archived previous implementations for historical reference.

## 🛠️ Tech Stack
- **Language**: Python 3.12+ (Optimized for Async/Await patterns)
- **Framework**: Pytest + Playwright (Plugin-based architecture)
- **API Engine**: HTTPX (High-performance asynchronous HTTP client)
- **Config Management**: Pydantic-Settings (Environment variable validation)
- **Build System**: `pyproject.toml` (Following PEP 518/621 Standards)
- **Linting/Formatting**: Ruff (Ensuring high-quality, code standards)
- **CI/CD**: GitHub Actions using Node 24 runners for modern performance.

## 🚀 Quick Start (Local Setup)
Follow these steps to replicate the lab environment:

1. **Clone & Create Virtual Env**:
- python -m venv .venv
- Windows: .venv\Scripts\activate
- Mac/Linux: source .venv/bin/activate

2. **Install Local Package & Dependencies**:
- pip install .
- playwright install chromium

3. **Configure Environment**:
- Create a .env file in the root directory (referencing .env_example)

4. **Run Tests**:
- pytest

## 🚀 Latest Milestones
- [x] **Async API Engine**: Implemented AsyncAPIClient with centralized logging.
- [x] **Type-Safe Configuration**: Migrated to Pydantic-Settings for robust .env management.
- [x] **Multi-Target Support**: Infrastructure ready for both SauceDemo (UI) and Restful-Booker (API/Hybrid).

## 📈 Engineering Objectives
- **Hybrid Testing Flow**: Executing API-first setups (e.g., Auth/Data seeding) followed by UI verification.
- **Asynchronous Execution**: Reducing CI/CD bottleneck by leveraging non-blocking I/O.
- **Correlation Tracing**: Implementing X-Correlation-ID in API clients for observability.
- **Atomic Commits**: Maintaining a clean, traceable Git history for collaborative growth.
- **Modern Standards**: Using pyproject.toml for unified, standardized configuration.