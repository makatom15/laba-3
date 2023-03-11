class Group:

    def __init__(self,age,number_of_students,scholarship,full_name):
        self.__age = age
        self.__number_of_students = number_of_students
        self.__scholarship = scholarship
        self.__full_name = full_name

    def print_private(self):
        print(self.__age,self.__number_of_students,self.__scholarship,self.__full_name)

    def get_age(self) :
        return self.__age
    def set_age(self,age):
        self.__age = age

    def get_number_of_students(self) :
        return self.__number_of_students
    def set_number_of_students(self,number_of_students):
        self.__number_of_students = number_of_students

    def get_scholarship(self):
        return self.__scholarship
    def set_scholarship(self,scholarship):
        self.__scholarship = scholarship

    def get_full_name(self):
        return self.__full_name
    def set_full_name(self, full_name):
        self.__full_name = full_name


    class GroupA:
        def __init__(self, age, number_of_students,
                     scholarship, full_name):
            self._age = age
            self._number_of_students = number_of_students
            self._scholarship = scholarship
            self._full_name = full_name

        @property
        def full_name(self):
            return self._full_name


    #age = property(get_age,set_age)
    #number_of_students = property(get_number_of_students,set_number_of_students)
    #scholarship = property(get_scholarship,set_scholarship)
    #full_name = property(get_full_name,set_full_name)


group_of_welders = Group(20,25,2000,"mak")
group_of_welders.print_private()
group_of_welders.get_age()

