from typing import Optional, List, Union


def mex(sgs: set) -> int:
    sgs = list(sgs)
    sgs.sort()
    for i in range(len(sgs)):
        if i != sgs[i]:
            return i
    return sgs[-1] + 1


def brake_case(case: int) -> List[Union[int, list]]:
    nex_cases = list()

    if case - 2 >= 0:
        nex_cases.append(case - 2)
        for i in range(1, (case - 2)):
            nex_cases.append([i, case - 2 - i])

    nex_cases.append(case - 1)
    for i in range(1, (case - 1)):
        nex_cases.append([i, case - 1 - i])

    return nex_cases


def sg_calculator(case: int):
    sg_values = [0, ]

    for i in range(1, case + 1):
        case_sgs = []
        next_cases = brake_case(i)

        for next_case in next_cases:
            if isinstance(next_case, list):
                case_sgs.append(sg_values[next_case[0]] ^ sg_values[next_case[1]])
            else:
                case_sgs.append(sg_values[next_case])
    
        sg_values.append(mex(set(case_sgs)))
    return sg_values[-1]


if __name__ == '__main__':
    case = int(input('how many bowling pins are there?'))
    sg = sg_calculator(case)
    print(f'answer is {sg}')
