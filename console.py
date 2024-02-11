#!/usr/bin/python3
"""
A command line interpreter for AirBnB clone
"""

import cmd
import models
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """A console class for the AirBnB-Clone project"""

    prompt: str = '(hbnb)'

    __class_lst = {
        BaseModel.__name__: BaseModel,
        State.__name__: State,
        City.__name__: City,
        Review.__name__: Review,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        User.__name__: User
    }

    __class_funcs = ["all", "count", "show", "destroy", "update"]

    @staticmethod
    def parse(arg, id=" "):
        """
        Gets list that parsed arguments from the string
        """

        list_argm = arg.split(id)
        nlist_argm = []

        for m in list_argm:
            if m != '':
                nlist_argm.append(m)
        return nlist_argm

    def do_quit(self, arg):
        """Closes and exits the program"""
        return True

    def help_quit(self):
        """Prints help for the quit command"""

        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True

    def do_create(self, arg):
        """
            This makes a new instance of BaseModel
            the saves it to the JSON file and prints
            the id.
        """

        lst_argm = HBNBCommand.parse(arg)

        if len(lst_argm) == 0:
            print("** class name missing **")
            return False

        if len(lst_argm) > 1:
            print("** to many arguments **")
            return False

        if (lst_argm[0] in HBNBCommand.__class_lst.keys()):
            new_obj = HBNBCommand.__class_lst[lst_argm[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
            prints the create function's Help info
        """
        print("""Creats a new instance of the first argument
              stores it in the JSON file and prints its id""")

    def do_show(self, arg):
        """
            based on the class name and id it
            Prints the string representation of an instance .
        """
        lst_argm = HBNBCommand.parse(arg)
        db = models.storage.all()

        if not len(lst_argm):
            print("** class name missing **")
        elif (lst_argm[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")

        elif len(lst_argm) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(lst_argm[0], lst_argm[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(lst_argm[0], lst_argm[1])])

    def help_show(self):
        """
            Prints Help for for the creat function
        """
        print("""Prints the string representation of an instance based
            on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234
            """)

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234
        """

        lst_argm = HBNBCommand.parse(arg)
        models.storage.reload()
        db = models.storage.all()

        if not len(lst_argm):
            print("** class name missing **")
        elif (lst_argm[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        elif len(lst_argm) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(lst_argm[0], lst_argm[1]) not in db:
            print("** no instance found **")
        else:
            del db["{}.{}".format(lst_argm[0], lst_argm[1])]
            models.storage.save()

    def help_destroy(self):
        """
            Prints Help for the destroy function
        """
        print("""Deletes an instance based on the class name and id
              (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234""")

    def do_all(self, arg):
        """
            Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all
        """
        list_argm = HBNBCommand.parse(arg)
        if len(list_argm) > 0 and list_argm[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            obj_a = []
            for obj in models.storage.all().values():
                if len(list_argm) > 0 and list_argm[0] == obj.__class__.__name__:
                    obj_a.append(obj.__str__())
                elif len(list_argm) == 0:
                    obj_a.append(obj.__str__())
            print(obj_a)

    def help_all(self):
        """
            prints help for the all function
        """
        print("""Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all""")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
        """
        list_argm = HBNBCommand.parse(arg)
        objdict = models.storage.all()

        if len(list_argm) == 0:
            print("** class name missing **")
            return False
        if list_argm[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
            return False

        if len(list_argm) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_argm[0], list_argm[1]) not in objdict.keys():
            print("** no instance found **")
            return False

        if len(list_argm) == 2:
            print("** attribute name missing **")
            return False
        if len(list_argm) == 3:
            try:
                type(eval(list_argm[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(list_argm) == 4:
            obj = objdict["{}.{}".format(list_argm[0], list_argm[1])]

            if list_argm[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[list_argm[2]])
                obj.__dict__[list_argm[2]] = valtype(list_argm[3])
            else:
                obj.__dict__[list_argm[2]] = list_argm[3]

        elif type(eval(list_argm[2])) == dict:
            obj = objdict["{}.{}".format(list_argm[0], list_argm[1])]
            for k, v in eval(list_argm[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v

        models.storage.save()

    def help_update(self):
        """
            prints Help for the update function
        """
        print(
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234
                      email "aibnb@holbertonschool.com""")

    def emptyline(self):
        """
            Does nothing if Empty line + enter is inserted.
            Used for overriding the emptyline function
        """
        pass

    def do_count(self, arg):
        """
            Prnits the number of elements inside the FileStorage that
            are of instances of cls
        """
        list_argm = HBNBCommand.parse(arg)
        if len(list_argm) > 0 and list_argm[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            obj_a = []
            for obj in models.storage.all().values():
                if len(list_argm) > 0 and list_argm[0] == obj.__class__.__name__:
                    obj_a.append(obj.__str__())
                elif len(list_argm) == 0:
                    obj_a.append(obj.__str__())
            print(len(obj_a))



if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()