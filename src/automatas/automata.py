class Automata:

    def read_file(self, file_to_read):
        with open(file_to_read, 'r') as file:
            data = file.read()
            
            for char in data:
                print(char)
