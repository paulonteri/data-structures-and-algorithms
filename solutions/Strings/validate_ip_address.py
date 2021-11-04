""" 
Validate IP Address

Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
    1 <= xi.length <= 4
    xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
    Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:
    Input: IP = "172.16.254.1"
    Output: "IPv4"
    Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
    Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Output: "IPv6"
    Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
    Input: IP = "256.256.256.256"
    Output: "Neither"
    Explanation: This is neither a IPv4 address nor a IPv6 address.
Example 4:
    Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    Output: "Neither"
Example 5:
    Input: IP = "1e1.4.5.6"
    Output: "Neither"
 

Constraints:

IP consists only of English letters, digits and the characters '.' and ':'.


https://leetcode.com/problems/validate-ip-address/solution
"""


# O(n) time | O(1) space
class Solution:
    def validIPAddress(self, IP: str):
        if ":" in IP:
            return self.validateIPv6(IP)
        return self.validateIPv4(IP)

    def validateIPv4(self, IP):
        if len(IP) > 15:
            return "Neither"
        if IP.count(".") != 3:
            return "Neither"

        for section in IP.split("."):
            if not section.isnumeric():
                return "Neither"

            num = int(section)
            # cannot contain leading zeros
            if not len(section) == len(str(num)):
                return "Neither"

            # 0 <= xi <= 255
            if num < 0 or num > 255:
                return "Neither"
        return "IPv4"

    def validateIPv6(self, IP):
        if len(IP) > 39:
            return "Neither"
        if IP.count(":") != 7:
            return "Neither"

        for section in IP.split(":"):
            if not section.isalnum():
                return "Neither"

            # 1 <= xi.length <= 4
            if len(section) < 1 or len(section) > 4:
                return "Neither"

            # digits, lower-case English letter ('a' to 'f') and upper-case ('A' to 'F').
            for char in section:
                is_number = char.isnumeric()
                is_corr_char = ord(char.lower()) >= ord(
                    "a") and ord(char.lower()) <= ord("f")
                if not (is_number or is_corr_char):
                    return "Neither"
        return "IPv6"
