from deep_translator import MyMemoryTranslator
def englishtofrench(englishtext):
    """Function translate en to fr"""
    #write the code here
    frenchtext = MyMemoryTranslator(source='english', target='french').translate(englishtext)
    print(frenchtext)
    return frenchtext


def frenchtoenglish(frenchtext):
    """Function translate fr to en"""
    englishtext = MyMemoryTranslator(source='french', target='english').translate(frenchtext)
    print(englishtext)
    return englishtext
