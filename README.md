# Azure IAM Governance Tool

An automated python GRC (Governance, Risk, and Compliance) utility designed to enhance identity security within Azure environments by identifying high-risk and dormant accounts.

## Overview
This python project provides an automated audit script to identify privileged accounts that lack recent sign-in activity. By flagging accounts that have been inactive for more than 90 days, this tool assists in enforcing the principle of least privilege and maintaining robust access control policies.

## Security Alignment
This pyhton script aligns with industry-standard security frameworks, including:
* **NIST SP 800-53**: Specifically addressing access control (AC) and account management (AC-2) controls.
* **COBIT**: Supporting the governance of enterprise IT by ensuring authorized access and compliance.

## Prerequisites
* **Azure CLI (az)**: Must be installed and authenticated (`az login`).
* **Python 3.x**: Installed on the host machine.
* **Libraries**: `python-dotenv` for secure configuration management.

## Installation & Setup
1. Clone this repository:
   `git clone https://github.com/YOUR_USERNAME/azure-iam-governance-tool.git`
2. Install dependencies:
   `pip install python-dotenv`
3. Configure your environment:
   Create a `.env` file in the root directory and add your subscription ID:
   `AZURE_SUBSCRIPTION_ID=your-subscription-id-here`

## Usage
Run the audit script from the terminal:
`python3 src/iam_audit.py`

## Security Practices
* **Environment Isolation**: Sensitive credentials are managed via an `.env` file, which is excluded from version control.
* **Version Control**: Best practices are maintained by utilizing `.gitignore` to prevent the exposure of local configuration and system files.







## Usage
1. Authenticate with Azure: `az login`
2. Run the audit: `python3 src/iam_audit.py`
