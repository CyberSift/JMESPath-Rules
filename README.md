<p align="center">
  <img src="https://raw.githubusercontent.com/CyberSift/JMESPath-Rules/refs/heads/main/docs/logo.png" alt="CyberSift logo" width="220">
</p>

# CyberSift JMESPath Rules

Detection rules for [CyberSift.io](https://cybersift.io/) and Sentio SIEM, written in [JMESPath](https://jmespath.org/) and maintained as version-controlled detection content.

This repository provides a practical rule library for identifying suspicious activity across structured security events. Rules are designed to be readable, reviewable, and easy to manage as part of a modern SIEM detection workflow.

## Overview

CyberSift helps security teams collect, analyze, and act on security telemetry through Sentio SIEM. This rule repository supports that workflow by keeping detection logic transparent and maintainable.

Each rule is written using JMESPath, a query language for JSON data. This makes the rules well suited for evaluating normalized event data and expressing detection logic in a clear, consistent format.

## What This Repository Contains

- SIEM detection rules written in JMESPath
- Rule content intended for CyberSift/Sentio SIEM workflows
- Version-controlled detection logic for review, maintenance, and improvement
- A source repository for rules published to the CyberSift rule catalog
- Some of the rules include "cybersift" fields which are proprietary to Sentio SIEM

## Published Rule Catalog

The published rules are available at:

[https://rules.cybersift.io/](https://rules.cybersift.io/)

## Rule Management Documentation

For details about managing rules in Sentio SIEM, see:

[Sentio SIEM Rule Management](https://outline.cybersift.io/s/sentio-siem/doc/rule-management-1bCmPqUgBb)

## Repository

[CyberSift/JMESPath-Rules](https://github.com/CyberSift/JMESPath-Rules/)
