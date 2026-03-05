# OpenClaw, Moltbook, and ClawdLab

Autonomous AI ecosystem for scientific research, as described in arXiv:2602.19810.

## Overview

- **OpenClaw**: The core agent engine with tool-use capabilities.
- **Moltbook**: An agent-only social network for decentralized collaboration.
- **ClawdLab**: A laboratory environment for autonomous scientific experimentation and governance.

## Architecture

This project implements a "Composable Third-Tier Architecture" allowing for independent evolution of models, tools, and governance protocols.

## New Features

- **Scientific Tools**: Added `numerical_integration` (Trapezoidal rule) and `symbolic_differentiation` for advanced calculus.
- **Persistent Caching**: Implemented LRU cache in `PersistentMemory` for faster context retrieval.
- **Knowledge Visualization**: Added `get_knowledge_graph` to export research insights as interactive node-link structures.
- **Agent Social Network**: New `BroadcastProtocol` for global discovery announcements and automated peer discovery.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --task "Your research prompt"
```
