this readme file i'm going to maintain for this project.
so that i can make use of this file by adding the required instructions for my personal use.

git clone <<github link>> (To clone a new project into local)
git branch (To list all branches) 
git pull (it pulls all remote branch references into your local)
git checkout -b "test-app" (To create a new branch by cutting a branch from base. Always create new branch from latest code.)
git add . (make all changes files into ready stage before committing)
git commit -m "some meaningful comment message" (execute this command if you are good to commit those changed files)
git push origin test-app (after commit your local changes won't get reflect into remote directory. so execute this command)
git stash (incase if you want to stash/clear all changed files)
git stash pop (incase if you decided to revert base all stashed files into you local)


Note: After cloning first time, default branch only will be listed.


short to open terminal is alt + f12 (open terminal)


reference link --> https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

How to setup github account in laptop?
To know your git version --> git --version
To know logged in git user --> git config user.name
To know logged in git email --> git config user.email
To setup github account in pc --> 
	git config --global user.name "*********"
	git config --global user.email *********@gmail.com
