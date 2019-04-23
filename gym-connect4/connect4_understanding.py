import random
import copy
# import math
# import numpy as np

# from keras.models     import Sequential
# from keras.layers     import Dense
# from keras.optimizers import Adam

import gym
# from gym import spaces, error, utils
# from gym.utils import seeding
import gym_connect4

ENV = gym.make('Connect4-v0')
ENV.reset()
MAX_STEPS = 21 # half of 7 x 6 board
# This is the score that means Ulima has done well.
# Could do it as a proportion of wins..?
INITIAL_GAMES = 1
SCORE_REQUIREMENT = 1
RAND = random.Random()

class Ulima():

    def model_data_preparation(self):
        # for each play we want to store the state of the board and the move
        training_data = []
        accepted_scores = []
        for _ in range(INITIAL_GAMES): # start by playing 10,000 games
            score = 0

            for _ in range(MAX_STEPS):
                # action = ENV.action_space.sample() # can we change this to .get_avail_moves
                action = RAND.choice(ENV.get_avail_moves())
                observation, reward, done, _ = ENV.step(action)

                # hot_action is the current Ulima move
                hot_action = [0, 0, 0, 0, 0, 0]
                hot_action.insert(action, 1)

                copy_observation = copy.deepcopy(observation)
                training_data += [copy_observation, hot_action]
                score += reward
                accepted_scores.append(score)
                if done:
                    break

            ENV.reset()

        print(accepted_scores)
        return training_data


    # def build_model(input_size, output_size):
    #     model = Sequential()
    #     model.add(Dense(128, input_dim=input_size, activation='relu'))
    #     model.add(Dense(52, activation='relu'))
    #     model.add(Dense(output_size, activation='linear'))
    #     model.compile(loss='mse', optimizer=Adam())
    #     return model
    #
    #
    # def train_model(self.training_data):
    #     X = np.array([i[0] for i in self.training_data]).reshape(-1,
    #         len(self.training_data[0][0]))
    #     y = np.array([i[1] for i in self.training_data]).reshape(-1,
    #         len(self.training_data[0][1]))
    #     model = build_model(input_size=len(X[0]), output_size=len(y[0]))
    #
    #     model.fit(X, y, epochs=10)
    #     return model
    #
    # trained_model = train_model(self.training_data)