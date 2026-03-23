


class LeetSpeak:
    LeetTable = {
                "A" : ("4","@"),
                "B" : ("8","|3"),
                "C" : ("(","<"),
                "D" : ("|)","[)"),
                "E" : ("3","€"),
                "F" : ("|=","ph"),
                "G" : ("6","9"),
                "H" : ("|-|","#"),
                "I" : ("1","!"),
                "J" : ("_|","_/"),
                "K" : ("|<","|{"),
                "L" : ("1","|_"),
                "M" : ("//\\","|/|"),
                "N" : ("||","//"),
                "O" : ("0","()"),
                "P" : ("|*","|o"),
                "Q" : ("0_","(,)"),
                "R" : ("|2","12"),
                "S" : ("5","$"),
                "T" : ("7","+"),
                "U" : ("|_|","(_)"),
                "V" : ("/","|"),
                "W" : ("\\//","vv"),
                "X" : ("><","}{"),
                "Y" : ("'/", "j"),
                "Z" : ("2", "7_")
                }
    
    @staticmethod
    def translate(text = "", index: int = 0):
        changed_text = ""
        if not isinstance(index, int):
            raise TypeError("Integer needed for leet conversion")
        elif index < 0 or index == float:
            raise ValueError
        elif index > 1:
            index = index % 2
        for i in text.upper():
            if i in LeetSpeak.LeetTable:
                changed_text += LeetSpeak.LeetTable[i][index]
        return changed_text

        


Leet = LeetSpeak()
Leet.translate("apple", 0)
Leet.translate("5 ApPlE piEs", 1)
#Leet.translate("apple", -1)
#Leet.translate("apple", "dog")
#Leet.translate("apple", 1.5)
