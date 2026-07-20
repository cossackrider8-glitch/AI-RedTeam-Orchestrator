# config.py - Universal LLM Engine for RINNEGAN AI

# ==================================================
# 1. CHOOSE YOUR PROVIDER (Change this one line)
# ==================================================
PROVIDER = "groq"   # Options: groq, openai, openrouter, ollama, deepseek

# ==================================================
# 2. API KEYS (Only fill in the one you are using)
# ==================================================

# --- GROQ (100% FREE) ---
GROQ_API_KEY = "gsk_...YOUR_GROQ_KEY_HERE..."

# --- OPENAI (PREMIUM) ---
OPENAI_API_KEY = "sk-...YOUR_OPENAI_KEY_HERE..."

# --- OPENROUTER (FREE + PREMIUM MIX) ---
OPENROUTER_API_KEY = "sk-or-...YOUR_OPENROUTER_KEY_HERE..."

# --- OLLAMA (100% FREE - LOCAL) ---
OLLAMA_BASE_URL = "http://localhost:11434"

# --- DEEPSEEK (VERY CHEAP) ---
DEEPSEEK_API_KEY = "sk-...YOUR_DEEPSEEK_KEY_HERE..."

# ==================================================
# 3. TARGET SETTINGS
# ==================================================
TARGET_IP = "192.168.152.129"
SCAN_PORTS = "22,80,443,445,3389,8080"
