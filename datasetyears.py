from selenium import webdriver
browser=webdriver.Chrome('C:\Atharv\Ipl_squad_builder\chromedriver')
# browser.get("https://www.youtube.com/watch?v=GJjMjB3rkJM")
browser.get("https://www.cricbuzz.com/cricket-scorecard-archives")
file_name='team_composition.csv'
f=open(file_name,'a')
match_count=37
years=['2011','2012','2013','2014','2015','2016','2017','2018','2019']
for x in years:
	browser.find_element_by_link_text(x).click()
	browser.find_element_by_partial_link_text('Indian Premier League').click()
	matches=browser.find_elements_by_class_name('cb-series-matches')
	length=len(matches)
	teams=['Mumbai Indians','Chennai Super Kings','Delhi Capitals','Sunrisers Hyderabad','Kolkata Knight Riders','Kolkata Knight Riders','Kings XI Punjab','Rajasthan Royals','Royal Challengers Bangalore','Rising Pune Supergiant','Gujarat Lions','Deccan Chargers','Kochi Tuskers Kerala','Pune Warriors']
	for i in range(length):
		batsman=0
		batting_allrounder=0
		bowling_allrounder=0
		bowler=0
		home_team_index=18
		away_team_index=23
		matches=browser.find_elements_by_class_name('cb-series-matches')
		text=matches[i].find_element_by_class_name('text-gray').text
		if text=='Wankhede Stadium, Mumbai':
			matches[i].find_element_by_class_name('text-hvr-underline').click()
			winner=browser.find_element_by_class_name('cb-min-stts').text
			browser.find_element_by_link_text('Match Facts').click()
			if winner!='No result':
				for x in teams:
					if x in winner:
						match_winner=x
						break
				if match_winner=='Mumbai Indians':
					check_index=home_team_index
				else:
					check_index=away_team_index
				for i in range(11):
					elem=browser.find_elements_by_class_name('cb-mat-fct-itm')
					players=elem[check_index].find_elements_by_class_name('text-hvr-underline')
					players[i].click()
					profile=browser.find_elements_by_class_name('cb-lst-itm-sm')
					role=profile[5].text
					if role=='Batsman':
						batsman+=1
					elif role=='Bowler':
						bowler+=1
					elif role=='Batting Allrounder':
						batting_allrounder+=1
					elif role=='Bowling Allrounder':
						bowling_allrounder+=1
					else:
						batsman+=1
					browser.back()
				print("batsman",batsman,"bowlers",bowler,"batting allrounder",batting_allrounder,"bowling allrounder",bowling_allrounder)
				f.write(str(match_count)+","+str(batsman)+","+str(bowler)+","+str(batting_allrounder)+","+str(bowling_allrounder)+"\n")
				match_count+=1
				browser.back()
			browser.back()
	browser.back()
	browser.back()
f.close()



		


		



