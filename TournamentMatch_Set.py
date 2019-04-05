"""
s1={1,2,3,4,5,6}
s2={3,4,2,5,6,7}

s3=s1.union(s2)
s4=s1|s2
print "Union is ",s3,"and",s4

s3=s1.intersection(s2)
s4=s1&s2
print "intersection is ",s3,"and",s4

s3=s1.difference(s2)
s4=s1-s2
print "Difference is ",s3,"and",s4

s3=s1.symmetric_difference(s2)
s4=s1^s2
print "Symmetric_diffrence is ",s3,"and",s4
"""

"""
SET decleration: Syntax: S1=set()
s1.add(ele)
s1.remove(ele):strictly remove(error if element not present)
s1.discard(ele):Pyar se remove(No error if elemrnt not present)
"""

#Assignment: Tournament Match winner using SET data struture

teams=set()
left_team=set()
left_winner=set()
right_winner=set()
right_team=set()
winner=set()

total_teams=int(raw_input("Enter total number of teams:"))

for each_team_counter in range(total_teams):
	team=raw_input('Enter Team%s:' %(each_team_counter+1)).upper()
	teams.add(team)

if len(teams)==1:
	print "Winner is:%s" %teams.pop()

elif total_teams>1:
	#If teams are even. Spliting into two parts
	if total_teams%2==0:
		for i in range(0,(total_teams/2)):
			left_team.add(teams.pop())
		for j in range((total_teams/2),total_teams):
			right_team.add(teams.pop())
		
		left_len=len(left_team)
		temp_set=set()
		for i in range(left_len):
			ele=left_team.pop()
			temp_set.add(ele)
			if len(temp_set)==2:
				print temp_set
				win=raw_input("Whose the winner in these two:").upper()
				if win in temp_set:
					left_winner.add(win)
					temp_set.clear()
				else:
					print "Wrong team name entered!"
				if len(left_winner)==2:
					print left_winner
					lw=raw_input("Enter who is the final left winner here:").upper()
					if lw in left_winner:
						temp=lw
						left_winner.clear()
						left_winner.add(temp)
					else:
						print "Wrong Input!"
		
		right_len=len(right_team)
		temp_set=set()
		for i in range(right_len):
			ele=right_team.pop()
			temp_set.add(ele)
			if len(temp_set)==2:
				print temp_set
				win=raw_input("Whose the winner in these two:").upper()
				if win in temp_set:
					right_winner.add(win)
					temp_set.clear()
				else:
					print "Wrong team name entered!"
				if len(right_winner)==2:
					print right_winner
					rw=raw_input("Enter who is the final right winner here:").upper()
					if rw in right_winner:
						temp=rw
						right_winner.clear()
						right_winner.add(temp)
					else:
						print "Wrong Input!"

		winner= left_winner|right_winner
		print winner

	else:
		pass

print "Left winner:", left_winner
