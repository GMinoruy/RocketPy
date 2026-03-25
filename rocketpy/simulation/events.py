class Event:
    def __init__(self, trigger, action, name):
        """Initializes an Event object.

        Parameters
        ----------
        trigger : function
            A function that takes the current state of the simulation as input and returns a boolean value. The event will be triggered when this function returns True.
        action : function
            A function that takes the current state of the simulation as input and performs some action when the event is triggered.
        name : str
            A name for the event, used for identification purposes.

        """
        self.trigger = trigger
        self.action = action
        self.name = name

    # TODO: check_trigger does note receive enough arguments to substitute parachute events
    def check_trigger(self, state):
        """Checks if the event should be triggered based on the current state of the simulation.

        Parameters
        ----------
        state : dict
            The current state of the simulation, containing information such as altitude, velocity, and time.

        Returns
        -------
        bool
            True if the event should be triggered, False otherwise.

        """
        return self.trigger(state)

    def execute_action(self, state):
        """Executes the action associated with the event.

        Parameters
        ----------
        state : dict
            The current state of the simulation, containing information such as altitude, velocity, and time.

        """
        return self.action(state)

    def __repr__(self):
        # TODO: Implement a more informative string representation of the Event object.
        pass

    def __str__(self):
        # TODO: Implement a more informative string representation of the Event object.
        pass

    def __call__(self, *args, **kwds):
        # TODO: This should call the action (or the trigger?)
        pass


# TODO: Implement functions which are standard types of events, such as motor burnout events, landing events, etc.
# def motor_burnout_trigger(state):
#     """A trigger function that returns

# # TODO: think about this
# class ParachuteEvent(Event):


#     def __init__(self, trigger, action, name, parachute):
#         """Initializes a ParachuteEvent object.

#         Parameters
#         ----------
#         trigger : function
#             A function that takes the current state of the simulation as input and returns a boolean value. The event will be triggered when this function returns True.
#         action : function
#             A function that takes the current state of the simulation as input and performs some action when the event is triggered.
#         name : str
#             A name for the event, used for identification purposes.
#         parachute : Parachute
#             The parachute associated with this event.

#         """
#         super().__init__(trigger, action, name)
#         self.parachute = parachute

#     def apogee_trigger(state):
#         """A trigger function that returns True when the rocket reaches apogee.

#         Parameters
#         ----------
#         state : dict
#             The current state of the simulation, containing information such as altitude, velocity, and time.

#         Returns
#         -------
#         bool
#             True if the rocket has reached apogee, False otherwise.

#         """
#         return state['velocity'] <= 0
