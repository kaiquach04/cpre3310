# lab01_part02.py by Kai Quach
# 01/29/26

def frequency(inputs: list[list[str]], character: str) -> None:
    count = 0
    list_count = 0
    for nested_list in inputs:
        count = 0
        for char in nested_list:
            if character == char:
                count += 1
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