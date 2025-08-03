# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server that provides security scanning functionality for detecting and redacting sensitive information in text content. The server is implemented in Python and designed to work with Claude Desktop and other MCP clients.

## Architecture

The codebase follows a simple, focused structure:

- `mcpsecurity/mcp_server.py` - Main MCP server implementation using FastMCP
- `mcpsecurity/test_server.py` - Comprehensive test script for all functionality
- Security patterns defined as regex in `SENSITIVE_PATTERNS` dictionary
- Three main tools: `scan_for_sensitive_data`, `redact_text`, `validate_data_safety`
- Two resources: `security://patterns` and `security://help`

## Development Commands

### Testing the Server
```bash
# Run comprehensive functionality tests
/opt/homebrew/bin/python3.11 mcpsecurity/test_server.py

# Test server imports and basic loading
/opt/homebrew/bin/python3.11 -c "import mcpsecurity.mcp_server; print('Server loads successfully')"
```

### Running the Server
```bash
# Start the MCP server directly
/opt/homebrew/bin/python3.11 mcpsecurity/mcp_server.py
```

## Python Environment

- **Required Python Version**: 3.10+ (configured for 3.11)
- **Python Path**: `/opt/homebrew/bin/python3.11` (macOS Homebrew installation)
- **Dependencies**: MCP Python SDK (`mcp[cli]`)

## Security Detection Patterns

The server detects these sensitive data types via regex patterns in `SENSITIVE_PATTERNS`:
- password, api_key, token, email, phone, ssn, credit_card, ip_address, url_with_credentials

## MCP Configuration

For Claude Desktop integration, the server requires this configuration in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "security-scanner": {
      "command": "/opt/homebrew/bin/python3.11",
      "args": ["/ABSOLUTE/PATH/TO/PROJECT/mcpsecurity/mcp_server.py"]
    }
  }
}
```

## Core Functions

- `detect_sensitive_info(content: str)` - Core detection logic
- `redact_sensitive_info(content: str)` - Core redaction logic
- MCP tools are decorated with `@mcp.tool()` and follow FastMCP patterns
- MCP resources are decorated with `@mcp.resource()` for documentation access

## Testing Strategy

The `test_server.py` script provides comprehensive testing with:
- Multiple test cases covering all sensitive data types
- Resource access testing
- Validation testing with different allowed types
- Error handling verification