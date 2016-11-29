import sys

def make_gadget(profit, weight):
    return { 'profit': profit, 'weight': weight }


def parse_input(lines):
    profits = lines[1].split(',')
    weights = lines[2].split(',')
    for i in range(len(profits)):
        yield make_gadget(int(profits[i]), int(weights[i]))

def maximize_profit(gadgets, g_max_weight):
    table = [[None for i in range(g_max_weight + 1)] for g in gadgets]
    for item_index, row in enumerate(table):
        for max_weight, weight in enumerate(row):
            if max_weight is 0: 
                table[item_index][max_weight] = 0
                
            elif item_index is 0:
                table[item_index][max_weight] = 0
            
            elif max_weight <= gadgets[item_index]['weight']:
                table[item_index][max_weight] = table[item_index - 1][max_weight]
            
            else:
                table[item_index][max_weight] = max(gadgets[item_index]['profit'] + table[item_index - 1][max_weight - gadgets[item_index]['weight']],
                        table[item_index - 1][max_weight])

    return table[len(table) - 1][g_max_weight]

def main():
    lines = sys.stdin.readlines()
    gadgets = list(parse_input(lines))
    max_weight = int(lines[3])
    profit = maximize_profit(gadgets, max_weight)
    print(profit)
    

main()
    

