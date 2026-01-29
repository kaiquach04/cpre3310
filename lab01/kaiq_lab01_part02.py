# lab01_part02.py by Kai Quach
# 01/29/26


def frequency(inputs: list[list[str]], character: str) -> None:
    count = 0
    list_count = 0 # keeps track of current list index
    for nested_list in inputs: # a nested loop since its a list within a list
        count = 0
        for char in nested_list: # looking at one of the 3 lists, and starts iterating through the chars
            if character == char:
                count += 1 # increase count if char is located
        print(f"List[{list_count}]: {count}")
        list_count += 1  
    

def main():
    inputs = [
        list("AOLSLAALYJJVVRPLZBHYABDPAOBSLAZAOBURBMVAOLYAOPUNZ"),
        list("ZCXNSMCPROCTYDGHCSUIRYTEBHHCJSMECWTQZCHDKRILLMSJS"),
        list("WSCVKAUSAUDJAUUEAOPLAHSMACDGHAUUSGABXHAGEHASGDARU")
    ]

    charToCount = input("What character do you want to check? ")
    frequency(inputs, charToCount)



if __name__ == "__main__":
    main()