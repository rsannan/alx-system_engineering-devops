# My first postmortem

Issue Summary:
	From 8:33 AM to 7:46 PM GMT, all requests to my web server 01 returned 500 error response messages.
This at its root was caused by a bad configuration file that shutdown the nginx server running on the web server.

Timeline (all times Greenwich Mean Time):
	. 8:33 AM: Bad configuration file is pushed
	. 8:34 AM: Server goes down
	. 8:45 AM: Engineer is alerted
	. 8:50 AM: Investigation begins
	. 7:10 PM: Configuration file is updated
	. 7:30 PM: All tests complete and file is uploaded
	. 7:43 PM: Server restarts
	. 7:46 PM: Traffic is back online

Root Cause:
	At 8:33 AM GMT, a change was made to the nginx configuration file that was meant to add integration for datadog monitoring service. The change was, due to a bad script written over the original configuration file instead of appended to the end of it. This among other things crucially removed the original server listening and redirect options. This meant that the server was no longer listening on any port and thereby unable to server our web pages.

Resolution and Recovery:
	At 8:45 AM GMT, Our engineer was alerted and he quickly began investigating the issue.
	At 7:10 PM GMT, The configuration file in questions is updated and tested.
	At 7:46PM GMT, The server is brought back online.

Corrective and preventative measures:
	Upon internal review of our systems we came to the realization that we need to take some measures to enusre such things do not occur and when they do are dealt with swiftly.
	. A web monitoring service has been added to reduce to time required to alert the engineers.
	. A new method of testing has been introduced to ensure all files are production ready before they are pushed.
