
```
██╗  ██╗███████╗ ██████╗ ████████╗██╗   ██╗██████╗ ███████╗████████╗
██║  ██║██╔════╝██╔═══██╗╚══██╔══╝██║   ██║██╔══██╗██╔════╝╚══██╔══╝
███████║█████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗     ██║   
██╔══██║██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝     ██║   
██║  ██║███████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   
```

# NeoTurst — NightFury Maximum Destruction v5.0

<p align="center">
  <b>INDUSTRIAL GRADE · 50+ METHODS · ZERO ERROR</b><br>
  <i>Advanced All-in-One Web Vulnerability Scanner & Penetration Testing Toolkit</i>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/go-1.21+-00ADD8?logo=go&logoColor=white" alt="Go"></a>
  <a href="#"><img src="https://img.shields.io/badge/platform-Linux%20%7C%20Termux%20%7C%20macOS-green" alt="Platform"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-yellow" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/status-active-success" alt="Status"></a>
</p>

---

## 📋 Overview

**NeoTurst** is an industrial-grade security assessment suite powered by the **NightFury Maximum Destruction v5.0** engine. It combines a custom multi-threaded Python vulnerability scanner with industry-standard tools like **sqlmap**, **ffuf**, and **paramspider**, plus curated wordlists — all in one unified toolkit.

> **⚠️ DISCLAIMER:** This tool is for **authorized security testing and educational purposes only**. Unauthorized use against targets without explicit consent is illegal. You are responsible for complying with all applicable laws.

---

## 🔥 Features

### ⚡ Performance Optimizations

| Feature | Detail |
|---------|--------|
| **Concurrent Scanner** | ThreadPoolExecutor — 20 parallel requests per test module |
| **Combinatorial Payloads** | 200+ unique payloads per category (non-time-based) |
| **Time-Based Efficiency** | 50 targeted time-delay payloads per sleep-based module |
| **Session Reuse** | Connection pooling through `requests.Session` |

### 🧠 NightFury Scanning Engine (18 Modules)

| Category | Module | Description |
|----------|--------|-------------|
| **Injection** | SQLi (Error) | Error-based SQL injection detection |
| | SQLi (Time) | Time-based blind SQL injection |
| | SQLi (Boolean) | Boolean-based blind inference |
| | SQLi (UNION) | UNION-based column enumeration |
| | Command Injection | OS command injection (time & output-based) |
| | SSTI | Server-Side Template Injection (Jinja2, Mako, Twig, etc.) |
| | XXE | XML External Entity injection |
| **XSS** | Reflected XSS | Non-persistent cross-site scripting |
| | Stored XSS | Persistent cross-site scripting |
| | DOM XSS | DOM-based cross-site scripting |
| **File** | LFI / RFI | Local & Remote File Inclusion |
| | Sensitive Files | `.env`, backups, SSH keys, git configs, DB dumps |
| **Infra** | Port Scanner | Basic service & port discovery |
| | WAF Detection | Web Application Firewall fingerprinting |
| | Tech Fingerprinting | CMS, framework, server header detection |
| **Web** | SSRF | Server-Side Request Forgery |
| | Open Redirect | URL redirect vulnerability |
| | CORS Misconfig | Cross-Origin Resource Sharing analysis |
| | CSRF | Cross-Site Request Forgery |
| | Clickjacking | Frame-options protection check |
| | Security Headers | Missing HTTP security header audit |

### 🧰 Integrated Tools

