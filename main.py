from Contact import Contact
from Parser import Parser
from sys import argv


if __name__ == "__main__":
    p = Parser()  # Init parser
    if len(argv) == 1:  # Init the file name to be parsed
        file_name = 'ex_v7'
    else:
        file_name = argv[1]

    att = {'86B7': 'first', '9E60': 'last', '5159': 'phone', 'D812': 'time', '6704': 'image'}
    list_att = ['phone', 'time']

    attributes, identifiers = p.parse(file_name, att, list_att)  # Let the parsing begin
    contacts = []  # Init list of contacts

    for id in identifiers:  # for each ID --> Create a contact with its attribute values
        first = attributes['first'][id]
        last = attributes['last'][id]
        phones = attributes['phone'][id]
        time = attributes['time'][id]
        img = attributes['image'][id]

        contacts.append(Contact(first, last, phones, time, img))  # Add to list

    for contact in contacts:  # Print all contacts information
        print contact
        # contact.save_image()  # Optional --> save_image() will save the image ('contact name.jpg')
        # contact.show_image()  # Optional --> show_image() will save (if not yet saved) and than open the image

