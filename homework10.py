INPUT = """map,9,150
compass,13,35
water,153,200
sandwich,50,160
glucose,15,60
tin,68,45
banana,27,60
apple,39,40
cheese,23,30
beer,52,10
suntan cream,11,70
camera,32,30
T-shirt,24,15
trousers,48,10
umbrella,73,40
waterproof trousers,42,70
waterproof overclothes,43,75
note-case,22,80
sunglasses,7,20
towel,18,12
socks,4,50
book,30,10"""

LIMIT = 400

if __name__ == '__main__':
    def comparator(i):
        return float(i.split(',')[2]) / float(i.split(',')[1])
    sorted_input = sorted(INPUT.split('\n'), key=comparator, reverse=True)
    bagpack = []
    total_weight = 0
    for item in sorted_input:
        if total_weight + int(item.split(',')[1]) <= LIMIT:
            bagpack.append(item)
            total_weight += int(item.split(',')[1])
    print('Bagpack: ', bagpack)
    print('Total weight: ', total_weight)
