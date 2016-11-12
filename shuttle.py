import sys

def make_gadget(profit, weight):
    return { 'profit': profit, 'weight': weight }


def parse_input(lines):
    profits = lines[1].split(',')
    weights = lines[2].split(',')
    for i in range(0, len(profits)):
        yield make_gadget(int(profits[i]), int(weights[i]))

def maximize_profit(gadgets, g_max_weight):
    table = [[None for i in range(0, g_max_weight + 1)] for g in gadgets]
    for num_items, row in enumerate(table):
        for max_weight, weight in enumerate(row):
            if max_weight is 0: 
                table[num_items][max_weight] = 0
                
            elif num_items is 0:
                table[num_items][max_weight] = 0
            
            elif max_weight <= gadgets[num_items]['weight']:
                table[num_items][max_weight] = table[num_items - 1][max_weight]
            
            else:
                table[num_items][max_weight] = max(gadgets[num_items]['profit'] + table[num_items - 1][max_weight - gadgets[num_items]['weight']],
                        table[num_items - 1][max_weight])

    return table[len(table) - 1][g_max_weight]

def main():
    lines = sys.stdin.readlines()
    gadgets = list(parse_input(lines))
    max_weight = int(lines[3])
    profit = maximize_profit(gadgets, max_weight)
    print(profit)
    

main()
    

