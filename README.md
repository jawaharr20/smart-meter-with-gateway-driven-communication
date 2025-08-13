# Smart Meter with Gateway Driven Communication

This repository contains a project focused on smart meter technology integrated with gateway-driven communication.
The goal is to enable reliable, secure, and scalable data transmission between smart meters and centralized management systems using a gateway architecture.

## Features

- **Smart Meter Data Acquisition:** Collects electricity usage data from smart meters.
- **Gateway Communication:** Relays data securely from multiple smart meters to a central server or cloud platform.
- **Scalability:** Designed for integration with multiple meters and gateways.
- **Security:** Implements encryption and authentication for data transmission.
- **Modular Design:** Easy to extend or adapt for different communication protocols.

  
## Project Structure


        ├── gateway/           # Gateway software and communication logic
        ├── meter/             # Smart meter firmware and data acquisition
        ├── docs/              # Project documentation
        ├── scripts/           # Utility scripts for setup and testing
        ├── tests/             # Unit and integration tests


## Getting Started

### Prerequisites

- Python 3.x (for gateway scripts)   - a5d2x has python 3.5 only
- Microcontroller platform (for smart meter firmware)  - stm32 controller needded stmcubeide
- MQTT broker or HTTP server (as communication backend) - Things board cloud

## Components
 
        1)ZMPT101B - voltage sensor
        2)ACS712 - current sensor
        3)STM32F446RE - Microcontroller
        4)A5d2x -Microprocessor
        5)Bread board
        6)jumper wires
        7)ethernet cable

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jawaharr20/smart-meter-with-gateway-driven-communication.git
    cd smart-meter-with-gateway-driven-communication
    ```

2. **Install dependencies (Python):**

    ```bash
    cd gateway
    pip install -r requirements.txt
    ```

3. **Build and flash smart meter firmware:**

    - Refer to the `meter/README.md` for microcontroller setup instructions.

### Configuration

- Configure gateway connection parameters in `gateway/config.yaml`.
- Set up meter parameters in `meter/config.ini`.
- Ensure network connectivity between meters and gateway.

## Usage

- **Start the Gateway:**

    ```bash
    python gateway/main.py
    ```

- **Collect Data from Meters:**

    - Meters automatically send usage data to the gateway at configured intervals.

- **Monitor Communication:**

    - Use provided scripts in `scripts/monitor.py` to visualize or log data.

## Documentation

Detailed documentation is available in the `docs/` directory. This includes:

- Architecture overview
- Communication protocol details
- API references
- Troubleshooting


## Contact

For questions, suggestions, or support, please open an issue or contact [jawaharr20](https://github.com/jawaharr20). or jawaharr16@gmail.com
