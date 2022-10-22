def verifyIndexer(number):
    while (number > 25):
        number -= 26

    return number


class CifraCesar:
    def __init__(self, num, letters):
        if (num < 0):
            num += 26

        self.indexer = verifyIndexer(num)
        self.letters = letters
        self.message = ''

    def encryptMessage(self, text):
        str(text).split()
        for letter in text:
            try:
                index = self.letters.findLetterIndex(letter)
                self.message += self.letters.getLetter(
                    verifyIndexer(index + self.indexer))
            except:
                self.message += letter
        else:
            return self.message
