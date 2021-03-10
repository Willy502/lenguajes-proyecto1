class MenuAutomata:

    def read_file(self, file_to_read):
        file = open(file_to_read, 'r')
        end_reached = False
        while (end_reached != True):
            try:
                print(file.read())
            finally:
                file.close()
                end_reached = True