// Test file for MCP Security Scanner
// This file contains various types of sensitive data for testing

// Password examples
const password = "5444";
const userPassword = "mySecretPass123";
const dbPassword = "admin123";

// API Keys and Tokens
const apiKey = "sk-1234567890abcdef";
const secretToken = "ghp_1234567890abcdefghijklmnopqrstuvwxyz";
const authToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9";

// Email addresses
const userEmail = "john.doe@example.com";
const supportEmail = "support@mycompany.org";

// Phone numbers
const phoneNumber = "555-123-4567";
const contactPhone = "555.987.6543";

// Credit card (fake for testing)
const creditCard = "4532-1234-5678-9012";

// IP addresses
const serverIP = "192.168.1.100";
const publicIP = "203.0.113.42";

// URL with credentials
const databaseUrl = "https://user:password123@db.example.com:5432/mydb";

// SSN (fake for testing)
const ssn = "123-45-6789";

// Mixed content
const config = {
    database: {
        host: "192.168.1.50",
        user: "admin",
        password: "dbSecret2023",
        url: "mongodb://admin:secret@localhost:27017/myapp"
    },
    email: {
        smtp: "smtp.gmail.com",
        user: "notifications@myapp.com",
        password: "emailPass456"
    },
    support: {
        phone: "1-800-555-0199",
        email: "help@myapp.com"
    }
};

console.log("This is a test file for the MCP Security Scanner"); 