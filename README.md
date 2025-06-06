# SQL Agent Lab - Natural Language to SQL Using Agno

A powerful SQL Agent built with Agno that transforms natural language queries into SQL. This agent enables users to interact with their databases using plain English, making data exploration and analysis more accessible and intuitive.

## Features

- 🤖 Natural Language to SQL Conversion: Ask questions about your data in plain English
- 🧠 Intelligent Query Construction: Optimized SQL queries based on context and requirements
- 💭 Reasoning Process: Clear explanation of how queries are constructed
- 🔄 Memory Enabled: Maintains context across conversations
- 📊 Database Schema Understanding: Automatically understands and navigates database relationships
- ⚡ Real-time Processing: Quick response times for interactive data exploration

## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- OpenAI API Key

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sql-agent-lab.git
cd sql-agent-lab
```

2. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI API key.

3. Start the PostgreSQL database:
```bash
docker-compose up -d
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the agent:
```bash
python api/agent/main.py
```

## Usage Examples

Here are some examples of how to interact with the SQL Agent:

1. Simple Query:
```
User: "Show me all users who joined last month"
Agent: *Transforms this into appropriate SQL query*
```

2. Complex Analysis:
```
User: "What's the average order value by category, but only for categories with more than 100 orders?"
Agent: *Creates complex SQL with aggregations and conditions*
```

3. Trend Analysis:
```
User: "Show me the sales trend over the last 6 months"
Agent: *Generates time-series analysis query*
```

## Architecture

The SQL Agent is built using:
- **Agno**: Core framework for building the AI agent
- **OpenAI GPT-4**: For natural language understanding and SQL generation
- **PostgreSQL**: Database backend with pgvector for vector storage
- **SQLTools**: For database interaction and query execution

## Features in Detail

### Natural Language Processing
- Understands context and intent
- Handles complex, multi-part questions
- Maintains conversation history

### SQL Generation
- Generates optimized SQL queries
- Handles complex joins and subqueries
- Considers performance implications

### Memory System
- Maintains context across conversations
- Remembers user preferences
- Stores previous query patterns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for your own purposes.

## Acknowledgments

- Built with [Agno Framework](https://github.com/agnohq/agno)
- Powered by OpenAI's GPT models
