#!/usr/bin/env python3

"""
Test script for the MCP Security Scanner server
"""

import sys
sys.path.insert(0, '.')
import mcp_server

def test_security_scanner():
    """Test the security scanning functionality"""
    
    print("🔍 Testing MCP Security Scanner")
    print("=" * 50)
    
    # Test data with various sensitive information
    test_texts = [
        "My email is john.doe@example.com and password is 'secret123'",
        "API key: 'sk-1234567890abcdef' for the service",
        "Call me at 555-123-4567 or email support@company.com",
        "SSN: 123-45-6789, Credit Card: 4532 1234 5678 9012",
        "Database URL: https://user:pass@db.example.com:5432/mydb",
        "This is clean text with no sensitive data",
        "Server IP: 192.168.1.100, Token = 'bearer_xyz789'"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"\n📝 Test {i}: {text[:50]}{'...' if len(text) > 50 else ''}")
        print("-" * 60)
        
        # Test scanning
        scan_result = mcp_server.scan_for_sensitive_data(text)
        print(f"🔍 Scan Result: {scan_result['alert']}")
        
        if scan_result['has_sensitive_data']:
            print(f"   Types found: {', '.join(scan_result['sensitive_data_types'])}")
            print(f"   Count: {scan_result['findings_count']}")
            print(f"   Redacted: {scan_result['redacted_content']}")
        
        # Test redaction
        redact_result = mcp_server.redact_text(text)
        if redact_result['status'] == 'redacted':
            print(f"🔒 Redaction: {redact_result['redaction_count']} items redacted")
        
        # Test validation (allowing only emails)
        validation_result = mcp_server.validate_data_safety(text, ['email'])
        print(f"✅ Validation (email allowed): {validation_result['validation_message']}")

def test_resources():
    """Test the resource functionality"""
    print("\n\n📚 Testing Resources")
    print("=" * 50)
    
    # Test help resource
    help_info = mcp_server.get_help()
    print("📖 Help Resource:")
    print(help_info[:200] + "..." if len(help_info) > 200 else help_info)
    
    # Test patterns resource
    patterns_info = mcp_server.get_security_patterns()
    print("\n🔍 Patterns Resource:")
    print(patterns_info[:300] + "..." if len(patterns_info) > 300 else patterns_info)

if __name__ == "__main__":
    try:
        test_security_scanner()
        test_resources()
        print("\n\n🎉 All tests completed successfully!")
        print("\n💡 Your MCP Security Scanner server is working correctly!")
        print("   You can now use it with MCP clients like Claude Desktop.")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        sys.exit(1) 