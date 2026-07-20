#!/usr/bin/env python3
# orchestrator.py - RINNEGAN Universal AI Engine

import sys
import json
import nmap
from config import *

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None
try:
    from langchain_ollama import ChatOllama
except ImportError:
    ChatOllama = None
from langchain_core.messages import HumanMessage, SystemMessage

def print_banner():
    banner = """
\033[95m
    ██████╗ ██╗███╗   ██╗███╗   ██╗███████╗ ██████╗  █████╗ ███╗   ██╗
    ██╔══██╗██║████╗  ██║████╗  ██║██╔════╝██╔════╝ ██╔══██╗████╗  ██║
    ██████╔╝██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║  ███╗███████║██╔██╗ ██║
    ██╔══██╗██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██║██║╚██╗██║
    ██║  ██║██║██║ ╚████║██║ ╚████║███████╗╚██████╔╝██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
\033[96m
        [ AI RED TEAM ORCHESTRATOR v2.0 - UNIVERSAL ]
\033[95m
        >> Autonomous Hacking Agent - For Authorized Testing Only <<
\033[93m
        Crafted by: Obito Uchiha [ h4ck3r ] 
        🧠 Current Provider: """ + PROVIDER.upper() + """
\033[0m
    """
    print(banner)

def get_llm():
    if PROVIDER == "groq":
        return ChatGroq(groq_api_key=GROQ_API_KEY, model="llama3-70b-8192", temperature=0.3)
    elif PROVIDER == "openai":
        return ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0.3)
    elif PROVIDER == "openrouter":
        return ChatOpenAI(openai_api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1", model="meta-llama/llama-3-70b-instruct:free", temperature=0.3)
    elif PROVIDER == "ollama":
        return ChatOllama(base_url=OLLAMA_BASE_URL, model="llama3", temperature=0.3)
    elif PROVIDER == "deepseek":
        return ChatOpenAI(openai_api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1", model="deepseek-chat", temperature=0.3)
    else:
        raise ValueError("Invalid PROVIDER")

def scan_target(ip, ports):
    print(f"\n[+] Starting reconnaissance scan on {ip}...")
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=ip, ports=ports, arguments='-sV -sC')
        if ip not in nm.all_hosts():
            print(f"[!] Host {ip} is down.")
            return None
        scan_data = {"host": ip, "state": nm[ip].state(), "protocols": {}}
        for proto in nm[ip].all_protocols():
            scan_data["protocols"][proto] = {}
            for port in nm[ip][proto].keys():
                s = nm[ip][proto][port]
                scan_data["protocols"][proto][port] = {"state": s.get('state'), "service": s.get('name')}
        return scan_data
    except Exception as e:
        print(f"[!] Nmap failed: {e}")
        return None

def analyze_with_ai(llm, scan_results):
    print("\n[+] Contacting AI Brain...")
    system = SystemMessage(content="You are a Senior Red Team Operator. Map findings to MITRE ATT&CK (T-codes). Suggest an attack path.")
    human = HumanMessage(content=f"Target: {scan_results['host']}\nData: {json.dumps(scan_results, indent=2)}")
    try:
        return llm.invoke([system, human]).content
    except Exception as e:
        return f"[!] AI Error: {e}"

def main():
    print_banner()
    if "YOUR_GROQ_KEY" in GROQ_API_KEY and PROVIDER == "groq":
        print("\033[91m[!] ERROR: Set GROQ_API_KEY in config.py!\033[0m")
        sys.exit(1)
    
    print(f"[+] Target: {TARGET_IP}")
    scan_data = scan_target(TARGET_IP, SCAN_PORTS)
    if not scan_data:
        sys.exit(1)
    
    print("\n" + "="*60)
    print("📡 SCAN RESULTS:")
    print("="*60)
    print(json.dumps(scan_data, indent=2))
    
    llm = get_llm()
    report = analyze_with_ai(llm, scan_data)
    
    print("\n" + "="*60)
    print("🧠 AI ATTACK PLAN (MITRE MAPPING):")
    print("="*60)
    print(report)
    print("="*60)
    print("\n[!] RINNEGAN Universal Engine finished.")

if __name__ == "__main__":
    main()
