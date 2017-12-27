from array_list import *
from sys import *
from copy import copy

# Song Class: number, name, artist, album
class Song:
    def __init__(self, number, name, artist, album):
        self.number = number
        self.name = name
        self.artist = artist
        self.album = album
    def __eq__(self, other):
        return (type(other) == Song and self.number == other.number and self.name == other.name and \
               self.artist == other.artist and self.album == other.album)

    def __repr__(self):
        return 'Song({!r}, {!r}, {!r}, {!r})'.format(str(self.number), self.name, self.artist, self.album)

    def __str__(self):
        return(self.number + "--" + self.name + "--" + self.artist + "--" + self.album)


# None -> x (int/string)
# menu_boot() function simply prints and takes in the value of the selection option off the menu
def menu_boot():
    print("\nSong Catalog\n   1) Print Catalog\n   2) Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit")
    x = (input("Enter Selection: "))
    return x

#string -> Boolean
# compare_album takes two parameters and compares the values returning True or False
def compare_album(one, two):
    if one.album == two.album:
        if one.artist == two.artist:
            if one.name == two.name:
                if one.number < two.number:
                    return True
            elif al(one.name, two.name):
                return True
        elif al(one.artist, two.artist):
            return True
    elif al(one.album, two.album):
            return True
    return False

#string -> Boolean
# compare_artist takes two parameters and compares the values returning True or False
def compare_artist(one, two):
    if one.artist == two.artist:
        if one.album == two.album:
            if one.name == two.name:
                if compare_number(one, two):
                    return True
            elif al(one.name, two.name):
                return True
        elif al(one.album, two.album):
            return True
    elif al(one.artist, two.artist):
            return True
    return False

#string -> Boolean
# compare_name takes two parameters and compares the values returning True or False
def compare_name(one, two):
    if one.name == two.name:
        if one.album == two.album:
            if one.artist == two.artist:
                if compare_number(one, two):
                    return True
            elif al(one.artist, two.artist):
                return True
        elif al(one.album, two.album):
            return True
    elif al(one.name, two.name):
            return True
    return False

#string -> Boolean
# compare_number takes two parameters and compares the values returning True or False
def compare_number(one, two):
    if int(one.number) == int(two.number):
        if one.album < two.album:
            return True
        if one.artist < two.artist:
            return True
        if one.name < two.name:
            return True
    return int(one.number) < int(two.number)

#string -> Boolean
# compare_album takes two parameters and compares the values returning True or False
def al(c, d):
    return [ord(i) for i in c] < [ord(i) for i in d]


# INPUTS THE CATALOG INTO AN INITIAL LIST
def main():
    sort_val = -1
   #creates a main_list of items Song(num, name, artist, album) in a large list. Returns errors of lines too
    main_list = empty_list()
    sort_list = empty_list()
    num = 0
    index = 0
    line_num = 1
    error_list = []
    try:
        inFile = open(argv[1], 'r')
    except FileNotFoundError:
        print("\n'{}': No such file or directory\n".format(argv[1]))
        exit()

    for line in inFile:
        line1 = line.strip('\n')
        temp = line1.split('--')
        if temp == ['']:
            line_num += 1
            continue
        elif len(temp) < 3 or temp[2] == ['']:
            error_list.append(line_num)
            line_num += 1
            continue
        else:
            temp_song = Song(str(num), temp[0], temp[1], temp[2])
            main_list = add(main_list, index, temp_song)
            sort_list = add(sort_list, index, temp_song)
            line_num += 1
        index += 1
        num += 1


    if len(error_list) >= 1:
        print("Catalog input errors:")
        for i in error_list:
            print("line %d: malformed song information" %(i))

    #CONTROLS MENU ITEMS

    x = menu_boot()
    while x != 'end of file' and x != 'end-of-file' and x != "0":


        #prints the catalog for OPTION 1
        if x == '1':
            foreach(sort_list, print)

        #prints the song selection for OPTION 2
        elif x == '2':
            index = int(input("Enter song number: "))
            if index < length(main_list):
                print('\nSong information ...')
                song_list = get(main_list, index)
                #print(main_list)
                #print(sort_list)
                print("   Number:" + song_list.number)
                print("   Title: " + song_list.name)
                print("   Artist: " + song_list.artist)
                print("   Album: " + song_list.album)
            else:
                print("\n... Invalid song number")

        #Sort Method OPTION 3
        elif x == '3':

            print(main_list)
            print(sort_list)


            print("\nSort songs\n   0) By Number\n   1) By Title\n   2) By Artist\n   3) By Album")
            y = input("Sort by: ")
            if y == '0':
                sort_list = is_sort(sort_list, compare_number)
                sort_val = 1
            elif y == '1':
                sort_list = is_sort(sort_list, compare_name)
                sort_val = 2
            elif y == '2':
                sort_list = is_sort(sort_list, compare_artist)
                sort_val = 3
            elif y == '3':
                sort_list = is_sort(sort_list, compare_album)
                sort_val = 4
            else:
                print("\n... Invalid sort option")

            #print('hi')


            print(main_list)
            print(sort_list)


        #Add Songs OPTION 4
        elif x == '4':
            num_1 = int(length(main_list))
            file_name = input("Enter name of file to load: ")
            index_1 = int(length(main_list))
            line_num_1 = 1
            error_list_1 = []
            #add songs if valid file_name
            try:
                inFile_1 = open(file_name, 'r')

                for line in inFile_1:
                    line1 = line.strip('\n')
                    temp = line1.split('--')
                    if temp == ['']:
                        line_num_1 += 1
                        continue
                    elif len(temp) < 3 or temp[2] == ['']:
                        error_list_1.append(line_num_1)
                        line_num_1 += 1
                        continue
                    else:
                        temp_song = Song(str(num_1), temp[0], temp[1], temp[2])
                        main_list = add(main_list, index_1, temp_song)
                        sort_list = add(sort_list, index_1, temp_song)
                        line_num_1 += 1
                        index_1 += 1
                        num_1 += 1
                print("Option 4")

                #sort_list = main_list

                if len(error_list_1) >= 1:
                    print("\nCatalog input errors:")
                    for i in error_list_1:
                        print("line %d: malformed song information" % (i))
                if int(sort_val) == 1:
                    sort_list = is_sort(sort_list, compare_number)
                elif int(sort_val) == 2:
                    sort_list = is_sort(sort_list, compare_name)
                elif int(sort_val) == 3:
                    sort_list = is_sort(sort_list, compare_artist)
                elif int(sort_val) == 4:
                    sort_list = is_sort(sort_list, compare_album)

            #if invalid file raise exception
            except FileNotFoundError:
                print("\n'{}': No such file or directory".format(file_name))

        #If selection other than 0-4 entered "invalid"
        else:
            print("\nInvalid option")

        x = menu_boot()

    #If 0 or end of file
    try:
        if int(x) == 0:
            exit()
    except ValueError:
        if x == 'end-of-file' or x == 'end of file':
            exit()












if __name__ == '__main__':
    main()