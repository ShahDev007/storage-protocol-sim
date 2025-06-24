# Storage Protocol Simulator & Verification Suite

[![CI](https://github.com/ShahDev007/storage-protocol-sim/actions/workflows/ci.yml/badge.svg)](https://github.com/ShahDev007/storage-protocol-sim/actions)

This suite simulates and validates storage protocol operations such as NVMe and SCSI read/write commands, useful for educational, CI/CD, or integration testing scenarios.

---

## 📦 Features

- 🔁 Simulated NVMe and SCSI I/O patterns using Python
- 🧪 Validated using Pytest with timing assertions
- 📝 Linux log parser to scan for NVMe errors
- ✅ GitHub Actions CI with mock I/O in headless environments

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/ShahDev007/storage-protocol-sim.git
cd storage-protocol-sim
pip install -r requirements.txt
