import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    gold = personCash["gold"]
    if personCash["platinum"] > 0:
        gold += platinum2gold(personCash["platinum"])
    if personCash["copper"] > 0:
        gold += copper2gold(personCash["copper"])
    if personCash["silver"] > 0:
        gold += silver2gold(personCash["silver"])
    return gold
    
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    cost = 0
    cost += people * COST_FOOD_HUMAN_COPPER_PER_DAY
    cost += horses * COST_FOOD_HORSE_COPPER_PER_DAY
    return round( copper2gold(cost) * JOURNEY_IN_DAYS, 2)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    end = []
    for item in list:
        if item[key] == value:
            end.append(item)
    return end

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    end = getAdventuringPeople(friends)
    end = getShareWithFriends(end)
    return end

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return round(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    rent = 0
    rent += horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    rent += tents * COST_TENT_GOLD_PER_WEEK * 2
    return float( rent)

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    itemlist = ""
    for index in range( len(items)):
        name = items[index]["name"]
        amount = items[index]["amount"]
        unit = items[index]["unit"]
        if index == len(items) -1:
            itemlist += f"{amount}{unit} {name}"
        else:
            itemlist += f"{amount}{unit} {name}, "
    return itemlist

def getItemsValueInGold(items:list) -> float:
    value = 0
    for item in items:
        type = item["price"]["type"]
        if type == "copper":
            value += copper2gold( item["amount"] * item["price"]["amount"])
        if type == "silver":
            value += silver2gold( item["amount"] * item["price"]["amount"])
        if type == "gold":
            value += item["amount"] * item["price"]["amount"]
        if type == "platinum":
            value += platinum2gold( item["amount"] * item["price"]["amount"])
    return value

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()