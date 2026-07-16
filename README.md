# Azure IAM Governance Tool

This project provides an automated audit script to identify high-risk, privileged accounts in Azure environments.

## Purpose
The script aligns with security frameworks such as **NIST SP 800-53** and **COBIT** by auditing privileged access and identifying dormant accounts.

## Prerequisites
* Azure CLI (az) must be installed and authenticated.
* Python 3.x installed.

## Usage
1. Authenticate with Azure: `az login`
2. Run the audit: `python3 src/iam_audit.py`
