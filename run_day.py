"""Module for running day simulation."""

from random import choice
from fsm import FiniteStateMachine


def run(day: FiniteStateMachine):
    """Run day simulation.

    Args:
        day (FiniteStateMachine): Day object.
    """
    probs = (0, 1)
    for hour in range(24):
        prob = choice(probs)
        day.send((prob, hour))


if __name__ == "__main__":
    my_day = FiniteStateMachine()
    run(my_day)
