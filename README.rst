=======================================
giraffesay, your friendly JIRA tracker
=======================================

giraffesay is a simple JIRA task tracker, which will display a list of JIRA tickets and a giraffe (**jira**  ffe) from your terminal::

	cerfeta:~ joelvogt$ giraffesay

	===========  =================================================  ========
	Issue        Summary                                            Status
	===========  =================================================  ========
	PROD-166     Build script to generate input data (Gatling)      Open
	PROD-164     Performance testing Gatling>flood.io               Open
	===========  =================================================  ========

	                                                .-.  .-.
	                                                |  \/  |
	                                               /,   ,_  `'-.
	                                             .-|\   /`\     '.
	                                           .'  0/   | 0\  \_  `".
	                                        .-'  _,/    '--'.'|#''---'
	                                         `--'  |       /   \#
	                                               |      /     \#
	                                               \     ;|\    .\#
	                                               |' ' //  \   ::\#
	                                               \   /`    \   ':\#
	                                                `"`       \..   \#
	                                                           \::.  \#
	                                                            \::   \#
	                                                             '  .:\#
	                                                              \  :::\#
	                                                               \  '::\#
	                                                           jgs  \     \#

Installation
~~~~~~~~~~~~

giraffesay requires Python 3. Install dependencies: ``pip3 install jira tabulate``

Configuration
~~~~~~~~~~~~~

Add the following environment variables to your shell startup file:

	- ``JIRA_SERVER`` the JIRA api for your organization
	- ``JIRA_USER`` your JIRA user id
	- ``JIRA_PASSWORD`` your JIRA password
	- ``MY_ISSUES`` the JIRA query to retrieve issues of interest

My .bash_profile configuration 

::

	export JIRA_USER='myusername'
	export JIRA_SERVER="https://evrythng.atlassian.net"
	export JIRA_PASSWORD='mypassword'
	export MY_ISSUES='assignee = currentUser() AND status NOT IN  (DONE, RESOLVED, CLOSED) ORDER BY priority DESC'
	alias giraffesay='python3 giraffesay.py'

Usage
~~~~~

View your JIRA tickets from your terminal giraffesay from your terminal ``python3 giraffesay.py``

Credits
~~~~~~~

I'd like to thank the artist who created this giraffe and shared it on http://ascii.co.uk/art/giraffe
