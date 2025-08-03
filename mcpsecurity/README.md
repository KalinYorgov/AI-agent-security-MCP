# MCP Security Scanner Server

A Model Context Protocol (MCP) server that provides defensive security functionality for AI agents, focusing on detecting and redacting sensitive information in text content.

## Features

### 🔍 **Security Tools**
- **scan_for_sensitive_data**: Detect sensitive information like passwords, API keys, emails, phone numbers, etc.
- **redact_text**: Automatically redact sensitive information from text
- **validate_data_safety**: Validate text content against allowed sensitive data types

### 📊 **Detected Data Types**
- Passwords and secrets
- API keys and tokens
- Email addresses
- Phone numbers
- Social Security Numbers (SSN)
- Credit card numbers
- IP addresses
- URLs with embedded credentials

### 📚 **Resources**
- **security://patterns**: View the regex patterns used for detection
- **security://help**: Get help and usage examples

## Installation

### Prerequisites
- Python 3.10 or higher (recommended: 3.11)
- The MCP Python SDK
- macOS with Homebrew (for the provided installation commands)

### Setup

1. **Install Python 3.11** (if not already installed):
   ```bash
   brew install python@3.11
   ```

2. **Install the MCP SDK**:
   ```bash
   /opt/homebrew/bin/python3.11 -m pip install "mcp[cli]"
   ```

3. **Test the server**:
   ```bash
   /opt/homebrew/bin/python3.11 test_server.py
   ```

## Usage with Claude Desktop

### 1. Configure Claude Desktop

Create or edit the Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration:

```json
{
  "mcpServers": {
    "security-scanner": {
      "command": "/opt/homebrew/bin/python3.11",
      "args": ["/ABSOLUTE/PATH/TO/YOUR/PROJECT/mcp_server.py"]
    }
  }
}
```

**Important**: Replace `/ABSOLUTE/PATH/TO/YOUR/PROJECT/` with the actual absolute path to your project directory (e.g., `/Users/username/Projects/Agent-Security-MCP/mcpsecurity/mcp_server.py`).

### 2. Restart Claude Desktop

After saving the configuration, restart Claude Desktop completely.

### 3. Verify Installation

In Claude Desktop, you should see a tools icon (🔨) appear. Click it to see the available security tools.

## Example Usage

### Scanning for Sensitive Data
```
Can you scan this text for sensitive information: "My email is john@example.com and my API key is 'sk-1234567890'"
```

### Redacting Sensitive Information
```
Please redact any sensitive data from: "Contact support at help@company.com or call 555-123-4567"
```

### Validating Data Safety
```
Check if this text is safe for public sharing, allowing only email addresses: "Contact us at info@company.com"
```

## Manual Testing

Run the test script to see the server in action:

```bash
/opt/homebrew/bin/python3.11 test_server.py
```

This will demonstrate:
- Detection of various sensitive data types
- Redaction capabilities
- Validation with different policies
- Resource access

## Configuration

### Adding New Patterns

To add new sensitive data patterns, edit the `SENSITIVE_PATTERNS` dictionary in `mcp_server.py`:

```python
SENSITIVE_PATTERNS = {
    "your_pattern": re.compile(r'your_regex_here', re.IGNORECASE),
    # ... existing patterns
}
```

### Customizing Redaction

The redaction format can be customized in the `redact_sensitive_info` function:

```python
redacted_content = pattern.sub(f'[CUSTOM_REDACTION_{pattern_name.upper()}]', redacted_content)
```

## Troubleshooting

### Server Not Appearing in Claude Desktop

1. **Check the configuration file path** - Ensure you're editing the correct file
2. **Verify the absolute path** - Make sure the path to `mcp_server.py` is correct
3. **Restart Claude Desktop** - Close completely and reopen
4. **Check Python path** - Ensure `/opt/homebrew/bin/python3.11` exists

### Testing the Server Manually

```bash
# Test imports
/opt/homebrew/bin/python3.11 -c "import mcp_server; print('Server loads successfully')"

# Run functionality test
/opt/homebrew/bin/python3.11 test_server.py
```

### Python Version Issues

If you encounter Python version errors:

```bash
# Check your Python version
/opt/homebrew/bin/python3.11 --version

# Should be 3.11.x or higher
```

## Security Notes

- **Defensive Security Only**: This server is designed for defensive security analysis and data protection
- **Local Processing**: All data processing happens locally - no data is stored or transmitted
- **Pattern Customization**: Detection patterns are based on common formats and may need customization for specific use cases
- **Testing Required**: Always test with your specific data formats before relying on the detection
- **Privacy Focused**: Designed to help prevent data leaks and protect sensitive information

## Development

### Project Structure
```
mcpsecurity/
├── mcp_server.py      # Main MCP server implementation
├── test_server.py     # Test script demonstrating functionality
└── README.md          # This file
```

### Adding New Tools

To add new security tools, follow the pattern in `mcp_server.py`:

```python
@mcp.tool()
def your_new_tool(parameter: str) -> dict[str, Any]:
    """
    Description of your tool
    
    Args:
        parameter: Description of the parameter
        
    Returns:
        Dictionary with results
    """
    # Your implementation here
    return {"result": "your_result"}
```

## License

This project is provided as-is for educational and security analysis purposes. 