def min_max_sum(input_list):
    input_list.sort()
    minimum_sum = sum(input_list[:4])
    maximum_sum = sum(input_list[1:])
    return print(f'{minimum_sum} {maximum_sum}')

if __name__=="__main__":
    input_list = [1,3,5,7,9]
    min_max_sum(input_list)