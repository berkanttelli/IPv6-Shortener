def LeadingZeroRemove(block):
    newblock = ""
    lastIndex = len(block) - 1
    for i, str in enumerate(block):
        if i != lastIndex and str == "0":
            continue
        else:
            newblock += str
    return newblock


def Ipv6compression(ipv6):
    try:
        ipv6blocks = ipv6.split(":")
        newIpv6 = ""
        saveBlock = []
        for i in ipv6blocks:
            if i[0] == "0":
                block = LeadingZeroRemove(i)
                saveBlock.append(block)
            else:
                saveBlock.append(i)
        blockIndex = 0
        zerosRemoved = False
        removeContigiousCounter = 0
        while len(saveBlock) != 0:
            if (
                zerosRemoved == False
                and saveBlock[blockIndex][0] == "0"
                and len(saveBlock[blockIndex]) == 1
            ):
                for i in range(blockIndex, len(saveBlock)):
                    if len(saveBlock[i]) == 1:
                        removeContigiousCounter += 1
                    else:
                        break
                for i in range(blockIndex, removeContigiousCounter):
                    saveBlock.remove(saveBlock[blockIndex])
                newIpv6 += ":"
                zerosRemoved = True
                continue
            else:
                newIpv6 += saveBlock[blockIndex] + ":"

                saveBlock.remove(saveBlock[blockIndex])
    except:
        print("An error occured")
        exit()

    if newIpv6[-1] == ":" and newIpv6[-2] == ":":
        return newIpv6
    else:
        return newIpv6[:-1]


def test():
    testIpv6 = [
        "2022:0db8:85a3:0000:0000:8a2e:0850:7990",
        "2022:3456:0123:0000:0000:0000:0000:0000",
        "723f:0abe:54ba:0009:0069:0000:0000:5432",
        "2022:9876:0000:0000:dbae:0000:0000:cb15",
        "6044:497b:9e0d:1ecc:eae0:51b5:1d2d:9883",
        "c6e8:8148:a0a3:4d2d:e944:5c6b:c3cd:04f6",
        "3970:cc85:42e9:0c4a:3848:07b0:6b2e:da4d",
        "0ea4:c57f:0b34:2a2f:5f13:ac9d:4d02:016c",
        "465b:598a:9f00:05a9:908d:1973:dfb9:683a",
        "cfa5:283e:6e29:239d:0299:a00c:ca22:5aea",
        "b09d:4038:e7bb:cf19:025d:2733:0678:67c6",
    ]
    rightAnswers = [
        "2022:db8:85a3::8a2e:850:7990",
        "2022:3456:123::",
        "723f:abe:54ba:9:69::5432",
        "2022:9876::dbae:0:0:cb15",
        "6044:497b:9e0d:1ecc:eae0:51b5:1d2d:9883",
        "c6e8:8148:a0a3:4d2d:e944:5c6b:c3cd:4f6",
        "3970:cc85:42e9:c4a:3848:7b0:6b2e:da4d",
        "ea4:c57f:b34:2a2f:5f13:ac9d:4d02:16c",
        "465b:598a:9f00:5a9:908d:1973:dfb9:683a",
        "cfa5:283e:6e29:239d:299:a00c:ca22:5aea",
        "b09d:4038:e7bb:cf19:25d:2733:678:67c6",
    ]
    codeAnswers = []

    for i in testIpv6:
        codeAnswers.append(Ipv6compression(i))

    for i in range(len(testIpv6)):
        if codeAnswers[i] == rightAnswers[i]:
            print("Test " + str(i + 1) + ": Passed")
        else:
            print("Test " + str(i + 1) + ": Failed")
            print("Expected: " + rightAnswers[i])
            print("Got: " + codeAnswers[i])


def main():

    # test()
    ipv6 = input("Enter an IPv6 address: ")
    if len(ipv6) != 39:
        print("Invalid IPv6 address")
        exit()
    else:
        print("The compressed IPv6 address is:", Ipv6compression(ipv6))


if __name__ == "__main__":
    main()
