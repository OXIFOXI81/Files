import os
# 2 задание

def get_shop_list_by_dishes(dishes, person_count):
     shoping_list={}
     asw=0
     for dish_in in dishes:
       for dish,ingr in cook_book.items():
           if dish==dish_in:
               for elem in ingr:
                   ing_var=elem['ingredient_name']
                   if ing_var not in  shoping_list.items():
                     ingr_list = []
                     ingr_list.append({
                         'measure': elem['measure'],
                         'quantity': int(elem['quantity'])*person_count
                      })
                   shoping_list[ing_var]=ingr_list
               else:
                    shoping_list[ing_var][0]['quantity'] =int(shoping_list[ing_var][0]['quantity'])+ int(elem['quantity']) * person_count
     for ingr in shoping_list:
         print(ingr,shoping_list[ingr])

# Задание 1

with open (os.path.join(os.getcwd(), 'recipes.txt'),'r',encoding='utf-8') as f:
    cook_book={}
    for dish in f:
        ingr_count=int(f.readline())
        ingr_list=[]
        for i in range(ingr_count):
            ingr_name,qty,ed =f.readline().strip().split('|')
            ingr_list.append({
                'ingredient_name': ingr_name,
                'quantity': qty,
                'measure': ed
            })
        f.readline()
        cook_book[dish.strip()]=  ingr_list

for key, value in cook_book.items():
    print(f'\n{key}')

    for v in value:
      print(f'{v}')
    print('\n')

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

# Задание 3

dict_={}
full_path=os.path.join(os.getcwd(),'TXT')
for filename in os.listdir(full_path):
    if filename.endswith("txt"):
        with open(os.path.join(os.getcwd(),'TXT', filename),'r',encoding='utf-8') as f:
           text = f.readlines()
           len_ = len(text)

           dict_[filename] =  [len_,text]
#dict_sorted= dict(sorted(dict_.items(), key=lambda item: item[1]))

full_path=os.path.join(os.getcwd(),'result.txt')
print(full_path)
with open(os.path.join(os.getcwd(),'result.txt'), 'w', encoding='utf-8') as output_file:
   for name_file,kstr in dict(sorted(dict_.items(), key=lambda item: item[1])).items():
      output_file.write(f'{name_file}\n{kstr[0]}\n')
      for v in kstr[1]:
        output_file.write(f'{v}')
      output_file.write(f'\n')

