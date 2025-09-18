#!/usr/bin/env python3
"""
MCP Server for event and meetup information using FastMCP 2.0 and DigitalOcean Gradient AI
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict, List, Optional
from gradient import Gradient
from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("event-agent")

# Create the FastMCP server
mcp = FastMCP(
    name="Event Information Agent",
    instructions="When you are asked about events, meetups, conferences, speakers, or event schedules, call the appropriate function to get detailed information."
)

class EventAgent:
    """Event and meetup information agent using DigitalOcean Gradient AI"""

    def __init__(self):
        try:
            # Get agent credentials from environment variables
            agent_access_key = os.environ.get("GRADIENT_AGENT_ACCESS_KEY")
            agent_endpoint = os.environ.get("GRADIENT_AGENT_ENDPOINT")

            if not agent_access_key or not agent_endpoint:
                logger.warning(
                    "Missing required environment variables: GRADIENT_AGENT_ACCESS_KEY and GRADIENT_AGENT_ENDPOINT. "
                    "Agent will not be functional until these are set."
                )
                self.client = None
                return

            # Initialize using the correct agent pattern
            self.client = Gradient(
                agent_access_key=agent_access_key,
                agent_endpoint=agent_endpoint
            )
            logger.info("EventAgent initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize EventAgent: {e}")
            self.client = None

    async def query_event_info(self, prompt: str, context: str = None) -> Dict[str, Any]:
        """Query the AI agent for event information"""
        if not self.client:
            return {
                "error": "EventAgent not configured. Please set GRADIENT_AGENT_ACCESS_KEY and GRADIENT_AGENT_ENDPOINT environment variables.",
                "status": "error"
            }

        try:
            messages = []

            # For trained agents, only add custom context if provided
            # The agent already has its training context
            if context:
                messages.append({"role": "system", "content": context})

            messages.append({"role": "user", "content": prompt})

            # Use the correct agent API call pattern - run in executor for async
            loop = asyncio.get_event_loop()
            completion = await loop.run_in_executor(
                None,
                lambda: self.client.agents.chat.completions.create(
                    messages=messages,
                    model="ignored"  # Model parameter is ignored for agents
                )
            )

            response_text = completion.choices[0].message.content

            return {
                "response": response_text,
                "status": "success",
                "model": "trained-agent"
            }

        except Exception as e:
            logger.error(f"Error querying event info: {e}")
            return {
                "error": str(e),
                "status": "error"
            }

    async def search_events(self, query: str, location: str = None) -> Dict[str, Any]:
        """Search for events based on query and optional location"""
        search_prompt = f"Search for events related to: {query}"
        if location:
            search_prompt += f" in {location}"
        search_prompt += ". Provide a list of relevant events with details like name, date, location, and description."

        return await self.query_event_info(search_prompt)

    async def get_speaker_info(self, speaker_name: str) -> Dict[str, Any]:
        """Get information about a specific speaker"""
        prompt = f"Provide detailed information about speaker {speaker_name}, including their background, expertise, notable presentations, and upcoming speaking engagements."
        return await self.query_event_info(prompt)

    async def get_event_schedule(self, event_name: str) -> Dict[str, Any]:
        """Get schedule information for a specific event"""
        prompt = f"Provide the schedule and agenda for the event '{event_name}', including session times, speakers, topics, and any special activities."
        return await self.query_event_info(prompt)

# Initialize event agent
event_agent = EventAgent()

@mcp.tool()
async def get_event_info(event_name: str) -> str:
    """Get comprehensive information about a specific event or meetup"""
    result = await event_agent.query_event_info(
        f"Provide detailed information about the event '{event_name}', including dates, location, speakers, agenda, registration details, and any other relevant information."
    )

    if result["status"] == "error":
        return f"❌ Error: {result['error']}"

    return f"📅 Event Information for: {event_name}\n\n{result['response']}"

@mcp.tool()
async def get_speaker_details(speaker_name: str) -> str:
    """Get detailed information about a specific speaker"""
    result = await event_agent.get_speaker_info(speaker_name)

    if result["status"] == "error":
        return f"❌ Error: {result['error']}"

    return f"🎤 Speaker Information for: {speaker_name}\n\n{result['response']}"

@mcp.tool()
async def search_events(query: str, location: Optional[str] = None) -> str:
    """Search for events based on keywords and optional location"""
    result = await event_agent.search_events(query, location)

    if result["status"] == "error":
        return f"❌ Error: {result['error']}"

    location_text = f" in {location}" if location else ""
    return f"🔍 Search Results for: '{query}'{location_text}\n\n{result['response']}"

@mcp.tool()
async def get_event_schedule(event_name: str) -> str:
    """Get the schedule and agenda for a specific event"""
    result = await event_agent.get_event_schedule(event_name)

    if result["status"] == "error":
        return f"❌ Error: {result['error']}"

    return f"📋 Schedule for: {event_name}\n\n{result['response']}"

@mcp.tool()
async def ask_event_question(question: str, event_context: Optional[str] = None) -> str:
    """Ask a general question about events, with optional context about a specific event"""
    context_prompt = f"Context about event: {event_context}\n\n" if event_context else ""
    prompt = f"{context_prompt}Question: {question}"

    result = await event_agent.query_event_info(prompt)

    if result["status"] == "error":
        return f"❌ Error: {result['error']}"

    return f"❓ Event Q&A\n\n{result['response']}"

@mcp.resource("event://info/{event_name}")
async def event_info_resource(event_name: str) -> str:
    """Get event information as a resource"""
    result = await event_agent.query_event_info(
        f"Provide structured information about the event '{event_name}' in JSON format"
    )

    if result["status"] == "error":
        return json.dumps({"error": result["error"]}, indent=2)

    return result["response"]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port, log_level="debug")