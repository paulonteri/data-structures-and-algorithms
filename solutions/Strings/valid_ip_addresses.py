"""
Valid IP Addresses:

You're given a string of length 12 or smaller, containing only digits. 
Write a function that returns all the possible IP addresses that can be created by inserting three .s in the string.
An IP address is a sequence of four positive integers that are separated by .s, where each individual integer is within the range 0 - 255, inclusive.
An IP address isn't valid if any of the individual integers contains leading 0s. 
 For example, "192.168.0.1" is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and 01, respectively.
  Another example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.
Your function should return the IP addresses in string format and in no particular order.
If no valid IP addresses can be created from the string, your function should return an empty list.


Sample Input
    string = "1921680"
Sample Output
    [
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0"
    ]
    // The IP addresses could be ordered differently.
https://www.algoexpert.io/questions/Valid%20IP%20Addresses
"""


def is_valid_ip(string):

    string_as_num = int(string)
    if string_as_num < 0 or string_as_num > 255:
        return False

    # check for leading zeros
    return len(str(string_as_num)) == len(string)


# O(1) time | O(1) space
# |-> there are a limited/finite/constant number (2^32) of IP Addresses
def validIPAddresses0(string):
    length = len(string)
    all_ip_addresses = []

    ip_address = ['', '', '', '']
    for i_one in range(1, min(length, 4)):
        ip_address[0] = string[:i_one]
        if not is_valid_ip(ip_address[0]):
            continue  # stop current for loop run

        for i_two in range(i_one+1, min(length, i_one+4)):
            ip_address[1] = string[i_one:i_two]
            if not is_valid_ip(ip_address[1]):
                continue  # stop current for loop run (for i_two)

            for i_three in range(i_two+1, min(length, i_two+4)):
                ip_address[2] = string[i_two:i_three]
                ip_address[3] = string[i_three:]
                if is_valid_ip(ip_address[2]) and is_valid_ip(ip_address[3]):
                    all_ip_addresses.append(".".join(ip_address))

    return all_ip_addresses


def is_valid_ip_section(string):
    if len(string) > 3 or len(string) < 1 or int(string) > 255:
        return False
    # ensure no leading zeros
    if len(string) > 1 and string[0] == "0":
        return False
    return True


# O(1) time | O(1) space
def validIPAddresses(string):
    output = []

    for dot_one in range(1, min(4, len(string))):
        sections = ["", "", "", ""]
        part_one = string[:dot_one]
        if is_valid_ip_section(part_one):
            sections[0] = part_one

            for dot_two in range(dot_one+1, min(dot_one+4, len(string))):
                sections[1] = string[dot_one:dot_two]
                if not is_valid_ip_section(sections[1]):
                    continue

                for dot_three in range(dot_two+1, min(dot_two+4, len(string))):
                    sections[2] = string[dot_two:dot_three]
                    if not is_valid_ip_section(sections[2]):
                        continue

                    sections[3] = string[dot_three:]
                    if not is_valid_ip_section(sections[3]):
                        continue

                    full_ip = ".".join(sections)
                    if len(full_ip) == len(string)+3:
                        output.append(full_ip)

    return output
