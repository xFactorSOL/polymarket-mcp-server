#!/usr/bin/env python3
"""
Entry point for running the web dashboard on Render.
This only starts the FastAPI web server, not the MCP stdio server.
"""
import os
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment (Render sets this automatically)
    port = int(os.getenv("PORT", 8080))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"Starting Polymarket MCP Web Dashboard on {host}:{port}")
    print(f"Python path: {sys.path}")
    
    # Use string-based import for uvicorn (more reliable)
    uvicorn.run(
        "polymarket_mcp.web.app:app",
        host=host,
        port=port,
        log_level="info",
        reload=False
    )
