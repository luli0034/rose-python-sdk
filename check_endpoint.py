#!/usr/bin/env python3
"""Simple script to check if Rose API endpoint is live and workable."""

import os
import sys
from rose_sdk import RoseClient
from rose_sdk.exceptions import RoseAPIError

# Configuration
BASE_URL = os.getenv('ROSE_BASE_URL', 'https://api.rose.kkv-test.com')
ACCESS_TOKEN = os.getenv('ROSE_ACCESS_TOKEN', 'u2ww3qaHjB+ELK/1+d4JqHKKRu0HYYPYUpW+D9qa2w0=')

def check_endpoint():
    """Check if the endpoint is live and workable."""
    if not ACCESS_TOKEN:
        print("❌ Error: ROSE_ACCESS_TOKEN environment variable not set")
        sys.exit(1)
    
    try:
        # Initialize client
        client = RoseClient(base_url=BASE_URL, access_token=ACCESS_TOKEN)
        
        # Check health
        print(f"🔍 Checking endpoint: {BASE_URL}")
        response = client.health_check()
        
        print("✅ Endpoint is live and workable!")
        print(f"   Response: {response}")
        return 0
        
    except RoseAPIError as e:
        print(f"❌ Endpoint check failed: {e.message}")
        if e.status_code:
            print(f"   Status Code: {e.status_code}")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(check_endpoint())

