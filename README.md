# Agent Security MCP

A Model Context Protocol (MCP) server that provides security functionality for AI agents, focusing on detecting and redacting sensitive information in text content.

## Overview

This MCP server enables AI agents to perform security analysis by scanning text for sensitive data like passwords, API keys, emails, phone numbers, and other confidential information. It provides tools for detection, redaction, and validation of text content safety.

## Features

- **Sensitive Data Detection**: Scan text for various types of sensitive information
- **Automatic Redaction**: Remove or mask sensitive data from text
- **Data Safety Validation**: Check if text content meets safety requirements
- **Pattern-based Detection**: Uses configurable regex patterns for identification
- **Local Processing**: All data processing happens locally for privacy

## Quick Start

1. **Prerequisites**: Python 3.10+ and MCP Python SDK
2. **Installation**: Clone this repository
3. **Testing**: Run `python3.11 mcpsecurity/test_server.py`
4. **Configuration**: Add to Claude Desktop config (see mcpsecurity/README.md)

## Project Structure

```
Agent-Security-MCP/
├── README.md                    # This file
├── CLAUDE.md                   # Claude Code guidance
└── mcpsecurity/
    ├── README.md               # Detailed setup and usage guide
    ├── mcp_server.py          # Main MCP server implementation
    └── test_server.py         # Comprehensive test suite
```

## Documentation

- See `mcpsecurity/README.md` for detailed installation, configuration, and usage instructions
- See `CLAUDE.md` for development guidance when using Claude Code

## Security Focus

This tool is designed for **defensive security purposes only**:
- Detect sensitive data leaks
- Prevent accidental exposure of confidential information
- Validate content before sharing or publishing
- Assist in security audits and compliance checks

## License

This project is provided as-is for educational and security analysis purposes.
