"""
prototyping for all bold and italics conversion.
"""

index = 0
tindex = 0 # tag index
sindex = 0 # sign index (bold and italic, bold, italic)
lookups = [[["***", "___", "__*", "**_"], ["**", "__"], ["*", "_"]], [["***", "___", "*__", "_**"], ["**", "__"], ["*", "_"]], [["<strong><i>", "<strong><i>", "<strong><i>", "<strong><i>"], ["<strong>", "<strong>"], ["<i>", "<i>"]], [["</i></strong>", "</i></strong>", "</i></strong>", "</i></strong>"], ["</strong>", "</strong>"], ["</i>", "</i>"]]]
result = []
with open("mistakes", "r+") as a:
    for x in a:
        try:
            raw = a.readline(index)
            for y in a.readline(index):
                print("Current line:")
                print(a.readline(index))
                try:
                    alpha = raw[:raw.find(lookups[0][sindex][tindex])] + lookups[2][sindex][tindex] + raw[raw.find(lookups[0][sindex][tindex]) + len(lookups[0][sindex][tindex]):]
                    beta = alpha[:alpha.find(lookups[1][sindex][tindex])] + lookups[3][sindex][tindex] + alpha[alpha.find(lookups[1][sindex][tindex]) + len(lookups[1][sindex][tindex]):]
                    raw = beta
                    tindex += 1
                except IndexError:
                    if tindex > len(lookups[0][sindex]) and sindex < 4:
                        tindex = 0
                        sindex += 1
                    pass
                pass
            pass
            print("the end:")
            print(raw)
        except IndexError:
            pass
        pass
        index += 1
    pass
pass
