<p align="center">
  <img src="https://raw.githubusercontent.com/cossackrider8-glitch/AI-RedTeam-Orchestrator/main/file%20(1).webp" alt="Rinnegan Banner" width="800"/>
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
| **💻 Bug Bounty Hunters** | Quickly enumerate targets and get AI-prioritized attack vectors. |

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

Open your terminal and run these **exact commands** one by one:

```bash
git clone https://github.com/cossackrider8-glitch/AI-RedTeam-Orchestrator.git
cd AI-RedTeam-Orchestrator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
(Wait for all packages to install. This may take 1-2 minutes).

🔑 Configuration (Set Up Your AI Provider)
This tool works with 5 different AI providers. You only need to pick ONE.

Step 1: Open the config file
bash
nano config.py
Step 2: Choose your provider
Find this line at the top:

python
PROVIDER = "groq"   # <--- CHANGE THIS to switch models
Here are your options:

Provider	Cost	Best For	Model Used
groq	100% FREE	Fastest AI (LPU hardware), no credit card.	Llama 3 70B
ollama	100% FREE	Air-gapped/offline testing.	Llama 3 (Local)
openrouter	Free rate-limited	Mix of free & premium models.	Llama 3 (Free)
openai	Paid (~$0.01/scan)	Enterprise-grade GPT-4.	GPT-4o-mini
deepseek	Very Cheap	Alternative to OpenAI.	DeepSeek Chat
Step 3: Paste your API Key
Scroll down to the section for your chosen provider and paste your key.

For Groq (100% FREE - RECOMMENDED):

Go to https://console.groq.com/keys

Sign up with Google/Email (30 seconds, no credit card).

Click "Create API Key".

Name it redteam-agent.

Copy the key (starts with gsk_...).

Paste it in config.py:

python
GROQ_API_KEY = "gsk_YOUR_KEY_HERE"
For OpenAI (Premium):

Go to https://platform.openai.com/api-keys

Add $5 to your account (one-time).

Create a key and paste it:

python
OPENAI_API_KEY = "sk-YOUR_KEY_HERE"
For Ollama (100% FREE - Local):

Install Ollama: https://ollama.com

Run ollama pull llama3 in terminal.

No API key needed. Just set PROVIDER = "ollama".

Step 4: Set your Target IP
Find this line in config.py:

python
TARGET_IP = "192.168.152.129"   # CHANGE THIS
Change it to your target machine's IP (e.g., 192.168.1.10 for your Windows VM, or your Kali IP for self-scan).

Step 5: Save the file
Press CTRL + X, then Y, then Enter.

🚀 Usage (How to Run the Tool)
Step 1: Make sure you are in the virtual environment
bash
cd ~/Desktop/AI-RedTeam-Orchestrator
source venv/bin/activate
Step 2: Run the tool
bash
python3 orchestrator.py
What happens next:
The Violet Rinnegan banner prints.

Nmap scans your target IP for open ports.

The AI (Groq/OpenAI/etc.) analyzes the results.

A full engagement report with MITRE ATT&CK mapping prints on your screen.

Example Output:
text
📡 RECONNAISSANCE RESULTS:
{
  "host": "192.168.1.10",
  "state": "up",
  "protocols": { "tcp": { "445": { "service": "microsoft-ds" } } }
}

🧠 AI-GENERATED ATTACK PLAN:
1. Open port 445 (SMB) detected. (T1046 - Network Service Scanning)
2. Potential vulnerability: EternalBlue or SMB Relay. (T1210 - Exploitation of Remote Services)
3. Recommended exploit: smbclient or Metasploit auxiliary/scanner/smb/smb_ms17_010.
🔄 How to Switch AI Providers (Change Models)
You can switch between providers anytime without reinstalling anything.

Step 1: Open config.py:

bash
nano config.py
Step 2: Change the PROVIDER line to your desired model:

python
PROVIDER = "groq"       # FREE - Fastest (Llama 3)
PROVIDER = "ollama"     # FREE - Local (Llama 3)
PROVIDER = "openai"     # PAID - GPT-4
PROVIDER = "openrouter" # FREE+PAID
PROVIDER = "deepseek"   # CHEAP
Step 3: Update the API key for the new provider:

If switching to groq, fill GROQ_API_KEY.

If switching to openai, fill OPENAI_API_KEY.

If switching to ollama, no key needed.

Step 4: Save and run:

bash
python3 orchestrator.py
❓ TROUBLESHOOTING (If It Doesn't Work)
Problem	Solution
ModuleNotFoundError: No module named 'langchain_groq'	Run pip install langchain-groq inside your venv.
Groq says "Rate limit exceeded"	Groq free tier has limits. Wait 1 minute or switch to Ollama.
Ollama says "Connection refused"	Make sure Ollama is installed and running: ollama serve
Nmap scan takes too long	Change SCAN_PORTS in config.py to fewer ports (e.g., "22,80,443").
API Key invalid error	Double-check you copied the exact key (no extra spaces).
Permission Denied on Kali	Run chmod +x orchestrator.py and try again.
Virtual environment not activating	Run source venv/bin/activate (not venv\Scripts\activate).
Target IP not responding	Make sure the target machine is turned on and on the same network.
🗺️ MITRE ATT&CK Mapping (Industry Standard)
Tactic	Technique ID	Technique Name
Reconnaissance	T1595	Active Scanning
Execution	T1059	Command and Scripting Interpreter
Defense Evasion	T1027	Obfuscated Files or Information
Lateral Movement	T1210	Exploitation of Remote Services
📂 Repository Structure
text
AI-RedTeam-Orchestrator/
├── orchestrator.py         # Main AI engine (Rinnegan Banner + Universal LLM)
├── config.py               # Universal config (Provider + API Keys + Target)
├── requirements.txt        # Python dependencies
├── file (1).webp           # Violet Banner Image
├── .gitignore              # Prevents cache files
└── README.md               # This complete manual
⚠️ Final Warning
This tool is for authorized security testing and educational purposes only.
Unauthorized access to computer systems is illegal. The creator assumes zero liability for misuse. By using this tool, you agree to use it ethically and legally.

🤝 Contributing
Found a bug or want to add a new provider (e.g., Anthropic, Gemini)?
Open an issue or submit a Pull Request.

📜 License
MIT License - Free to use, modify, and distribute. See LICENSE for details.

Star ⭐ this repo if you found it useful! It helps other cybersecurity professionals find it. 🚀
MIT License - Free to use, modify, and distribute. See LICENSE for details.

Star ⭐ this repo if you found it useful! It helps other cybersecurity professionals find it. 🚀
