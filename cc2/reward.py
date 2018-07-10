def reward(R, gamma):
        accumulator = 0
        for k in range(230):  # fails at 229
                accumulator += (( gamma ** k ) * R )

        return accumulator  # TODONE
