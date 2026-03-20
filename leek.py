


class LeetSpeak:
    LeetTable = {
                "A" : ("4","@"),
                "B" : ("8","|3"),
                "C" : ("(","<"),
                "D" : ("|)","[)"),
                "E" : ("3",""),
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
        if index > 1:
            index = index % 2
        elif index < 0:
            raise ValueError
        elif not isinstance(index, int):
            raise TypeError("Integer needed for leet conversion")
        for i in text.upper():
            if i in LeetSpeak.LeetTable:
                changed_text += LeetSpeak.LeetTable[i][index]
        text = changed_text
        print(text, changed_text)

        


Leet = LeetSpeak()
Leet.translate("apple", 0)
