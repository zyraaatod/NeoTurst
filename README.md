# 🐉 NeoTurst: NightFury Maximum Destruction v5.0

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux%20%7C%20macOS-green.svg)]()

**NeoTurst** (NightFury) is an industrial-grade, maximum-destruction security scanner designed for comprehensive penetration testing. It integrates multiple specialized tools and utilizes over 50+ advanced scanning methods to identify critical vulnerabilities with zero-error precision.

---

## 🚀 Core Capabilities

NeoTurst is equipped with a powerhouse of scanning modules, each targeting specific vulnerability classes:

### 💉 Injection Modules
- **SQL Injection (14 Types):** Error-based, Time-based Blind, Boolean-based Blind, Union-based, and deep payload generation (500+ payloads).
- **Command Injection (6 Types):** Both time-based and output-based detection for Linux and Windows targets.
- **XXE (XML External Entity):** Detecting file disclosure and SSRF via XML parsing.
- **SSTI (Server-Side Template Injection):** Identification for various template engines (Jinja2, Mako, Twig, etc.).

### 🌐 Web Vulnerability Modules
- **XSS (8 Types):** Reflected, Stored, and DOM-based Cross-Site Scripting with advanced WAF bypass payloads.
- **SSRF (Server-Side Request Forgery):** Internal port scanning and metadata service exploitation (AWS, GCP, Azure).
- **Open Redirect:** Scanning for malicious redirection via common parameter names.
- **LFI/RFI/Path Traversal:** Deep directory traversal scanning with 500+ payloads for critical file disclosure.

### 🔍 Discovery & Information Gathering
- **Sensitive File Scanner:** Automatically discovers `.env`, backups, logs, SSH keys, git configs, and database dumps.
- **Integrated Crawling:** Sophisticated endpoint discovery and form parsing to map the target attack surface.
- **WAF Detection & Fingerprinting:** Identify technologies and security layers (CMS, Frameworks, Servers).

---

## 🛠️ Integrated Power Tools

NeoTurst isn't just a script; it's a curated ecosystem:

| Tool | Description |
| :--- | :--- |
| **NightFury Engine** | The main Python core for multi-threaded vulnerability analysis. |
| **ffuf** | Brazingly fast web fuzzer written in Go. |
| **sqlmap** | The legendary automatic SQL injection and database takeover tool. |
| **Custom Fuzzer** | A high-performance Go-based directory fuzzer optimized for speed. |
| **Curated Wordlists** | 20,000+ entries for VHosts, CVE paths, parameters, and more. |

---

## 📥 Installation

### Prerequisites
Ensure you have Python 3.x and Go installed on your system.

### Setup
```bash
# Clone the repository
git clone https://github.com/zyraaatod/NeoTurst.git
cd NeoTurst

# Install Python dependencies
pip install -r requirements.txt || pip install requests colorama beautifulsoup4 urllib3

# Build the custom fuzzer (optional but recommended)
cd fuzzer
go build -o fuzz .
mv fuzz ../
cd ..
```

---

## ⚡ Quick Start

Launch the main engine:
```bash
python3 nightfury.py
```

Follow the interactive prompts:
1. Enter your target URL (e.g., `http://example.com`)
2. Let the NightFury engine crawl and analyze.
3. Review the detailed vulnerability report.

---

## 🛡️ Disclaimer

**For Educational and Ethical Testing Purposes Only.**

The use of NeoTurst for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">
  Developed with ❤️ for the Security Community
</p>
