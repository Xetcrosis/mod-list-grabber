import webbrowser

# blah\fallout4__19-02-2024_15-45-04.txt

file_location = input("Enter the txt file to load: ")

file = open(file_location, 'r')
# if link[0] == 'h':
#     webbrowser.open(link)
# else:
def parse_file():
    for line in file:
        link_idx = line.rfind("[link]")
        link_idx += 7
        link = line[link_idx:]
