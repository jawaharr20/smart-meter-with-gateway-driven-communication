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

## Usage

  # stm32
    It is used to get the values from the sensor using adc and it through uart to a5d2x
  # a5d2x
    It will receive the uart values from the stm32 process it send it to the Things board cloud and Display it in the Lcd
 # cloud
    The a5d2x sends the data to the Things  board cloud through the Telementry services 
    
## Documentation

Detailed documentation is available in the `docs/` directory. This includes:

- Architecture overview
- Communication protocol details
- API references
- Troubleshooting


## Contact

For questions, suggestions, or support, please open an issue or contact [jawaharr20](https://github.com/jawaharr20). or jawaharr16@gmail.com
