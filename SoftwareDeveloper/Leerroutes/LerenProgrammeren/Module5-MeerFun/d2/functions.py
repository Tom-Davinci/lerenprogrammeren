import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

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
    total = 0
    for person in people:
        if person["cash"]["platinum"]:
            total += platinum2gold(person["cash"]["platinum"])
        if person["cash"]["silver"]:
            total += silver2gold(person["cash"]["silver"])
        if person["cash"]["copper"]:
            total += copper2gold(person["cash"]["copper"])
        if person["cash"]["gold"]:
            total += person["cash"]["gold"]
    return total


##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    interesting = []
    for investor in investors:
        if investor["profitReturn"] <= 10:
            interesting.append(investor)
    return interesting

def getAdventuringInvestors(investors:list) -> list:
    investors = getInterestingInvestors(investors)
    return getAdventuringPeople(investors)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    investors = getAdventuringInvestors(investors)
    return round( len(investors) * (getItemsValueInGold(gear) + getJourneyFoodCostsInGold(1, 1) + getTotalRentalCost(1, 1)), 2)

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    x, cost = 0, 0
    while cost < leftoverGold:
        cost = getJourneyInnCostsInGold(x, people, horses)
        x += 1
    if leftoverGold == 0:
        return 0
    return x - 2

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    cost = 0
    cost += silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT) * nightsInInn
    cost += copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT) * nightsInInn
    return round(cost, 2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    investors = getInterestingInvestors(investors)
    investorMoney = []
    for investor in investors:
        cost = round( investor["profitReturn"] / 100 * profitGold, 2)
        investorMoney.append(cost)
    return investorMoney

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float: #fellowship = amount of adventurers
    return round((profitGold - sum(investorsCuts)) / fellowship, 2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    investorCount = 0
    
    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    amountAdventurers = len(adventuringInvestors) + len(adventuringFriends) + 1
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, amountAdventurers)
    
    # verdeel de uitkomsten
    for person in people:
        start = getPersonCashInGold(person["cash"])
        if person in interestingInvestors:
            if person in adventuringInvestors:
                end = start + investorsCuts[investorCount] + goldCut
            else:
                end = start + investorsCuts[investorCount]
            investorCount += 1
        elif person in adventuringFriends:
            end = start + goldCut - 10
        elif person == mainCharacter:
            end = start + goldCut + (len(adventuringFriends) * 10)
        else:
            end = start
        
        earnings.append({
            'name'   : person["name"],
            'start'  : start,
            'end'    : end
        })

    return earnings

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