| Tool | Language | Purpose |
|------|----------|---------|
| **[sqlmap](https://github.com/sqlmapproject/sqlmap)** | Python | Automated SQL injection & DB takeover |
| **[ffuf](https://github.com/ffuf/ffuf)** | Go | High-speed web fuzzing & content discovery |
| **[ParamSpider](https://github.com/devanshbatham/ParamSpider)** | Python | Wayback Archive URL miner with parameter extraction |
| **Custom Fuzzer** | Go | Lightweight directory fuzzer for Termux |
| **Wordlists** | — | 444k+ entries for dirs, vhosts, params, CVEs, fuzzing |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.x + pip
python3 --version
pip3 --version

# Go (for fuzzers)
go version
```

### Installation

```bash
# Clone
git clone https://github.com/zyraaatod/NeoTurst.git
cd NeoTurst

# Python dependencies
pip install requests colorama beautifulsoup4 urllib3

# Build custom fuzzer (optional)
cd fuzzer && go build -o fuzz . && mv fuzz ../ && cd ..

# ParamSpider (optional — for URL parameter mining)
cd paramspider && pip install . && cd ..
```

### Usage

```bash
# Launch NightFury engine
python3 nightfury.py

# Or run tools directly
python3 sqlmap/sqlmap.py -u "http://target.com/page?id=1"
./ffuf/ffuf -u "http://target.com/FUZZ" -w wordlist.txt
./fuzz "http://target.com/FUZZ" wordlist.txt 50 404

# ParamSpider — mine parameterized URLs from Wayback Archive
python3 paramspider/paramspider/main.py -d target.com -p FUZZ
```

The engine will guide you through:
1. **Enter target URL** (e.g., `http://example.com`)
2. **Automated crawl** — discovers endpoints, forms, parameters
3. **Multi-phase scan** — 18 module test pipeline
4. **Report** — saved to `report_{domain}.txt`

---

## 📁 Project Structure

```
NeoTurst/
├── nightfury.py          # Main scanner engine (2,132 lines)
├── wordlist.txt          # 444k-line directory wordlist
├── sqlmap/               # SQL injection automation tool (full copy)
├── ffuf/                 # Web fuzzer (Go source + binary)
├── fuzzer/               # Custom directory fuzzer for Termux (Go)
├── paramspider/          # Wayback Archive URL miner (Python)
├── wordlists/            # 60+ wordlist files across 7 categories
│   ├── SecListsCurated/  # Curated content discovery lists
│   ├── fuzz/             # SQLi, XSS, LFI, XXE, CMDi payloads
│   ├── technology/       # Tech-specific discovery (PHP, ASP, etc.)
│   ├── dns/              # Subdomain enumeration (amass, dnsgen)
│   ├── files/            # File discovery wordlists
│   └── dir/              # Directory brute-force lists
├── params.txt            # 27k URL parameter names
├── all_files.txt         # 408k file/directory paths
├── cvePaths.txt          # 7.5k known CVE exploit paths
└── vhost*.txt            # Virtual host brute-force wordlists
```

---

## 🛠️ Advanced Usage

### NightFury Scan Pipeline

```
Input URL → Connection Test → Web Crawl (50 pages max)
  → WAF Detection → Tech Fingerprinting → Port Scan
  → Module 1-18 Parallel Scan → Report Generation
```

### Payload Generation

The engine dynamically generates **200+ unique payloads per category** (SQLi, XSS, LFI, CMDi, SSRF, XXE, SSTI) using combinatorial techniques. All requests are sent **concurrently (20 threads)** for maximum speed.

### ParamSpider — URL Parameter Mining

Extract parameterized URLs from Wayback Machine archives for deeper scanning:

```bash
# Basic usage
python3 paramspider/paramspider/main.py -d target.com

# Custom placeholder (feed results into ffuf or NightFury)
python3 paramspider/paramspider/main.py -d target.com -p FUZZ

# From domain list
python3 paramspider/paramspider/main.py -l domains.txt

# Output to stream
python3 paramspider/paramspider/main.py -d target.com -s -p FUZZ

# Using proxy (e.g., Burp Suite)
python3 paramspider/paramspider/main.py -d target.com --proxy http://127.0.0.1:8080
```

---

## 📸 Sample Output

```
╔══════════════════════════════════════════════╗
║       NIGHTFURY MAXIMUM DESTRUCTION v5.0      ║
║         INDUSTRIAL GRADE - ZERO ERROR         ║
╚══════════════════════════════════════════════╝

[+] Target: http://example.com
[+] Connection: OK
[+] Crawl: 23 endpoints | 4 forms | 12 parameters
[+] WAF: Cloudflare detected
[+] Tech: PHP 7.4 | nginx 1.18 | WordPress 5.8
[+] Scan: 18/18 modules complete
[+] Report saved to: report_example.com.txt
```

---

## 📄 Report Format

Reports are saved as plain text with:
- Target information & timestamps
- Discovered endpoints & forms
- Vulnerability findings by severity
- Payloads used & evidence
- Remediation recommendations

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the project
2. Create your feature branch (`git checkout -b feat/amazing`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push (`git push origin feat/amazing`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  <sub>Built for the security community · Ethical hacking only</sub><br>
  <sub>NeoTurst — Maximum Destruction, Zero Regret</sub>
</p>
