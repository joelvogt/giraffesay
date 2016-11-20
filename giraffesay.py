# -*- coding: utf-8 -*-
import os

from jira import JIRA
from tabulate import tabulate

jira_user = os.environ['JIRA_USER']
jira_password = os.environ['JIRA_PASSWORD']
jira_server = os.environ['JIRA_SERVER']
my_issues = os.environ['MY_ISSUES']

"""Giraffe source: http://ascii.co.uk/art/giraffe, Accessed: 16.11.2016"""
giraffe = """
{margin}        .-.  .-.
{margin}        |  \/  |
{margin}       /,   ,_  `'-.
{margin}     .-|\   /`\     '.
{margin}   .'  0/   | 0\  \_  `".
{margin}.-'  _,/    '--'.'|#''---'
{margin} `--'  |       /   \#
{margin}       |      /     \#
{margin}       \     ;|\    .\#
{margin}       |' ' //  \   ::\#
{margin}       \   /`    \   ':\#
{margin}        `"`       \..   \#
{margin}                   \::.  \#
{margin}                    \::   \#
{margin}                     \'  .:\#
{margin}                      \  :::\#
{margin}                       \  '::\#
{margin}                   jgs  \     \#
{margin}                         \
"""
giraffe_length = len(giraffe.split('\n')[0]) - len('{margin}')

jira = JIRA(basic_auth=(jira_user, jira_password), server=jira_server)  # a username/password tuple

issues = dict()
status = dict()
issue_width = 0
status_width = 0
summary_width = 0
for issue in jira.search_issues(my_issues):
    summary = issue.fields.summary
    issues[issue.key] = summary
    if len(issue.key) > issue_width:
        issue_width = len(issue.key)
    status[issue.key] = issue.fields.status.name
    if len(status[issue.key]) > status_width:
        status_width = len(status[issue.key])

issues_table = []
col_sep = 2

columns, _ = os.get_terminal_size()
max_summary_line_width = columns - (status_width + issue_width + col_sep * 2)
for issue in issues:
    tokens = issues[issue].strip().split()
    summary_line_length = 0
    line = []
    issue_row = [[issue, line, status[issue]]]

    for word in tokens:
        if (summary_line_length + len(word) + 1) >= max_summary_line_width:
            issue_row[-1][1] = ''.join(issue_row[-1][1])
            summary_line_length = 0
            line = []
            issue_row.append([" ", line, " "])
            line_length = 0
        summary_line_length += len(word) + 1
        if summary_line_length > summary_width:
            summary_width = summary_line_length
        line.append(word)
        line.append(' ')
    if len(issue_row[-1][1]) == 0:
        issue_row.pop()
    issue_row[-1][1] = ''.join(issue_row[-1][1])
    issues_table.extend(issue_row)

output = tabulate(issues_table, tablefmt='rst', headers=["Issue", "Summary", "Status"])

giraffe_shift = issue_width + summary_width
giraffe_shift = giraffe_shift - (columns %(giraffe_shift + giraffe_length)) - col_sep
print("""
{}
{}
""".format(output, giraffe.format(margin=' ' * giraffe_shift)))
