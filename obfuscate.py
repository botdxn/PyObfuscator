import string
import random


class Obfuscate:
    def __init__(self, file):
        self.file = file
        with open(self.file, "r") as input_file:
            self.code_data = input_file.readlines()
            self.code_data = [line.replace("\n", "") for line in self.code_data]

    ## function to generate random letters from ascii (lower/upper)
    def generate_strings(self):
        return "".join(
            random.choice(string.ascii_letters) for i in range(random.randint(8, 15))
        )

    ## function to convert to binary
    def to_binary(self, string):
        return "".join(format(ord(i), "08b") for i in string)

    ## loading .py file
    # def load_file(self):
    #     with open(self.file, "r") as input_file:
    #         self.code_data = input_file.readlines()
    #         self.code_data = [line.replace("\n", "") for line in self.code_data]
    #         return self.code_data

    ## search, save and obfuscate function names
    def obfuscate_func_names(self, binary_obfuscation=False):

        list_of_func_names = []
        list_of_obfuscated_func_names = []
        for i, line in enumerate(self.code_data):
            elements = line.split(" ")
            for j, elem in enumerate(elements):
                if elem == "def" and elements[j + 1] != "__init__(self,":
                    func_name = elements[j + 1].split("(")
                    list_of_func_names.append(func_name[0])
                    list_of_obfuscated_func_names.append(self.generate_strings())
        code_string = "".join(self.code_data)

        if len(list_of_func_names) > 0:
            for k, func in enumerate(list_of_func_names):
                for i, line in enumerate(self.code_data):
                    line_string = "".join(line)
                    if func in line_string:
                        if binary_obfuscation == False:
                            line_string.replace(func, list_of_obfuscated_func_names[k])
                            self.code_data[i] = line_string.replace(
                                func, list_of_obfuscated_func_names[k]
                            )

                        elif binary_obfuscation == True:
                            line_string.replace(func, self.to_binary(func))
                            print(self.to_binary(func))
                            self.code_data[i] = line_string.replace(
                                func, list_of_obfuscated_func_names[k]
                            )

        with open("obfuscated_" + self.file, "w") as output:
            for line in self.code_data:
                output.write(line + "\n")

        return self.code_data

    ## search, save and obfuscate variable names
    def obfuscate_var_names(self):
        list_of_var_names = []
        list_of_obfuscated_var_names = []

        for i, line in enumerate(self.code_data):
            elements = line.split(" ")
            for j, elem in enumerate(elements):
                if elem == "def":
                    line = line.replace(":", ",")
                    line = line.replace("(", ",")
                    line = line.replace(")", ",")
                    line = line.replace(" ", ",")
                    try:
                        list_of_var_names.append(line[line.index("self") :])
                    except:
                        pass

        list_of_var_names = [ele.split(",") for ele in list_of_var_names]

        for sublist in list_of_var_names:
            while "self" in sublist:
                sublist.remove("self")

        list_of_var_names = [item for subitem in list_of_var_names for item in subitem]
        while "" in list_of_var_names:
            list_of_var_names.remove("")

        for i, line in enumerate(self.code_data):
            elements = line.split(" ")
            for j, elem in enumerate(elements):
                if elem == "=" and elements[j + 1] != "=" and elements[j - 1] != "=":
                    list_of_var_names.append(elements[: elements.index("=")][-1])

        list_of_obfuscated_var_names = [
            self.generate_strings() for _ in range(1, len(list_of_var_names) + 1)
        ]

        if len(list_of_var_names) > 0:
            for k, func in enumerate(list_of_var_names):
                for i, line in enumerate(self.code_data):
                    line_string = "".join(line)
                    if func in line_string:
                        line_string.replace(func, list_of_obfuscated_var_names[k])
                        self.code_data[i] = line_string.replace(
                            func, list_of_obfuscated_var_names[k]
                        )

        with open("obfuscated_" + self.file, "w") as output:
            for line in self.code_data:
                output.write(line + "\n")

        return self.code_data


if __name__ == "__main__":
    test = Obfuscate("main.py")
    #test.load_file()
    test.obfuscate_func_names()
    test.obfuscate_var_names()
