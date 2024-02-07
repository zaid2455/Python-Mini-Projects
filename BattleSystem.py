import random



class Weapon:
    
    def __init__(self, weapon, damage):
        self.weapon = weapon
        self.dmg = damage

    def __str__(self):
        return self.weapon
    
class Spells:
    def __init__(self, spell, damage):
        self.spell = spell
        self.damage = damage
    
    def __str__(self):
        return self.spell
    
class Potion:

    def __init__(self, name, type, multiplier, duration):
        self.name = name
        self.type = type
        self.buff = multiplier
        self.duration = duration

    def __str__(self):
        return self.name
    
class Character():

    def __init__(self, name, hitpoints, weapon, spells, inventory, damagebuff=1, runchance = 2):
        self.name = name
        self.hp = hitpoints
        self.wpn = weapon
        self.spells = spells
        self.inv = inventory
        self.defense = False
        self.dmgbuff = damagebuff
        self.rchance = runchance
        self.dead = False
        self.buff_duration = 0
        

    def reset_buffs(self):
        if self.buff_duration > 0:
            self.buff_duration -= 1
            if self.buff_duration == 0:
                print(f'{self.name}\'s buff has worn off!')
                self.dmgbuff = 1
        else:
            pass

        self.defense = False

    def check_status(self):
        if self.hp <= 0:
            self.dead = True


    def attack(self, target):
        if target.defense:
            attack_power = self.wpn.dmg * 0.6
        else:
            attack_power = self.wpn.dmg 
        attack_power = round(attack_power * self.dmgbuff)

        target.hp -= attack_power
        print(f'{self.name} attacks {target.name} for {attack_power} damage with {self.wpn}!')
        if target.hp <= 0:
            print(f'{target.name} has 0 hitpoints remaining!\n')
            print(f'{target.name} has died!')
        else:
            print(f'{target.name} has {target.hp} hitpoints remaining!\n')

    def use_spell(self, target):
        for num, spell in enumerate(self.spells, start=1):
            print(f'{num}: {spell}')
        spellnum = int(input('Which spell do you want to use?'))
        if spellnum in range(1, len(self.spells) + 1):
            spellused = self.spells[spellnum - 1]
            target.hp -= spellused.damage 
        print(f'{self.name} attacks {target.name} for {spellused.damage} damage with {spellused.spell}!')
        if target.hp <= 0:
            print(f'{target.name} has 0 hitpoints remaining!\n')
            print(f'{target.name} has died!')
        else:
            print(f'{target.name} has {target.hp} hitpoints remaining!\n')
            
            
    def defend(self):
        self.defense = True
        print(f'{self.name} is now in a defensive stance\n')

    def auto_item(self, item_type):
        for item in self.inv:
            if item.type == item_type:
                
                if item_type == 'HP':
                    self.hp += item.buff
                elif item_type == 'DMG':
                    self.dmgbuff *= item.buff
                    self.buff_duration = item.duration
                print(f'{self.name} has used {item.name}!\n')

                self.inv.pop(self.inv.index(item))






    def use_item(self):
        if self.inv:
            for num, item in enumerate(self.inv, start=1):
                print(f'{num}: {item}')
            itemnum = int(input('Which item do you want to use?'))
            if itemnum in range(1, len(self.inv) + 1):
                itemused = self.inv[itemnum - 1]
                if itemused.type == 'HP':
                    self.hp += itemused.buff
                elif itemused.type == 'DMG':
                    self.dmgbuff *= itemused.buff
                    self.buff_duration = itemused.duration
                print(f'{self.name} used {itemused.name}!\n')
                self.inv.pop(itemnum - 1)
            else:
                print('Item used not in inventory!\n')

            
        else:
            print('No items left!\n')


    def run(self, target):
        success = random.randint(1, target.rchance)
        if success == 1:
            print('Success!')
            return True
        else:
            print('Failed!')
            return False


    def __str__(self):
        return self.name


#Weapons
Sword = Weapon('Sword', 30)
Fists = Weapon('Fists', 10)

#Spells
Firaga = Spells('Firaga', 50)
Meteor = Spells('Meteor', 120)
Gigaflare = Spells('GIGAFLARE!!', 200)
Zantetsuken = Spells('Zantetsuken!!', 180)

#Potions \\Items
HealingPotion = Potion('Health Potion', 'HP', 25, 1)
DamageBuff = Potion('Damage Buff Potion', 'DMG', 1.3, 4)



#Characters
Ifrit = Character('Ifrit', 300, Fists, [Firaga, Meteor], [HealingPotion, DamageBuff])
Bahamut = Character('Bahamut', 300, Sword, [Gigaflare, Zantetsuken], [HealingPotion, DamageBuff])




def in_battle(player, opponent):


    print(f'{player} is engaging in battle with {opponent}\n')

    Ran = False
    your_turn = True
    
    origin_opp_hp = opponent.hp
    origin_p_hp = player.hp

    turn=1

    while player.dead == False and opponent.dead == False and Ran == False:
        print(f'{player}: {player.hp}/{origin_p_hp} HP\n{opponent}: {opponent.hp}/{origin_opp_hp} HP\n')
        
        while not your_turn:
            option = random.randint(1, 2)
            if player.hp < opponent.wpn.dmg:
                opponent.attack(player)

            if opponent.hp > round(origin_opp_hp * 0.7):
                if option == 1:
                    opponent.attack(player)
                elif option == 2:
                    if DamageBuff in opponent.inv:
                        opponent.auto_item('DMG')#Damage
                    else:
                        opponent.attack(player)

            elif opponent.hp < round(origin_opp_hp * 0.3):
                if HealingPotion in opponent.inv:
                    opponent.auto_item('HP')#Health
                else:
                    opponent.defend()

            elif opponent.hp < round(origin_opp_hp * 0.5):
                if option == 1:
                    opponent.defend()
                elif option == 2:
                    opponent.attack(player)

            


            your_turn = True
            player.reset_buffs()
            turn += 1 


        while your_turn:
            

            while True:
                print(f'turn: {turn}')
                
                option = input('What will you do?\n1. Attack\n2. Defend\n3. Items\n4. Run\n5. Spells\nYour Option:')
                print('\n')

                if option == '1':
                    player.attack(opponent)
                    break 
                if option == '2':
                    player.defend()
                    break
                if option == '3':
                    player.use_item()
                    break
                if option == '4':
                    Ran = player.run(opponent)
                    break
                if option == '5':
                    player.use_spell(opponent)
                    break
                else:
                    print('Not a valid option')

            
            your_turn = False
            opponent.reset_buffs()
            

    opponent.check_status()
    player.check_status()

    if player.dead:
        print(f'{opponent} wins!')
    elif opponent.dead:
        print(f'{player} wins!')
    else:
        print(f'{player} has fled from battle with {opponent}')

in_battle(Ifrit, Bahamut)

