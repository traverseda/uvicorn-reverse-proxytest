Demonstrates issues with uvicorn running behind a reverse proxy.

endpoints:

 * https://uvicorn.localhost
 
Uvicorn running behind caddy reverse proxy. Headers are set properly but websocket gets mysterious 403 forbidden.

 * localhost:8000
 
 Uvicorn, no reverse proxy. Everything works alright.
 
 * https://quart.localhost
 
 Running bult in quart webserver, websockets work but `X-Forwarded-Proto` doesn't get set meaning the websockets aren't encrypted. This doesn't work
 with caddy's default configuration.
