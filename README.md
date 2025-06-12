# Flight Delay Analysis

## Setup
1. Download uv: [link](https://docs.astral.sh/uv/)
2. Download repo
  `git clone https://github.com/mav3ri3k/flight_delays.git`
3. Setup the repo
  - Setup the environment for local development
    `cd ./flight_delays`
    `uv sync`
  - Download the dataset
    `curl https://static.apurva-mishra.com/flightdata.csv -O`
4. Start juypter notebook
  `uv run --with jupyter jupyter lab`
