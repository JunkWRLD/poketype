type_list = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", 
             "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy", "none"]

fire = [    ("fire", 0.5),
            ("water", 2), 
            ("grass", 0.5),
            ("ice", 0.5),
            ("ground", 2),
            ("bug", 0.5),
            ("rock", 2),
            ("fairy", 0.5),
            ("steel", 0.5) ]

water = [   ("fire", 0.5), 
            ("water", 0.5),
            ("grass", 2),
            ("electric", 2),
            ("ice", 0.5),
            ("steel", 0.5) ]

grass = [   ("fire", 2), 
            ("water", 0.5),
            ("grass", 0.5),
            ("eletric", 0.5),
            ("ice", 2),
            ("poison", 2),
            ("ground", 0.5),
            ("flying", 2),
            ("bug", 2) ]

normal = [  ("fighting", 2), 
            ("ghost", 0) ]

electric = [("electric", 0.5),
            ("ground", 2),
            ("flying", 0.5),
            ("steel", 0.5) ]

ice = [     ("fire", 2), 
            ("ice", 0.5),
            ("fighting", 2),
            ("rock", 2),
            ("steel", 2) ]

fighting = [("flying", 2),
            ("psychic", 2),
            ("bug", 0.5),
            ("rock", 0.5),
            ("dark", 0.5),
            ("fairy", 2) ]

poison = [  ("fighting", 0.5), 
            ("grass", 0.5),
            ("poison", 0.5),
            ("ground", 2),
            ("psychic", 2),
            ("bug", 0.5),
            ("fairy", 0.5) ]

ground = [  ("water", 2), 
            ("grass", 2),
            ("electric", 0),
            ("ice", 2),
            ("poison", 0.5),
            ("rock", 0.5) ]

flying = [  ("grass", 0.5), 
            ("electric", 2),
            ("ice", 2),
            ("fighting", 0.5),
            ("ground", 0),
            ("bug", 0.5),
            ("rock", 2) ]

psychic = [ ("fighting", 0.5), 
            ("bug", 2),
            ("psychic", 0.5),
            ("dark", 2),
            ("ghost", 2) ]

bug = [     ("fire", 2), 
            ("grass", 0.5),
            ("fighting", 0.5),
            ("ground", 0.5),
            ("flying", 2),
            ("rock", 2) ]

rock = [    ("normal", 0.5),
            ("fire", 2), 
            ("water", 2),
            ("grass", 2),
            ("fighting", 2),
            ("poison", 0.5),
            ("ground", 2),
            ("flying", 0.5),
            ("steel", 2) ]

ghost = [   ("normal", 0), 
            ("fighting", 0),
            ("poison", 0.5),
            ("bug", 0.5),
            ("ghost", 2),
            ("dark", 2) ]

dragon = [  ("fire", 0.5),
            ("water", 0.5),
            ("grass", 0.5),
            ("electric", 0.5),
            ("dragon", 2), 
            ("ice", 2),
            ("fairy", 2) ]

dark = [    ("fighting", 2), 
            ("bug", 2),
            ("psychic", 0),
            ("ghost", 0.5),
            ("dark", 0.5),
            ("fairy", 2) ]

steel = [   ("fire", 2), 
            ("normal", 0.5),
            ("grass", 0.5),
            ("ice", 0.5),
            ("fighting", 2),
            ("poison", 0),
            ("ground", 2),
            ("flying", 0.5),
            ("psychic", 0.5),
            ("bug", 0.5),
            ("rock", 0.5),
            ("dragon", 0.5),
            ("steel", 0.5),
            ("fairy", 0.5) ]

fairy = [   ("fighting", 0.5),
            ("poison", 2),
            ("dragon", 0),
            ("dark", 0.5),
            ("steel", 2)]

type_effectiveness = {
    "normal": normal,
    "fire": fire,
    "water": water,
    "grass": grass,
    "electric": electric,
    "ice": ice,
    "fighting": fighting,
    "poison": poison,
    "ground": ground,
    "flying": flying,
    "psychic": psychic,
    "bug": bug,
    "rock": rock,
    "ghost": ghost,
    "dragon": dragon,
    "dark": dark,
    "steel": steel,
    "fairy": fairy
}



def effectiveness(type1, type2=None):
    super_list = []
    not_very_list = []
    immune_list = []

    count_map = {}

    for i in type1:
        count_map[i[0]] = count_map.get(i[0], 1) * i[1]
    
    if type2 != None:
        for j in type2:
            count_map[j[0]] = count_map.get(j[0], 1) * j[1]
    
    quad_eff_list = []
    quad_resist_list = []

    for type_name, multiplier in count_map.items():
        if multiplier == 0:
            immune_list.append(type_name)
        elif multiplier >= 4:
            quad_eff_list.append(type_name)
        elif multiplier > 1:
            super_list.append(type_name)
        elif 0 < multiplier < 0.25:
            quad_resist_list.append(type_name)
        elif multiplier < 1:
            not_very_list.append(type_name)

    print(f"4x effective against you: {quad_eff_list}")
    print(f"Super effective against you: {super_list}")
    print(f"Not very effective against you: {not_very_list}")
    print(f"1/4x effective against you: {quad_resist_list}")
    print(f"No effect against you: {immune_list}")


# def effectiveness(type1, type2=None):
#     super_list = []
#     not_very_list = []
#     immune_list = []
#     for i in type1:
#         if i[1] > 1:
#             super_list.append(i[0])
#         elif i[1] > 0:
#             not_very_list.append(i[0])
#         else:
#             immune_list.append(i[0])
#     if type2 != None:
#         for j in type2:
#             if j[1] > 1:
#                 super_list.append(j[0])
#             elif j[1] > 0:
#                 not_very_list.append(j[0])
#             else:
#                 immune_list.append(j[0])
#         super_list, not_very_list, immune_list, quad_eff_list, quad_resist_list = logic(super_list, not_very_list, immune_list)

#     print(f"4x effective against you: {quad_eff_list}")
#     print(f"Super effective against you: {super_list}")
#     print(f"Not very effective against you: {not_very_list}")
#     print(f"1/4x effective against you: {quad_resist_list}")
#     print(f"No effect against you: {immune_list}")
    

# def logic(super_list, not_very_list, immune_list):
#     quad_eff_list = []
#     quad_resist_list = []
#     count = 0
#     for type in immune_list:
#         if type in super_list:
#             super_list.remove(type)
#         if type in not_very_list:
#             not_very_list.remove(type)
#     for type in not_very_list:
#         count += 1
#         if type in super_list:
#             not_very_list.remove(type)
#             super_list.remove(type)
#         if count > 1:
#             quad_resist_list.append(type)
#             not_very_list.remove(type)
#     for type in super_list:
#         count += 1
#         if count > 1:
#             quad_eff_list.append(type)
#             super_list.remove(type)
        

def main():
    
    x = 1
    while x == 1:
        type1 = input("attacking pokemon type 1: ")
        if type1 in type_list:
            x = 0
    while x == 0:
        type2 = input("attacking pokemon type 2: ")
        if type2 in type_list:
            x = 2

    effectiveness(type_effectiveness[type1], type_effectiveness[type2])


main()