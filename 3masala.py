# 3--------
def find_top_three_numbers_sorted(data: list) -> list:
    result=[]
    for sonlar in data:
        sonlar=sorted(sonlar, reverse=True)
        result.append(tuple(sonlar[:3]))
    return result
data=[(10,20,30,11),(5,15),(40,),(7,8,50,3)]
print(find_top_three_numbers_sorted(data))