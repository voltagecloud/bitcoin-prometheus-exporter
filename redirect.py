import json

def request(flow):
    flow.request.port = 8334
    flow.request.scheme = "https"

    # Check if the request method is POST
    if flow.request.method == "POST":
        # Parse the JSON content
        data = json.loads(flow.request.text)
        # Modify the data
        data["jsonrpc"] = "2.0"
        # Update the request content
        flow.request.text = json.dumps(data)