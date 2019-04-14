g = 34943
while True:
    Input = input()
    if Input == "":
        print("00 00")
    else:
        if Input[0] == "#":
            break
        # from g substract
        # [make text into bytes and get int from the bytes, multiply by 2 ** 16 to leave the crc bits empty] % g
        Int_Input = hex(g - int.from_bytes(Input.encode(), 'big') * 2 ** 16 % g)
        # cut out the hex notation characters
        Int_Input = Int_Input[2:]
        # gets its len
        InLen = len(Int_Input)
        # if len is less than 4, add zeroes in front
        Int_Input = ((4 - InLen) * "0" + Int_Input).upper()
        # format it and print
        print(Int_Input[:2] + " " + Int_Input[2:])
