"""
Lowest Common Manager:

You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing to their direct reports.
The first input is the top manager in an organizational chart (i.e., the only instance that isn't anybody else's direct report),
 and the other two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct.
Write a function that returns the lowest common manager to the two reports.

Sample Input
    // From the organizational chart below.
    topManager = Node A
    reportOne = Node E
    reportTwo = Node I
            A
        /     \
        B       C
        /   \   /   \
    D     E F     G
    /   \
    H     I
Sample Output
    Node B

https://www.algoexpert.io/questions/Lowest%20Common%20Manager
"""


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


def getLowestCommonManager1(top_manager, report_one, report_two):
    common_manager = [None]
    getManagers(top_manager, report_one, report_two, common_manager)
    return common_manager[0]


def getManagers(curr, report_one, report_two, common_manager):

    count = 0

    # one of them is the common ancestor edge case
    if curr == report_one or curr == report_two:
        count = 1

    for report in curr.directReports:
        count += getManagers(report, report_one, report_two, common_manager)

    if common_manager[0] == None and count == 2:
        common_manager[0] = curr

    return count


""" """


class TreeInfo:
    def __init__(self, lowest_common_manager=None):
        self.lowest_common_manager = lowest_common_manager


def getLowestCommonManager(topManager, reportOne, reportTwo):
    treeInfo = TreeInfo()
    getLowestCommonManagerHelper(topManager, reportOne, reportTwo, treeInfo)
    return treeInfo.lowest_common_manager


def getLowestCommonManagerHelper(curr, reportOne, reportTwo, treeInfo):
    if not curr:
        return False

    found = curr == reportOne or curr == reportTwo
    for child in curr.directReports:
        child_found = getLowestCommonManagerHelper(child,
                                                   reportOne, reportTwo, treeInfo)
        if found and child_found:
            treeInfo.lowest_common_manager = curr
            return False
        found = found or child_found
    return found
