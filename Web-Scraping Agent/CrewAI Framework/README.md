# 🌐 Web Scraping Agent (CrewAI)

An AI-powered web scraping and summarization agent built with the [CrewAI](https://docs.crewai.com) framework.  
This project allows you to **scrape web pages, list links, and perform web searches** interactively from the command line.

---

## ✨ Features

- **Scrape Web Pages**: Extract and clean readable text content from any URL.  
- **List Links**: Collect outbound links (absolute URLs) from a page.  
- **DuckDuckGo Search**: Perform quick web searches and return top results.  
- **Summarization Ready**: Extracted content is cleaned and truncated for LLM-friendly input.  
- **Interactive CLI**: Query the agent in real time and exit with `exit` or `quit`.  

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)  
- [CrewAI](https://docs.crewai.com) – Multi-agent framework  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- [Requests](https://docs.python-requests.org/) – Web requests  
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) – Web search API  
- [PyYAML](https://pyyaml.org/) – Agent/task configuration  

---

## 📂 Project Structure

```
.
├── crew.py              # CrewBase definition (agents + tasks)
├── run_scraper.py       # CLI entry point
├── tools.py             # Custom scraping/search tools
├── config/              # Configuration files
│   ├── agents.yaml      # Agent configurations
│   └── tasks.yaml       # Task configurations
└── README.md            # Project documentation
```

- **crew.py** – Defines the `WebScraperCrew` class with an agent and a scraping task.  
- **run_scraper.py** – Runs the crew interactively in the terminal.  
- **tools.py** – Implements `ScrapePageTool`, `ListLinksTool`, and `WebSearchTool`.  
- **config/agents.yaml** – YAML file defining the agent’s role and behavior.  
- **config/tasks.yaml** – YAML file defining scraping/summarization tasks.  

---

## ⚙️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/web-scraper-crewai.git
   cd web-scraper-crewai
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
   crewai
   requests
   beautifulsoup4
   duckduckgo-search
   pyyaml
   ```

---

## 🚀 Usage

Run the interactive CLI:

```bash
python run_scraper.py
```

Example session:

```
🌐 WebScraperCrew ready! (type 'exit' to quit)

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

- **Agents** are defined in `config/agents.yaml`.  
- **Tasks** are defined in `config/tasks.yaml`.  

You can customize prompts, instructions, and behavior here without changing the Python code.

---

## 🔒 Notes & Limitations

- Does not support JavaScript rendering (no dynamic DOM scraping).  
- DuckDuckGo results are limited to the top 5 by default.  
- Large pages are truncated at ~6000 characters for efficiency.  
- Error handling is basic; invalid selectors or unavailable URLs return error strings.  

---

## 📜 License

MIT License © 2025
