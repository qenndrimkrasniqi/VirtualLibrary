class Library:
    def __init__(self, source_path, name, location, floors):
        self.source_path = source_path
        self.name = name
        self.location = location
        self.floors = list(floors)

    def __str__(self):
        return self.name

    def get_floors(self):
        list1 = os.listdir(source_path1)
        print(list1)
        for i in list1:
            print(i)


source_path1 = ('../Data/Hivzi Sylejmani - Prishtinë')
basename = os.path.basename(source_path1)
name = basename.split('-')[0].strip()
print(name)

