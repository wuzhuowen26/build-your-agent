import openai
import asyncio
import os
from pathlib import Path
from typing import Any, Dict
import nest_asyncio
from dotenv import load_dotenv
from dp.agent.adapter.adk import CalculationMCPToolset
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams
from google.genai import types


# Set environment variables if needed

#Use deepseek
os.environ['DEEPSEEK_API_KEY'] = "sk-d3c4dc3f27b041feab840268a233736d"

#Use gpt-4o
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = ""


# Configure SSE params
sse_params = SseServerParams(
    url="http://47.92.7.195:50001/sse",  
)

toolset = MCPToolset(
    connection_params=SseServerParams(
        url="http://47.92.7.195:50001/sse",
    ),
)


use_model = "deepseek"

if use_model == "deepseek":
    model = LiteLlm(model="deepseek/deepseek-chat")
if use_model == "gpt-4o":
    model = LiteLlm(model="azure/gpt-4o")

# Create agent
root_agent = Agent(
    name="mcp_sse_agent",
    model=model,
    instruction="You are an intelligent assistant capable of using external tools via MCP.",
    tools=[]
)
