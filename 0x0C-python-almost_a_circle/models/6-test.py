def display(self):
        """prints a # rectangle"""
        for i in range(0, self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")
        if self.__width == 0 or self.height == 0:
            print("")
