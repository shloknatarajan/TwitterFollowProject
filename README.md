Twitter Follow Project

Initial Run: Run once at the beginning of the project, will not be needed to run regularly
1.	Writes list of all people the account is following into following.txt using myfollowing.py 
2.	Add new stuff from following.txt to followed.txt using updatefollowed.py
    a.	Run updatefollowed.py to do this
3.	Writes list of all people following mlamons into followers.txt using myfollowers.py

Doc Updater: Run before any other processes (daily)
	The data in followers.txt and following.txt needs to be updated to include new followers and to remove nonfollowers (all nonfollowers from followers.txt, but just the ones we unfollow from following.txt)
1.	Run updatefollowers.py  - updates the followers.txt with the most recent followers
2.	Don’t (usually) need to run anything for the following.txt file as all changes to the following will be taken care of by followusers.py or nonfollowers.py
    a.	When followusers.py is run it adds the users to followed.txt and following.txt
    b.	When nonfollowers.py is run, all the removed users are removed from following.txt
    c.	If manual follows are done, run the updatefollowing.py then updatefollowed.py method before doing anything else

Unfollow nonfollowers: Run after doc updater
1.	Calculates nonfollowers by comparing the following list to the followers list
    a.	(This is why it’s important to have updated followers and following lists)
    b.	Unfollows a certain number of nonfollowers (specified in code)
    c.	Removes the unfollowed users from the following list

Following Users: Run process after nonfollowers.py
1.	When filteredprelim.txt is empty - followermining.py generates a list of the followers of a certain user and puts it in prelim.txt
    a.	I have not been running followercheck.py recently so currently just putting all the data straight into filteredprelim.txt
    b.	Followercheck.py takes the users from prelim.txt, checks if they have over 50 followers, then puts the ones that do inside filteredprelim.txt
2.	Followusers.py follows the users in the filteredprelim.txt file and adds them to both the following.txt file and the followed.txt file

Text File Info:
Filteredprelim.txt – this is where followusers.py gets the users to follow
Followed.txt – a list of all people the user has followed
	Run updatefollowed.py right after running the myfollowing.py program
	Also updated by the followusers.py program 
Followers.txt – a list of all the people following the mlamons account, calculated using a research account that creates a list of all the followers using myfollowers.py and updated by updatefollowers.py
Following.txt – list of who mlamons is following. Initially created using myfollowing.py (will take a while). Then updates are typically taken care of in followusers.py and nonfollowers.py. If manual following is done run updatefollowing.py
Nonfollowers.txt – calculated by nonfollowers.py, a list of all people in the following.txt doc but not in the followers.txt doc
Prelim.txt – Used to be used for creating an initial list of people and filtering is applied on top. Currently not being utilized
Temp.txt – Used for testing and by some methods for temporary text storage

Process
0.	Perform initial run: run myfollowing.py and myfollowers.py and wait until complete before doing any operations. Then run updatefollowed.py
Daily process:
1.	Run updatefollowers.py. Wait until complete
2.	Run nonfollowers.py. Wait until complete
    a.	On Skejul account, run this once every 3 days
3.	Run followusers.py. Wait until complete
Deviations will occur when: manual follows/unfollows are ever done, filteredprelim.txt runs out of people to follow (email me and I will send more users to follow, running the followermining.py operation myself), if errors start occurring, and maybe once a month when the initial process (step 0) is repeated.  
