'''
The main differences between the httpx and requests libraries in Python are centered around asynchronous support, HTTP/2 capabilities, and modern design. Here's a detailed comparison:
1. Asynchronous Support

    httpx:
    Supports both synchronous and asynchronous requests out-of-the-box.
    Example async usage:
    python

    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")

    requests:
    Synchronous only. For async, you need third-party wrappers (e.g., grequests, requests-async), which are less robust.

2. HTTP/2 Support

    httpx:
    Supports HTTP/2 (requires pip install httpx[http2]).
    Enables faster multiplexed requests and modern protocol features.

    requests:
    Only supports HTTP/1.1.

3. Performance

    httpx:
    Faster for concurrent tasks via async (e.g., handling 100+ requests simultaneously).
    Built-in connection pooling and HTTP/2 reduce latency.

    requests:
    Efficient for basic synchronous use cases but struggles with high concurrency without threading (adds complexity).

4. API Design & Features

    httpx:

        Modern API with first-class support for timeouts, redirects, and proxies.

        Built-in connection pooling and streaming responses (for large files/streams).

        Explicit Client instances for connection reuse (similar to requests.Session).

        Supports WebSocket connections (via httpx-ws).

    requests:
    Simpler API for straightforward use cases.
    Lacks built-in async/HTTP/2 but widely adopted in legacy code.

5. Type Hinting

    httpx:
    Full type annotation support (PEP 484 compliant).

    requests:
    Limited type hints (added gradually in newer versions).

6. Dependency Management

    httpx:
    Uses httpcore for low-level handling (supports Trio/AnyIO).

    requests:
    Relies on urllib3.

When to Use Which?

    Use requests for:
    Simple synchronous scripts, legacy projects, or when HTTP/2/async isn’t needed.

    Use httpx for:
    Modern applications requiring async, HTTP/2, better concurrency, or advanced features (e.g., streaming/WebSockets).

Code Example Comparison

Synchronous GET:
python

# requests
import requests
resp = requests.get("https://example.com")

# httpx
import httpx
resp = httpx.get("https://example.com")

Async GET:
python

# httpx (async)
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://example.com")
        print(resp.status_code)

asyncio.run(main())

Summary
Feature	httpx	requests
Async	✅ Built-in	❌ Requires third-party
HTTP/2	✅ Optional	❌ No
Sync	✅	✅
Performance	Faster for async/concurrency	Good for simple sync
Type Annotations	✅ Full support	⚠️ Partial
WebSockets	✅ (with extras)	❌ No
Legacy Support	⚠️ Newer (2019)	✅ Mature (since 2011)

For new projects requiring modern features, httpx is the recommended choice. For existing scripts or minimal needs, requests remains reliable.
'''