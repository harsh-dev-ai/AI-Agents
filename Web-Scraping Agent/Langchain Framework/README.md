# 🌐 Web Scraping Agent (LangChain)

An AI-powered web scraping and summarization agent built with the [LangChain](https://python.langchain.com/) framework.  
This project enables you to **scrape web pages, list links, and perform web searches** interactively from the command line.

---

## ✨ Features

- **Scrape Web Pages**: Extract and clean readable text content from any URL.  
- **List Links**: Collect outbound links (absolute URLs) from a page.  
- **DuckDuckGo Search**: Search the web and return top results with links.  
- **Summarization Ready**: Extracted content is cleaned and truncated for LLM-friendly input.  
- **Interactive CLI**: Run directly in your terminal, exit with `exit` or `quit`.  

---

## 🛠️ Tech Stack

- [Python 3.9+](https://www.python.org/)  
- [LangChain](https://python.langchain.com/) – Agent orchestration  
- [OpenAI GPT (via `langchain_openai`)](https://python.langchain.com/docs/integrations/llms/openai)  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing  
- [Requests](https://docs.python-requests.org/) – Web requests  
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) – Web search API  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Load API keys from `.env`  

---

## 📂 Project Structure

```
.
├── web-scraping_agent.py      # Main LangChain web scraper agent
└── README.md                  # Project documentation
```

- **web-scraping_agent.py** – Defines scraping helpers, tools (`scrape`, `list_links`, `search`), and runs an interactive LangChain agent.  

---

## ⚙️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/langchain-web-scraper.git
   cd langchain-web-scraper
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
   langchain
   langchain-openai
   langchain-community
   requests
   beautifulsoup4
   duckduckgo-search
   python-dotenv
   ```

4. **Set your OpenAI API key** in a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

## 🚀 Usage

Run the interactive CLI:

```bash
python web-scraping_agent.py
```

Example session:

```
🌐 WebScraper Agent ready! (type 'exit' to quit)

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

- **LLM**: Defaults to `gpt-4o-mini` via LangChain’s `ChatOpenAI`.  
- **Tools**:
  - `ScrapePage` → fetch and clean text from a URL.  
  - `ListLinks` → collect outbound links from a page.  
  - `WebSearch` → query DuckDuckGo for candidate URLs.  

---

## 🔒 Notes & Limitations

- No JavaScript rendering (static HTML only).  
- DuckDuckGo search results limited to top 5 by default.  
- Large pages are truncated at ~6000 characters.  
- Error handling is basic; invalid selectors or bad URLs return error strings.  

---

## 📜 License

MIT License © 2025
