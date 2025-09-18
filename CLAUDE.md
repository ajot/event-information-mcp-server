# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development & Testing
```bash
# Run the local MCP server with FastMCP dev tools (requires agent credentials)
GRADIENT_AGENT_ACCESS_KEY=your-key GRADIENT_AGENT_ENDPOINT=https://your-agent.agents.do-ai.run fastmcp dev local-event-agent.py

# Run the remote-deployable version locally (requires PORT env variable and agent credentials)
PORT=8080 GRADIENT_AGENT_ACCESS_KEY=your-key GRADIENT_AGENT_ENDPOINT=https://your-agent.agents.do-ai.run python event-agent.py

# Install dependencies
pip install -r requirements.txt

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# For local testing, you can also create a .env file with:
# GRADIENT_AGENT_ACCESS_KEY=your-access-key
# GRADIENT_AGENT_ENDPOINT=https://your-agent.agents.do-ai.run
```

## Architecture Overview

### MCP Server Implementation
This is a Model Context Protocol (MCP) server built with FastMCP framework that provides event and meetup information using DigitalOcean's Gradient AI platform. The codebase consists of two main entry points:

1. **local-event-agent.py** - For local development and testing with MCP-compatible applications (Claude Desktop, Cursor, Windsurf)
2. **event-agent.py** - For remote deployment with HTTP transport (includes port configuration for DigitalOcean App Platform)

### Core Components

**EventAgent Class** - The main service class that provides AI-powered event information using DigitalOcean's Gradient AI platform:
- Uses trained agent with specialized event knowledge
- Provides comprehensive event, speaker, and schedule information
- Supports natural language queries for event discovery
- Configurable via environment variables: `GRADIENT_AGENT_ACCESS_KEY` and `GRADIENT_AGENT_ENDPOINT`

**MCP Tools**:
- `get_event_info(event_name: str)` - Get comprehensive information about a specific event
- `get_speaker_details(speaker_name: str)` - Get detailed speaker information
- `search_events(query: str, location: Optional[str])` - Search for events by keywords and location
- `get_event_schedule(event_name: str)` - Get event schedule and agenda
- `ask_event_question(question: str, event_context: Optional[str])` - Ask general event questions
- `event_info_resource` - Exposes event info as an MCP resource at `event://info/{event_name}`

### Deployment Configuration

The application is configured for DigitalOcean App Platform deployment:
- Uses port 8080 (configurable via PORT environment variable)
- Deployment specs in `.do/deploy.template.yaml` and `one-click-deploy-final-spec.yaml`
- Health check endpoint at `/mcp`
- Requires gunicorn for production deployment

### Key Dependencies
- **fastmcp** - MCP server framework
- **gradient** - DigitalOcean Gradient AI SDK for agent integration
- **gunicorn** - Production WSGI server
- **uvicorn** - ASGI server (for async support)
- **pytz** - Timezone handling for event information

### Transport Modes
- Local version uses default FastMCP transport (stdio)
- Remote version uses `streamable-http` transport on `0.0.0.0:8080`