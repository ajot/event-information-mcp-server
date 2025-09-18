# Event Information Agent MCP Server

A Model Context Protocol (MCP) server that provides comprehensive event and meetup information using DigitalOcean's Gradient AI platform. Built with the modern FastMCP framework for easy setup and intelligent event discovery.

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=event-information-mcp&config=eyJ1cmwiOiJodHRwczovL2V2ZW50LWluZm9ybWF0aW9uLW1jcC1zZXJ2ZXIub25kaWdpdGFsb2NlYW4uYXBwL21jcCIsImRlc2NyaXB0aW9uIjoiR2V0IGV2ZW50IGFuZCBtZWV0dXAgaW5mb3JtYXRpb24iLCJjb21tYW5kIjoiIn0=")


![Image](https://github.com/user-attachments/assets/d5e7db9e-346d-436b-9c2f-53f014debe17)

## Deploy this Remote MCP Server to DigitalOcean
[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/ajot/event-information-mcp-server/tree/main)

## Features

- 🤖 **AI-Powered**: Uses DigitalOcean's Gradient AI platform with trained agents
- 📅 **Event Discovery**: Find conferences, meetups, and professional gatherings
- 🎤 **Speaker Information**: Get detailed speaker bios and session details
- 📋 **Schedule Management**: Access event agendas and session timings
- 🔍 **Intelligent Search**: Natural language queries for event information

## Using the Event Information Agent

### Option 1: Use the Remote MCP Server (Easiest)

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=event-information-mcp&config=eyJ1cmwiOiJodHRwczovL2V2ZW50LWluZm9ybWF0aW9uLW1jcC1zZXJ2ZXIub25kaWdpdGFsb2NlYW4uYXBwL21jcCIsImRlc2NyaXB0aW9uIjoiR2V0IGV2ZW50IGFuZCBtZWV0dXAgaW5mb3JtYXRpb24iLCJjb21tYW5kIjoiIn0=")

Add the following configuration to your MCP-compatible application:

```json
{
  "mcpServers": {
    "event-information-mcp": {
      "url": "https://event-information-mcp-server.ondigitalocean.app/mcp",
      "description": "Get event and meetup information",
      "command": ""
    }
  }
}
```

This remote MCP server provides AI-powered event information and is ready to use!

![Image](https://github.com/user-attachments/assets/34b5228e-2bb8-4fb4-9326-248a62f9519a)

### Option 2: With FastMCP Development Tools

```bash
# Make sure your virtual environment is activated
fastmcp dev local-event-agent.py
```
![Image](https://github.com/user-attachments/assets/beb32cf0-499f-40d3-aeda-a255291ca5f3)

### Option 3: Configure Local MCP Server

This MCP server works with Claude Desktop, Cursor, Windsurf, and other MCP-compatible applications.

#### Configuration Locations

- **Claude Desktop**:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

![Image](https://github.com/user-attachments/assets/c855b19a-9498-47c5-88cd-a778d04319a0)
  
- **Cursor**:
  - macOS: `~/Library/Application Support/Cursor/cursor_desktop_config.json`
  - Windows: `%APPDATA%\Cursor\cursor_desktop_config.json`

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=event-agent&config=eyJjb21tYW5kIjoicHl0aG9uIC9wYXRoL3RvL3lvdXIvZXZlbnRfYWdlbnQucHkifQ%3D%3D)


- **Windsurf**:
  - macOS: `~/Library/Application Support/Windsurf/windsurf_desktop_config.json`
  - Windows: `%APPDATA%\Windsurf\windsurf_desktop_config.json`

Add the following configuration to the appropriate file, making sure to point to your virtual environment:

```json
{
  "mcpServers": {
    "event-agent": {
      "command": "/path/to/your/venv/bin/python",
      "args": ["/path/to/your/local-event-agent.py"],
      "env": {
        "GRADIENT_AGENT_ACCESS_KEY": "your-gradient-agent-access-key",
        "GRADIENT_AGENT_ENDPOINT": "https://your-agent.agents.do-ai.run"
      }
    }
  }
}
```

**Important**:
- Replace paths with the actual paths to your virtual environment and event agent directory
- **Required**: Set `GRADIENT_AGENT_ACCESS_KEY` and `GRADIENT_AGENT_ENDPOINT` with your DigitalOcean Gradient agent credentials
- Use `local-event-agent.py` for local development (it has simpler configuration without port/host settings)
- `event-agent.py` is configured for remote deployment with additional parameters

## Installation (For Local Use)

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajot/event-information-mcp-server.git
   cd event-information-mcp-server
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Agent Credentials**
   The server requires DigitalOcean Gradient agent credentials. You can set these in your MCP configuration (see configuration examples above) or create a `.env` file for local testing:
   ```bash
   # Create a .env file (optional, for local testing)
   echo "GRADIENT_AGENT_ACCESS_KEY=your-access-key" >> .env
   echo "GRADIENT_AGENT_ENDPOINT=https://your-agent.agents.do-ai.run" >> .env
   ```

## Deploy to DigitalOcean App Platform

This MCP server can be deployed as a remote MCP server on DigitalOcean App Platform.

### Prerequisites

- A DigitalOcean account
- The [doctl](https://docs.digitalocean.com/reference/doctl/how-to/install/) command-line tool (optional)
- Git repository with your code

### Deployment Steps

1. **Push your code to a Git repository**
   Make sure all your changes are committed and pushed to a GitHub, GitLab, or Bitbucket repository.

2. **Create a new App on DigitalOcean App Platform**
   - Go to the [DigitalOcean App Platform](https://cloud.digitalocean.com/apps) dashboard
   - Click "Create App" and select your Git repository
   - Select the branch you want to deploy
   - Choose "Python" as the environment

3. **Configure the App**
   - Set the source directory to `/`
   - Set the run command to: `python event-agent.py`
   - Set the environment variables:
     - `PORT=8080`
     - `GRADIENT_AGENT_ACCESS_KEY=your-access-key`
     - `GRADIENT_AGENT_ENDPOINT=https://your-agent.agents.do-ai.run`
   - Set HTTP port to 8080

4. **Deploy the App**
   - Click "Deploy to Production"
   - Wait for the build and deployment to complete

5. **Configure as Remote MCP**
   Once deployed, you can use the app URL as a remote MCP server in your MCP-compatible applications:

   ```json
   {
     "mcpServers": {
       "event-agent": {
         "url": "https://your-app-name.ondigitalocean.app/mcp",
         "description": "Get event and meetup information",
         "env": {
           "GRADIENT_AGENT_ACCESS_KEY": "your-gradient-agent-access-key",
           "GRADIENT_AGENT_ENDPOINT": "https://your-agent.agents.do-ai.run"
         }
       }
     }
   }
   ```

### Updating Your Deployment

To update your deployed app, simply push changes to your Git repository. DigitalOcean App Platform will automatically build and deploy the new version.

## Usage Examples

### Get Event Information
"Tell me about TechCrunch Disrupt 2024"

### Search for Events
"Find AI conferences in San Francisco"

### Get Speaker Details
"Get information about Jensen Huang"

### Get Event Schedule
"What's the agenda for AWS re:Invent?"

### Ask Event Questions
"What are the most important tech conferences this year?"

## Understanding Results

### Event Information

The AI agent provides comprehensive information about:
- **Event Details**: Dates, locations, registration info
- **Speaker Information**: Bios, expertise, presentations
- **Schedules**: Session times, topics, activities
- **Search Results**: Relevant events based on your criteria

### Sample Output

```
📅 Event Information for: TechCrunch Disrupt 2024

TechCrunch Disrupt 2024 is one of the most anticipated startup conferences...
- Date: October 28-30, 2024
- Location: San Francisco, CA
- Focus: Early-stage startups, venture capital, emerging technologies
- Notable Speakers: [List of speakers]
- Key Sessions: [Session details]
```

## Troubleshooting

### Common Issues

**1. Import Errors**
- Make sure your virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Ensure gradient SDK is installed: `pip install gradient>=3.0.0b6`

**2. Agent Authentication Issues**
- Verify that `GRADIENT_AGENT_ACCESS_KEY` and `GRADIENT_AGENT_ENDPOINT` environment variables are set correctly
- Check that the DigitalOcean Gradient agent is properly trained and accessible
- Ensure the agent endpoint URL is in the correct format: `https://your-agent.agents.do-ai.run`

**3. DigitalOcean Deployment Issues**
- Check that the port is set to 8080 in both the code and the App Platform configuration
- Verify that all dependencies are in requirements.txt
- Check the deployment logs for any error messages

---

**Disclaimer**: This tool provides AI-generated event information. Always verify event details through official event websites and organizers before making any decisions or commitments.
