# Hotel Hopper
#  Flag Question
# As the pandemic begins to wane, you're looking forward to traveling again. There are many hotels offering discounted vouchers that you can buy today and use later in a given timeframe. You're planning a holiday. (Let's pretend there are no travel restrictions.)
#
#
# There are h hotels offering vouchers for future use. Each voucher can be used to stay at the hotel between the dates d and D (inclusive) and have a value of v.
#
#
# You're planning to stay at as many hotels as possible with the goal to maximize the value of each stay. You are guaranteed that if you go to the hotel and present the voucher, you'll be able to stay between the dates d and D at no extra cost. Each of your vouchers is only valid for the given range, and you don’t plan to pay to extend your stay at any hotel. If you use a voucher, you must use on the date d and check out on the date D. You cannot check in later or check out before the given dates.
#
#
# What hotels will be on your itinerary?
#
# Input Format
#
# The first line: number of scenarios (n)
# For each scenario:
# A number of lines for the vouchers (V)
# The start date and end date (t, T) of your holiday are inclusive and separated by a space
# For each line in the next V lines:
# The hotel ID as a number (h)
# The inclusive range of dates (d, D) that you can use the voucher
# The value of the voucher as an integer (v)
# The data, separated by spaces (h d D v)
# All of the date inputs are in the dd MM yyyy format
# Constraints
#
# 0 ≤ h, v, V ≤ 1,000,000
# 2022-01-01 ≤ d, D, t, D ≤ 2030-12-31
# d < D and t < T
# The vouchers are only for the given range.
# The check-in and check-out time is 12:00 (noon), so you can go from hotel to hotel seamlessly.
# It is guaranteed that there is an answer and at least one voucher will be used.
# Output Format
#
# For each scenario, list the maximum amount of value you can obtain from using the vouchers.
# A hyphen surrounded by spaces to separate the maximum value and the hotel list
# List of the hotel IDs ordered by stay dates separated by spaces (h1 h2 h3)
# If there are multiple possibilities, choose a voucher that has earlier expiring date
# Sample Input
#
# 3
# 1
# 2022 01 01 2022 12 31
# 1 2022 01 01 2022 12 31 5000
# 2
# 2022 01 01 2022 12 31
# 1 2022 01 01 2022 01 02 3000
# 5 2022 01 01 2022 01 02 5000
# 3
# 2022 01 01 2022 12 31
# 1 2022 01 01 2022 01 31 7000
# 12 2022 01 01 2022 01 30 7000
# 55 2022 02 01 2022 02 31 2000
# Sample Output
#
# 5000 - 1
# 5000 - 5
# 9000 - 12 55
# Sample output explanation
#
# For the first test case, there is only one possible stay: 2022-01-01 at the value of 5000 at hotel 1.
#
#
# For the second test case, both hotels 1 and 5 offer vouchers for 2022-01-01 to 2022-01-02, so since you have to choose one of them, you choose hotel 5 which offers a higher value.
#
#
# For the last test case, you can enjoy all three hotels. Hotels 1 and 12 fall into an overlapping period, so you choose the one with earlier check-out date (12), and we'll get 12,55.
#



from datetime import date, timedelta

def main():
  n = int()
  for i in range(n):
      V = int()
      holiday = list(map(int,input().split()))
      t = date(holiday[0], holiday[1], holiday[2])
      T = date(holiday[3],holiday[4], holiday[5])
      data = list(map(int,input().split()))
      h = data[0]
      d = date(data[1], data[2], data[3])
      D = date(data[4], data[5], data[6])
      v = data[7]
      print(v,h)


if __name__ == '__main__':
    main()