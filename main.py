class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.weight += 1
        return 'покормили'


class MilkGiving(Animals):

    class_action = "Можно доить"
    def get_milk(self):
        print('получено молоко')
        return 1

class EggGiving(Animals):
    class_action = "Можно собрать яйца"
    def get_egg(self):
        print('получено яйцо')
        return 1

class WoolGiving(Animals):
    class_action = "можно стрич"
    def get_wool(self):
        print('получена шерсть')
        return 1

class Cow(MilkGiving):
    type = 'Корова'
    voice = 'Му - Му'


class Goat(MilkGiving):
    type = 'Коза'
    voice = 'Ме - Ме'


class Duck(EggGiving):
    type = 'Утка'
    voice = 'Кря - Кря'


class Goose(EggGiving):
    type = 'Гусь'
    voice = 'Га - Га'


class Chicken(EggGiving):
    type = 'Курица'
    voice = 'Ко - Ко'


class Sheep(WoolGiving):
    type = 'Овца'
    voice = 'Бе - Бе'

store = {'milk':0, 'egg':0, 'wool':0}
farm = [Goose('Серый', 4),
        Goose('Белый', 5),
        Cow('Манька', 200),
        Sheep('Барашек', 10),
        Sheep('Кудрявый', 12),
        Chicken('Ко-Ко', 2),
        Chicken('Кукареку', 1),
        Goat('Рога', 30),
        Goat('Копыта', 25),
        Duck('Кряква', 3)]

def collect_egg(farm):
  user_input = input('имя животного у которого собрать яйца: ')
  for animal in farm:
    if animal.name != user_input:
      continue
    else:
     if animal.class_action == "Можно собрать яйца":
         EggGiving.get_egg(animal)
         store['egg'] = store.get('egg') + 1
     elif animal.class_action != "Можно собрать яйца":
      return 'это животное не несет яиц'
  return store

def collect_milk(farm):
  user_input = input('имя животного которое будем доить: ')
  for animal in farm:
    if animal.name != user_input:
      continue
    else:
     if animal.class_action == "Можно доить":
         MilkGiving.get_milk(animal)
         store['milk'] = store.get('milk') + 1
     elif animal.class_action != "Можно доить":
      return 'это животное не дает молока'
  return store

def collect_wool(farm):
  user_input = input('имя животного для стрижки: ')
  for animal in farm:
    if animal.name != user_input:
      continue
    else:
     if animal.class_action == "Можно стрич":
        WoolGiving.get_wool(animal)
        store['wool'] = store.get('wool') + 1
     elif animal.class_action != "Можно стрич":
      return 'это животное нельзя стрич'
  return store

def get_feed(farm):
  user_input = input('кого будем кормить: ')
  for animal in farm:
   if animal.name != user_input:
     continue
   else:
     Animals.feed(animal)
     print (f'вес животного {animal.name }: {animal.weight}')
   return 'покормили'

def weight(farm):
    weight = 0
    for animal in farm:
        weight += animal.weight
    return weight

def heaviest(farm):
    max_weight = 0
    name = ' '
    for animal in farm:
        if animal.weight > max_weight:
            max_weight = animal.weight
            name = animal.name
        else:
            continue
    return print(f'{name}: {max_weight} кг')

def main():
    help = f'СПИСОК КОМАНД: \nmilk - команда, которая позволяет подоить животное. \negg – команда, которая позволяет '\
           f'собрать яйца. \nwool - команда, которая позволяет собрать шерсть. \nfeed - команда, которая позволяет ' \
           f'накормить животное. \nweight – команда, которая выводит общий вес обитателей фермы. \nheaviest – команда, которая  ' \
           f'выводит самого тяжелого обитателя фермы. \nstore – команда, которая выводит список продуктов на складе. ' \
           f'\nfarm - команда, которая выводит данные о всех обитателях фермы. \nhelp - команда для вызова справки. ' \
           f'\nquit - команда для выхода из приложения'
    print(help)
    while True:
     user_action = input('\nВведите команду: ')
     if user_action == 'milk':
      print(collect_milk(farm))
     elif user_action == 'egg':
      print(collect_egg(farm))
     elif user_action == 'wool':
      print(collect_wool(farm))
     elif user_action == 'feed':
       print(get_feed(farm))
     elif user_action == 'weight':
        print(weight(farm))
     elif user_action == 'heaviest':
        print(heaviest(farm))
     elif user_action == 'store':
        print(store.items())
     elif user_action == 'farm':
        for animal in farm:
          print(f'{animal.type} "{animal.name}", говорит {animal.voice}, вес животного:{animal.weight}, {animal.class_action}')
     elif user_action == 'help':
        print(help)
     elif user_action == 'quit':
        print('\nДо свидания!')
        break
     else:
         print('\nтакой команды нет в списке.')
main()

