from consistent_hash import ConsistentHash
import requests

ch = ConsistentHash()

# Add servers
ch.add_server("http://localhost:4000")
ch.add_server("http://localhost:4001")
ch.add_server("http://localhost:4002")

# Function to route request
def route_request(key):
    server = ch.get_server(key)
    if server:
        response = requests.get(f"{server}/home")
        return response.json()
    else:
        return {"error": "No servers available"}

# Example usage
if __name__ == "__main__":
    key = "my_key"
    result = route_request(key)
    print(f"Server response for key '{key}': {result}")

    key = "another_key"
    result = route_request(key)
    print(f"Server response for key '{key}': {result}")
