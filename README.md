# Distributed Systems Load Balancer

This project implements a load balancer for a distributed system using Docker containers. The load balancer distributes incoming requests among multiple server instances using consistent hashing.

## Introduction

This project demonstrates the implementation of a load balancer that distributes traffic among multiple server instances. The load balancer is built using Flask and Docker and utilizes consistent hashing to manage server instances dynamically.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Additional Python packages as listed in `requirements.txt`

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Build the Docker image:**
    ```sh
    docker build -t server_image .
    ```

3. **Start the Docker containers:**
    ```sh
    docker run --name server1 -d --network=app-network -e SERVER_ID=server1 --rm server_image
    docker run --name server2 -d --network=app-network -e SERVER_ID=server2 --rm server_image
    docker run --name server3 -d --network=app-network -e SERVER_ID=server3 --rm server_image
    ```

4. **Run the load balancer:**
    ```sh
    python load_balancer.py
    ```

## Usage

To interact with the load balancer, you can use the following endpoints:

- **Get Replicas:** `GET /rep`
- **Add Replica:** `POST /add` with JSON body `{"n": 1, "hostnames": ["server4"]}`
- **Remove Replica:** `DELETE /rm` with JSON body `{"n": 1, "hostnames": ["server1"]}`

## Testing

A sample `test_balancer.py` script is provided to test the load balancer functionality:

```python
import requests

url = 'http://localhost:8000/home'  # Adjust the URL if necessary

responses = [requests.get(url).text for _ in range(10)]
for response in responses:
    print(response)
To run the test script:

sh
Copy code
python test_balancer.py
Experiments

1. Server Fault Tolerance
The following graph shows the request distribution among servers when one of the servers fails:


![output](https://github.com/michellenekesa/DistributedSystems/assets/105868059/33f99fc1-3587-429f-aff9-7d8c73526c50)

2. Scalability Experiment
The following graph shows the average load distribution as the number of servers increases:
![output 3](https://github.com/michellenekesa/DistributedSystems/assets/105868059/19a8ea1c-d8f0-4462-acaa-127cea5f8933)

3. Another Server Fault Tolerance Test
The following graph shows the request distribution among servers in another fault tolerance scenario:
![output 2](https://github.com/michellenekesa/DistributedSystems/assets/105868059/f0f7b92c-25b9-42d8-93b0-a3265a64d2a7)
