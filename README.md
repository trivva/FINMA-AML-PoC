# FINMA-AML-Neo4j-PoC
Automating FINMA Compliance & Travel Rule Transaction Monitoring using Graph Databases.

## Context
This repository contains the technical Proof of Concept for my Master Thesis (MSc Business Engineering, UCLouvain / Humboldt-Universität zu Berlin). It aims to demonstrate how Neo4j and Python can automate multi-hop transaction tracing to detect exposure to sanctioned addresses (OFAC), outperforming manual compliance checks.

## Architecture (To-Be)
*   **Data Ingestion:** Python agents interacting with on-chain APIs (Etherscan, Arkham) and local CSV sanctions lists.
*   **Graph Infrastructure:** Neo4j database modeling addresses as nodes and value transfers as relationships.
*   **Filtering Logic:** Cypher queries designed to flag high-risk transaction clusters.

## Current Status
*   Building the initial Python ingestion pipelines (BTC/EVM).
*   Mapping DSR architecture and BPMN compliance workflows.

