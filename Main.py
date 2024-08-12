from Options.Colors import Colors
from Options.Connection import Connection
from Options.Create import Create
from Options.Delete import Delete
import platform
import os

class Menu:
    def __init__(self) -> None:
        self.message = ''

    def options(self):
        self.clearConsole()
        print(f'{Colors.GRAY.value}╔══════════════════════════════════════╗')
        print(f'║ {Colors.WHITE.value}Practica 1 - Seminario De Sistemas 2 {Colors.GRAY.value}║')
        print(f'╠══════════════════════════════════════╣')
        print(f'║            {Colors.WHITE.value}Menu Principal            {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}1. Borrar Modelo              {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}2. Crear Modelo               {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}3. Extraer Información        {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}4. Cargar Información         {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}5. Consultas                  {Colors.GRAY.value}║')
        print(f'║        {Colors.WHITE.value}6. Salir                      {Colors.GRAY.value}║')
        print(f'╚══════════════════════════════════════╝{Colors.WHITE.value}')
        if self.message != '':
            print(self.message)
            self.message = ''

    def readInputKey(self) -> int:
        option = input('\n  Opcion: ')
        if option.isdigit():
            if 1 <= int(option) <= 6:
                return int(option)
            self.message = f'{Colors.RED.value}  Solo se permiten números [1-6]{Colors.WHITE.value}'
            return 0
        self.message = f'{Colors.RED.value}  Solo se permiten números{Colors.WHITE.value}'
        return 0

    def chooseOption(self):
        self.options()
        return self.readInputKey()

    def clearConsole(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

class Practica1:
    def __init__(self):
        self.menu = Menu()
        self.conn = Connection()
        self.create = Create(self.conn)
        self.delete = Delete(self.conn)

    def run(self):
        self.menu.clearConsole()
        option = 0
        while(option != 6):
            option = self.menu.chooseOption()
            match option:
                case 1:
                    print()
                    self.menu.message = self.delete.start()
                case 2:
                    print()
                    self.menu.message = self.create.start()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case _:
                    pass
        print(f'  {Colors.GREEN.value}¡Finalizado!{Colors.WHITE.value}')

Practica1().run()