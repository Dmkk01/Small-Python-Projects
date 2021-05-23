def main():
    filename = input("Enter the name of the file to be read:\n")
    try:
        file = open(filename, "r")
        
        part = file.readline()
        part = part.split(',')
        sizeX = int(part[0])
        sizeY = int(part[1])
        fullArray = zeros = [ ['0'] * sizeX for _ in range(sizeY)]

        for line in file:
            a = line.split(',')
            try:
                partX = int(a[0])
                partY = int(a[1])
                fullArray[partY][partX] = '1'
            except:
                print('Error in line: "{}"'.format(line))
            
        for r in fullArray:
            for c in r:
                if c == '1':
                    print(' ',end = "")
                else:
                    print('H',end = "")
            print()
        file.close()
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))
    except (ValueError, IndexError):
        print("Image dimensions are incorrect or the file '{:s}' is empty. Program ends.".format(filename))
        
main()