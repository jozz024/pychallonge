from . import tournaments, matches, participants
from .api import set_credentials

class ChallongeTournament:
    def __init__(self, id, username, api_key):
        # Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
        set_credentials(username, api_key)
        self.tournament = tournaments.show(id)
        self.matches = self.get_matches()
        self.participants = self.get_all_participants()

    # Tournaments
    def start_tournament(self):
        tournaments.start(self.tournament["id"])

    def reset_tournament(self):
        tournaments.reset(self.tournament["id"])

    def end_tournament(self):
        tournaments.finalize(self.tournament["id"])

    # Participants
    def get_all_participants(self):
        # Retrieve the participants for a given tournament.
        users = participants.index(self.tournament["id"])
        return users

    def add_participant(self, name, challonge_username = None, email = None, seed = None, misc = None):
        participants.create(self.tournament["id"], name, challonge_username=challonge_username, email=email, seed=seed, misc=misc)

    def mass_add_participants(self, names):
        participants.bulk_add(self.tournament["id"], names)

    def get_participant(self, player_id):
        return participants.show(self.tournament["id"], player_id)

    def get_participant_from_group_player_id(self, id):
        for participant in self.participants:
            if participant["group_player_ids"][0] == id:
                return participant

    def update_participant(self, id, name, challonge_username = None, email = None, seed = None, misc = None):
        participants.update(self.tournament["id"], id, name=name, challonge_username=challonge_username, email=email, seed=seed, misc=misc)

    def check_in_participant(self, id):
        participants.check_in(self.tournament["id"], id)

    def un_check_in_participant(self, id):
        participants.undo_check_in(self.tournament["id"], id)

    def delete_participant(self, id):
        participants.destroy(self.tournament["id"], id)

    def clear_participants(self):
        participants.clear(self.tournament["id"])

    def randomize_participants(self):
        participants.randomize(self.tournament["id"])

    # Matches

    def get_matches(self, state = "all", participant_id = None):
        return matches.index(self.tournament["id"], state=state, participant_id = participant_id)

    def get_match(self, id):
        return matches.show(self.tournament["id"], id)

    def update_match(self, id, scores_csv = None, winner_id = None, player1_votes = None, player2_votes = None):
        matches.update(self.tournament["id"], id, scores_csv=scores_csv, winner_id=winner_id, player1_votes=player1_votes, player2_votes=player2_votes)

    def reopen_match(self, id):
        matches.reopen(self.tournament["id"], id)

    def mark_match_in_progress(self, id):
        matches.mark_as_underway(self.tournament["id"], id)

    def unmark_match_in_progress(self, id):
        matches.unmark_as_underway(self.tournament["id"])








