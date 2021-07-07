import os
import sys
import datetime

sa = sys.argv

now = datetime.datetime.now()
default_msg = "{} 강의".format(now.strftime("%Y-%m-%d"))
commit_msg = default_msg
has_msg = len(sa) >= 2

if has_msg:
    commit_msg = sa[1]

if has_msg == False:
    input_msg = input("Default Message?? (Yes:Enter or Input Message)>>>")
    if input_msg:
        commit_msg = input_msg

print(commit_msg)

os.system("git add --all")
os.system("git commit -am{}".format(commit_msg))
os.system("git push")
