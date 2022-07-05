import numpy as np

NUM_PRISONERS = 100
MAX_TRIES = 50
NUM_TRIALS = 1000


def simulate_loop_strategy(boxes):
    """
    simulate the loop strategy: open a box and follow the trail (loop)
    until a box containing the given prisoner finds his ID or MAX_TRIES is exhausted

    boxes: an array of size NUM_PRISONERS, with each box containing a random prisoner ID
    returns: number of prisoners who could successfully find their ID
    """
    res = []
    for prisoner in range(NUM_PRISONERS):
        found = False
        curr = boxes[prisoner]
        for _ in range(MAX_TRIES - 1):
            if curr == prisoner:
                found = True
                break
            else:
                curr = boxes[curr]

        res.append(found)

    return sum(res)


def simulate_random_strategy(boxes):
    """
    simulate the random strategy: keep opening random boxes
    until a box containing the given prisoner finds his ID or MAX_TRIES is exhausted

    boxes: an array of size NUM_PRISONERS, with each box containing a random prisoner ID
    returns: number of prisoners who could successfully find their ID
    """
    res = []
    for prisoner in range(NUM_PRISONERS):
        found = False
        boxes_to_open = np.random.choice(
            range(NUM_PRISONERS),
            size=MAX_TRIES,
            replace=False
        )

        for b_ix in boxes_to_open:
            if boxes[b_ix] == prisoner:
                found = True
                break

        res.append(found)

    return sum(res)


if __name__ == '__main__':
    PRISONERS = range(NUM_PRISONERS)

    num_success_loop_strategy = []
    num_success_random_strategy = []
    for _ in range(NUM_TRIALS):
        random_boxes = np.random.permutation(PRISONERS)
        num_prisoners_success_loop = simulate_loop_strategy(random_boxes)
        num_prisoners_success_random = simulate_random_strategy(random_boxes)

        num_success_loop_strategy.append(
            num_prisoners_success_loop == NUM_PRISONERS
        )
        num_success_random_strategy.append(
            num_prisoners_success_random == NUM_PRISONERS
        )

    print(
        f"P(success_loop) = {sum(num_success_loop_strategy) / NUM_TRIALS}"
    )
    print(
        f"P(success_random) = {sum(num_success_random_strategy) / NUM_TRIALS}"
    )
