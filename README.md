# Honeypot Setup

This repository contains a simple Python-based SSH honeypot that logs connection attempts and data received on a specified port. 

## Features
- Listens on a configurable port (`2222` by default).
- Logs all connection attempts and received data.
- Multi-threaded to handle multiple connection attempts simultaneously.
- Lightweight and easy to configure.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/theamitsiingh/Honeypot.git
    cd honeypot-setup
    ```

2. Install Python (Python 3.x recommended) and required packages:
    ```sh
    sudo apt-get install python3
    ```

3. Modify the `PORT` in `honeypot.py` if necessary (default is `2222`).

## Usage

1. Run the honeypot:
    ```sh
    python3 honeypot.py
    ```

2. The honeypot will start listening for connections on `0.0.0.0:2222` and log connection attempts in `honeypot.log`.

## Example Log Output
