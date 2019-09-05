class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        for element in  self.formula:
            print('Coke has {}!'.format(element))
    def drink(self):
        print('Energy!')
coke = CocaCola()


class TestA:
attr = 1
obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)



class CocaCola:
formula = ['caffeine','sugar','water','soda']
coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐' #􀚠􀭌􀨫􀖺􀪂􀯔
print(coke_for_China.local_logo)



class CocaCola():
formula = ['caffeine','sugar','water','soda']
def __init__(self):
self.local_logo = '可口可乐'
def drink(self): # HERE􀑺
print('Energy!')
coke = CocaCola()
print(coke.local_logo)



class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup'
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))


