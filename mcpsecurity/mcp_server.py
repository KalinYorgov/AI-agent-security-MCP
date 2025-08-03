#!/usr/bin/env python3.11

import re
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Security Scanner")

# Patterns to detect sensitive data
SENSITIVE_PATTERNS = {
    "password": re.compile(r'password\s*[=:]\s*["\'].*?["\']', re.IGNORECASE),
    "api_key": re.compile(r'api[_-]?key\s*[=:]\s*["\'].*?["\']', re.IGNORECASE),
    "token": re.compile(r'(token|secret|key)\s*[=:]\s*["\'].*?["\']', re.IGNORECASE),
    "email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    "phone": re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
    "ssn": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    "credit_card": re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
    "ip_address": re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),
    "url_with_credentials": re.compile(r'https?://[^:]+:[^@]+@[^\s]+', re.IGNORECASE)
}

def detect_sensitive_info(content: str) -> dict[str, list[str]]:
    """Detect sensitive information in content and return findings by type."""
    findings = {}
    for pattern_name, pattern in SENSITIVE_PATTERNS.items():
        matches = pattern.findall(content)
        if matches:
            findings[pattern_name] = matches
    return findings

def redact_sensitive_info(content: str) -> str:
    """Redact sensitive information from content."""
    redacted_content = content
    for pattern_name, pattern in SENSITIVE_PATTERNS.items():
        redacted_content = pattern.sub(f'[REDACTED_{pattern_name.upper()}]', redacted_content)
    return redacted_content

@mcp.tool()
def scan_for_sensitive_data(text: str) -> dict[str, Any]:
    """
    Scan text content for sensitive information like passwords, API keys, emails, etc.
    
    Args:
        text: The text content to scan for sensitive information
        
    Returns:
        Dictionary containing scan results with detected sensitive data types and redacted content
    """
    try:
        findings = detect_sensitive_info(text)
        has_sensitive_data = bool(findings)
        
        result = {
            "has_sensitive_data": has_sensitive_data,
            "sensitive_data_types": list(findings.keys()) if findings else [],
            "findings_count": sum(len(matches) for matches in findings.values()),
            "redacted_content": redact_sensitive_info(text) if has_sensitive_data else text
        }
        
        if findings:
            result["findings_detail"] = findings
            result["alert"] = f"⚠️ Found {result['findings_count']} sensitive data items of types: {', '.join(findings.keys())}"
        else:
            result["alert"] = "✅ No sensitive data detected"
            
        return result
        
    except Exception as e:
        return {
            "error": f"Error scanning content: {str(e)}",
            "has_sensitive_data": False,
            "redacted_content": text
        }

@mcp.tool()
def redact_text(text: str) -> dict[str, Any]:
    """
    Redact sensitive information from text content.
    
    Args:
        text: The text content to redact
        
    Returns:
        Dictionary containing the redacted text and summary of redactions
    """
    try:
        original_findings = detect_sensitive_info(text)
        redacted_content = redact_sensitive_info(text)
        
        return {
            "original_text": text,
            "redacted_text": redacted_content,
            "redactions_made": list(original_findings.keys()) if original_findings else [],
            "redaction_count": sum(len(matches) for matches in original_findings.values()),
            "status": "redacted" if original_findings else "no_redaction_needed"
        }
        
    except Exception as e:
        return {
            "error": f"Error redacting content: {str(e)}",
            "redacted_text": text,
            "status": "error"
        }

@mcp.tool()
def validate_data_safety(text: str, allowed_types: Optional[list[str]] = None) -> dict[str, Any]:
    """
    Validate if text content is safe based on allowed sensitive data types.
    
    Args:
        text: The text content to validate
        allowed_types: List of allowed sensitive data types (e.g., ['email', 'phone'])
        
    Returns:
        Dictionary containing validation results
    """
    try:
        findings = detect_sensitive_info(text)
        allowed_types = allowed_types or []
        
        # Check for disallowed sensitive data
        disallowed_findings = {
            data_type: matches for data_type, matches in findings.items()
            if data_type not in allowed_types
        }
        
        is_safe = not bool(disallowed_findings)
        
        return {
            "is_safe": is_safe,
            "all_findings": findings,
            "disallowed_findings": disallowed_findings,
            "allowed_types": allowed_types,
            "validation_message": "✅ Content is safe" if is_safe else f"❌ Content contains disallowed sensitive data: {', '.join(disallowed_findings.keys())}"
        }
        
    except Exception as e:
        return {
            "error": f"Error validating content: {str(e)}",
            "is_safe": False
        }

@mcp.resource("security://patterns")
def get_security_patterns() -> str:
    """Get information about the security patterns used for detection."""
    pattern_info = []
    for name, pattern in SENSITIVE_PATTERNS.items():
        pattern_info.append(f"- {name}: {pattern.pattern}")
    
    return f"""Security Scanner Patterns:

{chr(10).join(pattern_info)}

These patterns are used to detect and redact sensitive information in text content.
"""

@mcp.resource("security://help")
def get_help() -> str:
    """Get help information about using the security scanner."""
    return """Security Scanner MCP Server Help

Available Tools:
1. scan_for_sensitive_data(text) - Scan text for sensitive information
2. redact_text(text) - Redact sensitive information from text
3. validate_data_safety(text, allowed_types) - Validate if text is safe

Available Resources:
1. security://patterns - View detection patterns
2. security://help - This help information

Example Usage:
- Scan: scan_for_sensitive_data("My email is user@example.com")
- Redact: redact_text("Password: secret123")
- Validate: validate_data_safety("Contact: user@example.com", ["email"])

Detected Data Types:
- password, api_key, token, email, phone, ssn, credit_card, ip_address, url_with_credentials
"""

if __name__ == "__main__":
    mcp.run()
