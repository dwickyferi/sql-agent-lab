from agno.agent import Agent
from agno.memory.agent import AgentMemory
from agno.memory.db.postgres import PgMemoryDb
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.postgres import PostgresStorage
from dotenv import load_dotenv
from agent.main import agent_sql
load_dotenv()

db_url = "postgresql+psycopg2://ai:ai@localhost:5432/ai"

basic_agent = Agent(
    name="Basic Agent",
    model=OpenAIChat(id="gpt-4.1"), # Ensure OPENAI_API_KEY is set
    memory=AgentMemory(
        db=PgMemoryDb(
            table_name="agent_memory",
            db_url=db_url,
        ),
        create_user_memories=True,
        update_user_memories_after_run=True,
        create_session_summary=True,
        update_session_summary_after_run=True,
    ),
    storage=PostgresStorage(
        table_name="agent_sessions", db_url=db_url, auto_upgrade_schema=True
    ),
    add_history_to_messages=True,
    num_history_responses=3,
    add_datetime_to_instructions=True,
    markdown=True,
)

app = Playground(
    agents=[
        basic_agent,
        agent_sql
    ]
).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", port=7777, reload=True)