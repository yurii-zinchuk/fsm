"""Module for storing a Finite State Machine implementation."""


class FiniteStateMachine:
    """
    Class to represent a day model.
    """

    def __init__(self) -> None:
        """Define day instance with different states."""
        self.s0 = self.state_sleep()
        next(self.s0)
        self.s1 = self.state_eat()
        next(self.s1)
        self.s2 = self.state_study()
        next(self.s2)
        self.s3 = self.state_drink_beer()
        next(self.s3)
        self.s5 = self.state_cry()
        next(self.s5)
        self.s6 = self.state_excercise()
        next(self.s6)
        self.state = self.s0

    def send(self, info: tuple) -> None:
        """Send info to python coroutine.

        Args:
            info (tuple): Info to send.
        """
        self.state.send(info)

    def state_sleep(self) -> None:
        """Create sleep state behaviour."""
        while True:
            overslept, hour = yield
            if hour == 7:
                if overslept:
                    print(
                        f"\nTime: {hour} o`clock.\nAhh, shit, overslept again...\nTime to study."
                    )
                    self.state = self.s2
                else:
                    print(
                        f"\nTime: {hour} o`clock.\nAnother greate morning.\nTime to eat."
                    )
                    self.state = self.s1

    def state_eat(self) -> None:
        """Create eat state behaviour."""
        while True:
            _, hour = yield
            if hour == 8:
                print(
                    f"\nTime: {hour} o`clock.\nSuper tasty breakfest.\nTime to study."
                )
                self.state = self.s2
            elif hour == 19:
                print(f"\nTime: {hour} o`clock.\nGreat supper. Time to sleep.")
                self.state = self.s0

    def state_study(self) -> None:
        """Create study state behaviour."""
        while True:
            homework, hour = yield
            if homework and hour == 18:
                print(
                    f"\nTime: {hour} o`clock.\nI had a lot of homework.\nTime to cry."
                )
                self.state = self.s5
            elif homework:
                print(
                    f"\nTime: {hour} o`clock.\nI got a lot of homework.\nTime to study more."
                )
                self.state = self.s2
            else:
                print(
                    f"\nTime: {hour} o`clock.\nGreat, I got little homework.\nTime to excercise."
                )
                self.state = self.s6

    def state_excercise(self) -> None:
        """Create excercise state bahaviour."""
        while True:
            friends, hour = yield
            if friends:
                print(
                    f"\nTime: {hour} o`clock.\nCool, my friends called.\nTime to drink beer."
                )
                self.state = self.s3
            else:
                print(f"\nTime: {hour} o`clock.\nGreat excercise.\nTime to eat.")
                self.state = self.s1

    def state_drink_beer(self) -> None:
        """Create drink beer behaviour."""
        while True:
            _, hour = yield
            print(f"\nTime: {hour} o`clock.\nBeer very good.\nTime to sleep.")
            self.state = self.s0

    def state_cry(self) -> None:
        """Create cry behaviour."""
        while True:
            _, hour = yield
            print(f"\nTime: {hour} o`clock.\nIm a crybaby.\nTime to sleep.")
            self.state = self.s0
