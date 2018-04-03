from IPython import embed
import numpy as np
import re

def base_x_max(x,num_players):

	total = 0
	max_digit = x-1
	for i in xrange(num_players):
		total = total + max_digit*(x**i)
	return total


def to_base_x(x,n,num_players):

    s = ""
    while n:
        s = str(n % x) + s
        n /= x
    return '0'*(num_players - len(s)) + s

def at_least_one_in_each_team(iterator,num_teams):

	for i in xrange(num_teams):
		if str(i) not in iterator:
			return False
	return True

def get_team_steps(assignment, num_teams):

	team_scores = {}
	for i in xrange(num_teams):
		team_scores[str(i)] = []

	for player in xrange(len(assignment)):
		team_scores[assignment[player]].append(player_scores[player][1])

	results = {}
	for team in team_scores:
		results[team] = 1.0*sum(team_scores[team])/len(team_scores[team])

	return results

def brute_force(num_players, num_teams):

	assignment_scores = {}
	for n in xrange(base_x_max(num_teams,num_players)):
		assignment = str(to_base_x(num_teams,n,num_players))
		print assignment
		if at_least_one_in_each_team(assignment,num_teams):
			assignment_scores[assignment] = get_team_steps(assignment, num_teams)
	return assignment_scores

def evaluate(assignment_team_steps):

	assignment_scores = {}
	for i in assignment_team_steps:
		assignment_scores[i] = np.std(assignment_team_steps[i].values())
	return assignment_scores

def pretty_print_team(assignment):

	print assignment
	team = 0
	while(True):
		players = [m.start() for m in re.finditer(str(team), assignment)]
		if len(players) == 0:
			return
		print "Team {team}:".format(**locals())
		for player in players:
			print player_scores[player][0]
		print "----"
		team = team + 1
	return

def main():

	global player_scores
	player_scores = {
	0:['emma',388813],
	1:['raquel',359430],
	2:['ray',337150],
	3:['sergei',300071],
	4:['andreea',239065],
	5:['mitchell',150440],
	6:['sandra',471631],
	7:['mike',433345],
	8:['lynn',398030],
	9:['matthew',305385],
	10:['scott',260947],
	11:['james',144432],
	12:['clayton',106613],
	13:['olga',450000]
	}

	num_teams = 3
	num_players = len(player_scores)
	assignment_team_steps = brute_force(num_players, num_teams)
	scores = evaluate(assignment_team_steps)
	best = min(scores, key=scores.get)
	pretty_print_team(best)
	embed()

if __name__ == "__main__":
	main()
