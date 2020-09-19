# I always have to write custom code to pull items off of a text document list, so this will be a nice little
# auto list creator "library" to return each individual line of a text document as it's own element in a list.
# Written by James Scheiber, 4am 9/19/2020 :)

class Lister:
    def __init__(self, filePath = "list.txt"):
        self.filePath = filePath

    def returnList(self):
        list = []
        f = None

        # Tries to iterate through the file and add each new line to the list variable created above
        try:
            f = open(self.filePath, 'r')
            lines = f.readlines()
            for line in lines:
                if not line.startswith(' ') and not line.startswith('\n'):
                    list.append(line)
            f.close()

        # Will throw in event of file not existing or being able to be found
        except FileNotFoundError:
            print("File did not exist, check that first.")
            raise

        except:
            print("File is okay but something else is causing problems. :/ sorry bro")
            raise

        finally:
            # Safety shutdown as last thing done
            if f != None:
                f.close()

        # Finally returns the list to the original call
        return(list)
