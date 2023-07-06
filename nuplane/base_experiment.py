#!/usr/bin/env python

# Copyright (c) 2021 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

from .utils.transform import join_dicts

BASE_EXPERIMENT_CONFIG = {}


class BaseExperiment(object):
    def __init__(self, config):
        self.config = join_dicts(BASE_EXPERIMENT_CONFIG, config)

    def reset(self):
        """Called at the beginning and each time the simulation is reset"""
        pass

    def get_action_space(self):
        """Returns the action space"""
        raise NotImplementedError

    def get_observation_space(self):
        """Returns the observation space"""
        raise NotImplementedError

    def get_actions(self):
        """Returns the actions"""
        raise NotImplementedError

    def compute_action(self, action):
        """Given the action, returns a XPlane.VehicleControl() which will be applied to the hero

        :param action: value outputted by the policy
        """
        raise NotImplementedError

    def get_observation(self, sensor_data):
        """Function to do all the post processing of observations (sensor data).

        :param sensor_data: dictionary {sensor_name: sensor_data}

        Should return a tuple or list with two items, the processed observations,
        as well as a variable with additional information about such observation.
        The information variable can be empty
        """
        return NotImplementedError

    def get_done_status(self, observation, core):
        """Returns whether or not the experiment has to end"""
        return NotImplementedError

    def compute_reward(self, observation, core):
        """Computes the reward"""
        return NotImplementedError
