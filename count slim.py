import sys

original_stdout = sys.stdout

with open('slim.txt', 'w') as f:
    sys.stdout = f

    with open("aew.txt", encoding="utf8") as filler:
        file_content = filler.read().strip('/"')
        


    overall = file_content.count("seatstyles")
    available = file_content.count("seatstyles__Seat-sc-1efhiok-0 bMPatX")
    grey = file_content.count("seatstyles__Seat-sc-1efhiok-0 hBuynS")
    resale = file_content.count("seatstyles__CustomSeat-sc-1efhiok-1 ibzkpR")
    VIP = file_content.count("seatstyles__CustomSeat-sc-1efhiok-1 ikViJw")
    checksum = available + grey + resale + VIP




    print(overall)
    print(available)
    print(grey)
    print(resale)
    print(VIP)
    print(checksum)
    #print("__________________________")





    sections = file_content.split("data-section-name")
    i = 1
    while i < len(sections):
        print (sections[i] [2:5] )
        print (sections[i].count("svg__seat"))
        print (sections[i].count("seatstyles__Seat-sc-1efhiok-0 bMPatX"))
        print (sections[i].count("seatstyles__Seat-sc-1efhiok-0 hBuynS"))
        print (sections[i].count("seatstyles__CustomSeat-sc-1efhiok-1 ibzkpR"))
        print (sections[i].count("seatstyles__CustomSeat-sc-1efhiok-1 ikViJw"))
        #print ("_________________________________________________")
        i = i + 1

f.close()