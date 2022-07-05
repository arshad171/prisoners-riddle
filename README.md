# Simulating the 100-Prisoners Riddle

This project contains a simple Python script to simulate the solution to the seamingly impossible 100-Prisoners Riddle, and compares the success probabilities for "loop strategy" and "random strategy". (Refer the references for more details)

## Running the Script

1. Install the requirements: `pip3 install -r requirements.txt`

2. Run the script: `python3 main.py`

## Tweaking the Experiment Parameters

The following global params in the script can be tweaked: `NUM_PRISONERS`, `MAX_TRIES`, `NUM_TRIALS`

Few interesting observations following the intuition:

1. Increasing `NUM_PRISONERS` decreases the probability of all prisoners finding their respective ID.

2. Increasing `MAX_TRIES` increases the probability of succeeding.

3. Increasing `NUM_TIRALS` produces a better estimate of the probability.

4. Default params:
    - `NUM_PRISONERS = 100`
    - `MAX_TRIES = 50`
    - `NUM_TRIALS = 1000`

    With the above params, the probability of all prisoners finding their ID as found to be close to 0.3 while following the "loop strategy" and close to 0.0 while following the "random strategy". The obtained results corroborate the theoretical results [2]

## References

1. Original paper: Gál, A., & Miltersen, P.B. (2003). The Cell Probe Complexity of Succinct Data Structures. BRICS, Department of Computer Science, University of Aarhus. All rights reserved. – https://ve42.co/GalMiltersen

2. Video explanation by Veritasium: https://www.youtube.com/watch?v=iSNsgj1OCLA&t=80s