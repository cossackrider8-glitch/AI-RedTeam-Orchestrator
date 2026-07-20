<p align="center">
  <img src="rinnegan-banner.webp" alt="Rinnegan Banner" width="800"/>
</p>

# 🟣 AI-RedTeam-Orchestrator
### *Autonomous AI Hacking Agent with Universal LLM Support (Free + Premium)*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI](https://img.shields.io/badge/AI-Groq%20%7C%20OpenAI%20%7C%20Ollama-blueviolet)](https://groq.com/)

---

## 👥 Who Can Use This Tool?

| Role | How They Use It |
| :--- | :--- |
| **🔴 Red Team Operators** | Automate multi-host attack planning and execution with AI-generated MITRE mapping. |
| **🟣 Purple Teamers** | Test detection coverage against AI-simulated adversary TTPs. |
| **🛡️ SOC Analysts** | Understand how AI can automate attacker decision-making. |
| **🎓 Security Students** | Learn AI integration in offensive security with free (Groq/Ollama) models. |

> **⚠️ DISCLAIMER:** This tool is for **educational purposes and AUTHORIZED security testing ONLY**. The author is not responsible for any misuse. Use only on systems you own or have explicit written permission to test.

---

## 🎯 Features

- ✅ **Universal LLM Engine**: Supports 5 providers—**Groq (FREE)**, **Ollama (FREE/Local)**, **OpenRouter (Free+Paid)**, **OpenAI (Premium)**, and **DeepSeek (Low-cost)**.
- ✅ **AI-Driven Attack Planning**: Uses state-of-the-art LLMs (Llama 3, GPT-4, Mistral) to map vulnerabilities to MITRE ATT&CK.
- ✅ **Automated Reconnaissance**: Scans target IPs and identifies open ports/services with Nmap.
- ✅ **MITRE ATT&CK Mapping**: Every action is mapped to industry-standard T-codes (T1595, T1059, T1027).
- ✅ **Rinnegan Branding**: Professional violet banner on every run—HR approved.
- ✅ **Zero Billing Surprises**: Switch to Groq/Ollama for **100% free** AI analysis.

---

## 📦 Installation (On Kali / Attacker Machine)

Open your terminal and run these **exact commands**:

```bash
git clone https://github.com/cossackrider8-glitch/AI-RedTeam-Orchestrator.git
cd AI-RedTeam-Orchestrator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🔑 Configuration (Set Up Your AI Provider)
Step 1: Open the config file
bash
nano config.py
Step 2: Choose your provider
Find this line:

python
PROVIDER = "groq"   # <--- CHANGE THIS to switch models
Provider	Cost	Best For
groq	100% FREE	Fastest AI, no credit card.
ollama	100% FREE	Air-gapped/offline testing.
openrouter	Free rate-limited	Mix of free & premium models.
openai	Paid	Enterprise-grade GPT-4.
Step 3: Paste your API Key
For Groq (FREE): Get a key at https://console.groq.com/keys

For OpenAI (Paid): Get a key at https://platform.openai.com/api-keys

For Ollama (FREE): Install locally, run ollama pull llama3.

Paste it in config.py:

python
GROQ_API_KEY = "gsk_YOUR_KEY_HERE"
Step 4: Set your Target IP
python
TARGET_IP = "192.168.152.129"   # CHANGE THIS
Save the file: CTRL + X, then Y, then Enter.

🚀 Usage (How to Run)
bash
python3 orchestrator.py
Example Output:
text
📡 RECONNAISSANCE RESULTS:
{ "host": "192.168.1.10", "state": "up" }

🧠 AI-GENERATED ATTACK PLAN:
1. Open port 445 (SMB) detected. (T1046 - Network Service Scanning)
2. Recommended exploit: smbclient.
🔄 How to Switch AI Providers
Open config.py and change:

python
PROVIDER = "groq"      # FREE - Fastest
PROVIDER = "ollama"    # FREE - Local
PROVIDER = "openai"    # PAID - GPT-4
Update the API key for the new provider, save, and run python3 orchestrator.py again.

❓ TROUBLESHOOTING
Problem	Solution
ModuleNotFoundError	Run pip install langchain-groq
Groq rate limit	Wait 1 minute or switch to Ollama.
Ollama connection refused	Run ollama serve in another terminal.
API Key invalid	Double-check no extra spaces.
🗺️ MITRE ATT&CK Mapping
Tactic	Technique ID	Technique Name
Reconnaissance	T1595	Active Scanning
Execution	T1059	Command and Scripting Interpreter
Defense Evasion	T1027	Obfuscated Files or Information
📂 Repository Structure
text
AI-RedTeam-Orchestrator/
├── orchestrator.py         # Main AI engine
├── config.py               # Universal config
├── requirements.txt        # Dependencies
├── rinnegan-banner.webp    # Banner Image
└── README.md               # This manual
⚠️ Final Warning
This tool is for authorized security testing and educational purposes only.
Unauthorized access is illegal. The creator assumes zero liability for misuse.

📜 License
MIT License - Free to use, modify, and distribute.

Star ⭐ this repo if you found it useful! 🚀

MIT License - Free to use, modify, and distribute.

Star ⭐ this repo if you found it useful! 🚀
