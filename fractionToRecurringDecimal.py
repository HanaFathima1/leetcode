"""

LC: 166. Fraction to Recurring Decimal

Medium

Topics:
Hash Table
Math
String

Hint
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
294,196/1.1M
Acceptance Rate
27.9%

Hint 1
No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Hint 2
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Hint 3
Notice that once the remainder starts repeating, so does the divided result.
Hint 4
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

"""

class Solution:
    def fractionToDecimal(self, numerator:int, denominator:int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator<0) ^ (denominator<0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator//denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        res.append(".")
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                res.insert(remainder_map[remainder], "(")
                res.append(")")
                break
            remainder_map[remainder] = len(res)
            remainder*=10
            res.append(str(remainder//denominator))
            remainder%=denominator
        return "".join(res)
sol = Solution()
print(sol.fractionToDecimal(numerator = 1, denominator = 2))
print(sol.fractionToDecimal(numerator = 2, denominator = 1))
print(sol.fractionToDecimal(numerator = 4, denominator = 333))

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # If numerator is 0, the result is exactly "0" (no sign, no fractional part).
        if numerator == 0:
            return "0"

        # We'll build the answer in a list of strings for efficient appends,
        # then join at the end. (Faster than repeated string concatenation.)
        res = []

        # Determine sign: append '-' if exactly one of numerator/denominator is negative.
        # The '^' operator performs boolean XOR here.
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # Work with positive values to simplify division logic.
        # (LeetCode guarantees denominator != 0.)
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part of the fraction (before the decimal point).
        # Floor division gives the integer quotient.
        res.append(str(numerator // denominator))

        # Remainder after extracting integer part; this drives the fractional digits.
        remainder = numerator % denominator

        # If there's no remainder, we have an exact integer — return result now.
        if remainder == 0:
            return "".join(res)

        # Otherwise, we will have a fractional part — add the decimal point.
        res.append(".")

        # Map to remember where each remainder first appeared in the result.
        # Key: remainder value
        # Value: index in `res` where the digit produced from this remainder was placed
        # (i.e., the position of the first fractional digit coming from this remainder).
        remainder_map = {}

        # Simulate long division until remainder becomes 0 (terminating) or repeats (recurring).
        while remainder != 0:
            # If we have seen this remainder before, the fractional part from that index onward repeats.
            if remainder in remainder_map:
                # Insert '(' at the index where this remainder first produced a digit.
                # That marks the start of the repeating sequence.
                res.insert(remainder_map[remainder], "(")
                # Append ')' to close the repeating sequence at the current end.
                res.append(")")
                break  # we've inserted parentheses and can stop

            # Record the position in `res` where the next digit (from this remainder) will go.
            remainder_map[remainder] = len(res)

            # Long division step: bring down a zero.
            remainder *= 10

            # Append the next digit (quotient of remainder // denominator).
            res.append(str(remainder // denominator))

            # Update remainder for the next iteration.
            remainder %= denominator

        # Join the parts into the final string and return.
        return "".join(res)
