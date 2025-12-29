#!/usr/bin/env python3
"""
Entry point for running the web dashboard on Render.
This only starts the FastAPI web server, not the MCP stdio server.
"""
import os
import uvicorn
from src.polymarket_mcp.web.app import app

if __name__ == "__main__":
    # Get port from environment (Render sets this automatically)
    port = int(os.getenv("PORT", 8080))
    host = os.getenv("HOST", "0.0.0.0")
    
    # Start the web server
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )
