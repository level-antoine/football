class State:

    def __init__(self):
        self.active_player = False
        self.ball = False
        self.ball_owned_team = None
        self.ball_owned_player = None
        self.nb_left_player = 0
        self.nb_right_player = 0
        self.score_left_team = 0
        self.score_right_team = 0
        self.front_of_goal = False

    def toString(self):
        print(self.active_player)
        print(self.ball)
        print(self.ball_owned_team)
        print(self.ball_owned_player)
        print(self.nb_left_player)
        print(self.nb_right_player)
        print(self.score_left_team)
        print(self.score_right_team)
        print(self.front_of_goal)

    def equals(self, other_state):
        if other_state.active_player != self.active_player:
            return False
        if other_state.ball != self.ball:
            return False
        if other_state.ball_owned_team != self.ball_owned_team:
            return False
        if other_state.ball_owned_player != self.ball_owned_player:
            return False
        if other_state.nb_left_player != self.nb_left_player:
            return False
        if other_state.nb_right_player != self.nb_right_player:
            return False
        if other_state.score_left_team != self.score_left_team:
            return False
        if other_state.score_right_team != self.score_right_team:
            return False
        if other_state.front_of_goal != self.front_of_goal:
            return False
        return True