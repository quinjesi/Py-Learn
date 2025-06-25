# Emoji Converter

def emoji_converter(msg):
    words = msg.split(" ")

    emoji_dict = {
        ":)": "😊",
        ":(": "😞",
        ":D": "😄",
        ";)": "😉",
        ":P": "😛",
        ":o": "😮",
        ":/": "😕"
    }

    output = ""
    for word in words:
        output += emoji_dict.get(word, word) + " "
    return output

msg = input(">: ")
print(emoji_converter(msg))


