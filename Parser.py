from collections import defaultdict


class Parser:
    def __init__(self, id_len=4, info_len=5):
        self.id_len = id_len  # Number of characters that define the unique identifier for each contact
        self.info_len = info_len  # Number of characters that define the length of the information

    def parse(self, file_name, att, list_att):
        with open(file_name, 'r') as f:  # Reading lines from file
            lines = f.readlines()

        attributes_dic = {}
        identifiers = set()

        for line in lines:
            attribute_name = att[line[:self.id_len]]  # Get current line identifier
            index = self.id_len  # Starting index
            line_length = len(line.strip())  # Length of line without trailing spaces

            if attribute_name not in attributes_dic:
                attributes_dic[attribute_name] = defaultdict(lambda: [] if attribute_name in list_att else '')

            while index < line_length:
                contact_id = line[index:index + self.id_len]  # get current contact identifier
                index += self.id_len
                identifiers.add(contact_id)

                info_len = int(line[index:index + self.info_len], 16)  # How many characters we need to read
                index += self.info_len

                if attribute_name in list_att:
                    attributes_dic[attribute_name][contact_id].append(
                        line[index:index + info_len])  # Append phone number
                else:
                    attributes_dic[attribute_name][contact_id] = line[index:index + info_len]

                index += info_len

        return attributes_dic, identifiers
