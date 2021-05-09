""" convert text file to C parallel arrays """
def main():
    try:
        datafile = open("states-and-capitals.txt","r")
    except:
        print("unable to open input file")
        return
    # tab-delimited: state, abbreviation, year joined, capital
    state = []
    postal = []
    joined = []
    capital = []
    another = []
    for line in datafile:
        # skip the first line (credit)
        if line[0] == "#":
            continue
        data = line.split('\t')
        state.append(data[0])
        postal.append(data[1])
        joined.append(data[2])
        capital.append(data[3])
        another.append(data[4])
    datafile.close()

    # print the array definitions
    arrayState = 'string states[] = {""'
    for s in state:
        arrayState += ',"'+s.strip()+'"'
    arrayState += '};'

    arrayPostal = 'string postal[] = {""'
    for p in postal:
        arrayPostal += ',"'+p.strip()+'"'
    arrayPostal += '};'

    arrayJoined = 'int joined[] = {0'
    for j in joined:
        arrayJoined += ','+j.strip()+''
    arrayJoined += '};'

    arrayCapital = 'string capital[] = {""'
    for c in capital:
        arrayCapital += ',"'+c.strip()+'"'
    arrayCapital += '};'
    
    arrayAnother = 'string another[] = {""'
    for a in another:
        arrayAnother += ',"'+a.strip()+'"'
    arrayAnother += '};'

    print(arrayState)
    print(arrayPostal)
    print(arrayJoined)
    print(arrayCapital)
    print(arrayAnother)
    
if __name__ == "__main__":
    main()
