import sys

original_stdout = sys.stdout

with open('filename.txt', 'w') as f:
    sys.stdout = f

    with open("aew.txt", encoding="utf8") as filler:
        file_content = filler.read().strip('/"')
        


    overall = file_content.count("seatstyles")
    available = file_content.count("seatstyles__Seat-sc-1efhiok-0 bMPatX")
    grey = file_content.count("seatstyles__Seat-sc-1efhiok-0 hBuynS")
    resale = file_content.count("seatstyles__CustomSeat-sc-1efhiok-1 ibzkpR")
    VIP = file_content.count("seatstyles__CustomSeat-sc-1efhiok-1 ikViJw")
    checksum = available + grey + resale + VIP




    print("All seats", overall)
    print("Available tickets: ", available)
    print("Grey seat (sold or not open): ", grey)
    print("Resale: ", resale)
    print("VIP Tickets: ", VIP)
    print("Checksum: ", checksum)
    print("__________________________")





    sections = file_content.split("data-section-name")
    i = 1
    while i < len(sections):
        print ("Section ", sections[i] [2:5] )
        print ("Overall Seats: ", sections[i].count("svg__seat"))
        print ("Available (Blue) Seats: ", sections[i].count("seatstyles__Seat-sc-1efhiok-0 bMPatX"))
        print ("Grey (Sold or not available) Seats: ", sections[i].count("seatstyles__Seat-sc-1efhiok-0 hBuynS"))
        print ("Resale Seats: ", sections[i].count("seatstyles__CustomSeat-sc-1efhiok-1 ibzkpR"))
        print ("VIP Seats: ", sections[i].count("seatstyles__CustomSeat-sc-1efhiok-1 ikViJw"))
        print ("_________________________________________________")
        i = i + 1

f.close()