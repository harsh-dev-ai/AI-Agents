# 🌐 Web Scraping Agent (Google ADK)

An AI-powered web scraping and summarization agent built with the [Google AI Development Kit (ADK)](https://ai.google.dev/).  
This project enables you to **scrape web pages, list links, and perform web searches** interactively from the command line.

---

## ✨ Features

- **Scrape Web Pages**: Extract and clean text content from any URL.  
- **List Links**: Collect outbound links (absolute URLs) from a page.  
- **DuckDuckGo Search**: Search the web and return top results with links.  
- **Summarization Ready**: Cleaned and truncated text for LLM-friendly input.  
- **Interactive CLI**: Run in your terminal, exit with `exit` or `quit`.  

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)  
- [Google ADK](https://ai.google.dev/) – AI agent development framework  
- [LiteLLM](https://github.com/BerriAI/litellm) – Connects OpenAI/Gemini models via ADK  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- [Requests](https://docs.python-requests.org/) – Web requests  
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) – Web search API  

---

## 📂 Project Structure

```
.
├── run_scraper.py             # CLI entry point
├── adk_web_scraper/           # Package
│   ├── agent.py               # Defines the ADK LlmAgent and tools
│   └── __init__.py            # Package initializer
└── README.md                  # Project documentation
```

- **run_scraper.py** – Launches an interactive loop using `InMemoryRunner` to query the agent.  
- **adk_web_scraper/agent.py** – Defines tools (`web_search`, `list_links`, `scrape_page`) and the `web_scraper_agent`.  
- **adk_web_scraper/__init__.py** – Makes the folder importable as a Python package.  

---

## ⚙️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/adk-web-scraper.git
   cd adk-web-scraper
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Minimal requirements:
   ```
   google-adk
   litellm
   requests
   beautifulsoup4
   duckduckgo-search
   ```

---

## 🚀 Usage

Run the interactive CLI:

```bash
python run_scraper.py
```

Example session:

```
🌐 ADK WebScraper ready! (type 'exit' to quit)

You: scrape https://example.com
Agent:
 Example Domain
 This domain is for use in illustrative examples in documents...
 [Source] https://example.com

You: list_links https://example.com
Agent:
 https://www.iana.org/domains/example

You: web_search crewAI framework
Agent:
 CrewAI Documentation: https://docs.crewai.com
 GitHub - CrewAI repo: https://github.com/joaomdmoura/crewAI
 ...
```

Exit with:
```
You: exit
```

---

## ⚡ Configuration

- **LLM**: Defaults to OpenAI `gpt-4o-mini` via LiteLLM, configurable in `agent.py`.  
- Swap model by editing:
  ```python
  model=LiteLlm(model="gemini-2.0-flash")
  ```
- **Tools**:
  - `web_search(query)` → search DuckDuckGo.  
  - `list_links(url, limit=20)` → collect outbound links.  
  - `scrape_page(url, selector="", max_chars=6000)` → scrape and clean text.  

---

## 🔒 Notes & Limitations

- No JavaScript rendering (static HTML only).  
- DuckDuckGo search results limited to 5 by default.  
- Large pages truncated at ~6000 characters.  
- Error handling is basic; invalid selectors or bad URLs return error strings.  

---

## 📜 License

MIT License © 2025
