# Flight Delay Analysis

## Setup
1. Download uv: [link](https://docs.astral.sh/uv/)
2. Download repo\
  `git clone https://github.com/mav3ri3k/flight_delays.git`
3. Setup the repo
  - Setup the environment for local development\
    `cd ./flight_delays`\
    `uv sync`
4. Start juypter notebook\
  `uv run --with jupyter jupyter lab`

## Project Structure
> [!NOTE]
> For correct working, each sub-project item must be run in order given below.

### Data Collection
File: `data_collection.ipynb`

### Data Pre-Processing
File: `pre-processing.ipynb`

### Model Building
File: `model.ipynb`

### Application Building
File: `app.py`

> [!TIP]
> To run use `uv run streamlit run app.py`

