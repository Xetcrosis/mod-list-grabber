import webbrowser
# blah\fallout4__19-02-2024_15-45-04.txt


def parse_file(file):  # -> tuple[list, list]:
    link_list = []
    non_link_list = []
    for line in file:
        link_idx = line.rfind("[link]")
        fileN_idx = line.rfind("[Filename]")
        file_name = line[0:fileN_idx]
        link_idx += 7
        link = line[link_idx:]
        if link[0] == 'h' and link[1] == 't':
            link_list.append(link[:-2])
        else:
            non_link_list.append(file_name)
    return (link_list, non_link_list)


def display_tuple(tuple):
    for lis in links_tuple:
        print("-------------------------------")
        for link in lis:
            print(link)


file_location = input("Enter the txt file to load: ")
# file_location = "./blah/test.txt"

file = open(file_location, 'r')

links_tuple = parse_file(file)

display_tuple(links_tuple)
