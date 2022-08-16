
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        alphabet = {}
        alphabet['0'] = count['z']
        alphabet['2'] = count['w']
        alphabet['4'] = count['u']
        alphabet['6'] = count['x']
        alphabet['8'] = count['g']
        
        alphabet['3'] = count['h'] - alphabet['8'] #letter h in three & eight only
        alphabet['5'] = count['f'] - alphabet['4'] #letter f in four and five only
        alphabet['7'] = count['s'] - alphabet['6'] #letter s in seven and six only
        alphabet['9'] = count['i'] - alphabet['5'] - alphabet['6'] - alphabet['8'] #letter i in five, six, eight, nine only
        alphabet['1'] = count['n'] - alphabet['7'] - 2 * alphabet['9'] #letter n in one, seven, nine only
        
        res = []
        for key in sorted(alphabet.keys()): #sort the dictionary by keys so alphabet will have {'0': , '1': , ...}
            if alphabet[key] != 0:
                number = key * alphabet[key]
                res.append(number)
        
        return ''.join(res)
        