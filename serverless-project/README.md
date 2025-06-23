# Serverless Multi-Runtime Project

This project demonstrates a Serverless application with functions in both Python and Node.js runtimes.

## Project Structure

```
.
├── functions/
│   ├── python/
│   │   └── handler.py     # Python function
│   └── nodejs/
│       └── handler.js    # Node.js function
├── serverless.yml         # Serverless configuration
└── requirements.txt       # Python dependencies
```

## Prerequisites

- Node.js 14.x or later
- Python 3.8
- Serverless Framework (`npm install -g serverless`)
- AWS credentials configured

## Setup

1. Install Serverless Framework globally:
   ```bash
   npm install -g serverless
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt -t functions/python/
   ```

3. Deploy the application:
   ```bash
   cd serverless-project
   serverless deploy
   ```

## Available Endpoints

After deployment, you'll get two endpoints:
- Python Function: `GET /python/hello`
- Node.js Function: `GET /nodejs/hello`

## Development

- Python function: `functions/python/handler.py`
- Node.js function: `functions/nodejs/handler.js`

After making changes, redeploy with:
```bash
serverless deploy
```
