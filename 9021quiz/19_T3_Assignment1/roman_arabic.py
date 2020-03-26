def roman_to_int(roman):
    roman_dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    s = 0
    if not all(i in roman_dic for i in roman):
        return False
    else:
        for i in range(len(roman) - 1):
            if roman_dic[roman[i]] < roman_dic[roman[i + 1]]:
                s -= roman_dic[roman[i]]
            else:
                s += roman_dic[roman[i]]
        return s + roman_dic[roman[-1]]


def int_to_roman(number):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    for i in range(len(num_list)):
        while number >= num_list[i]:
            number -= num_list[i]
            roman += roman_list[i]
    return roman


def get_rules(string):
    rule_dict = {}
    for i in range(len(string)):
        if i % 2 == 0:
            rule_dict[string[::-1][i]] = int(1 * (10 ** (i / 2)))
        else:
            rule_dict[string[::-1][i]] = int(5 * (10 ** (i // 2)))
    return rule_dict


def get_two_list(rule_dict):
    num_list = []
    roman_list = []
    ele = list(rule_dict.keys())[::-1]
    length = len(ele)
    for i in range(length - 2):
        num_list.append(rule_dict[ele[i]])
        roman_list.append(ele[i])
        if '1' in str(rule_dict[ele[i]]):
            num_list.append(rule_dict[ele[i]] - rule_dict[ele[i + 2]])
            roman_list.append(ele[i + 2] + ele[i])
        elif '5' in str(rule_dict[ele[i]]):
            num_list.append(rule_dict[ele[i]] - rule_dict[ele[i + 1]])
            roman_list.append(ele[i + 1] + ele[i])
    num_list.append(rule_dict[ele[-2]])
    num_list.append(rule_dict[ele[-2]] - rule_dict[ele[-1]])
    num_list.append(rule_dict[ele[-1]])
    roman_list.append(ele[-2])
    roman_list.append(ele[-1] + ele[-2])
    roman_list.append(ele[-1])
    return num_list, roman_list


def general_roman_to_int(first, rule_dict):
    s = 0
    if not all(i in rule_dict for i in first):
        return False
    else:
        for i in range(len(first) - 1):
            if rule_dict[first[i]] < rule_dict[first[i + 1]]:
                s -= rule_dict[first[i]]
            else:
                s += rule_dict[first[i]]
        return s + rule_dict[first[-1]]


def general_int_to_roman(first, rule):
    num_list, roman_list = get_two_list(rule)
    num = int(first)
    result = ''
    for i in range(len(num_list)):
        while num >= num_list[i]:

            result += roman_list[i]
            num -= num_list[i]
    return result

def judge_valid(rule):
    invalid_list = []
    for i in rule:
        if '5' in str(rule[i]):
            invalid_list.append(i + i)
    return invalid_list

string = input('How can I help you? ')
command_list = string.strip().split(' ')
length_of_command = len(command_list)
flag = 1
# print(int_to_roman(100000))
if 'Please convert' not in string:
    flag = 0
if 'using' in string:
    if length_of_command != 5:
        flag = 0
if 'minimally' in string:
    if length_of_command != 4:
        flag = 0
if 'using' not in string and 'minimally' not in string:
    if length_of_command != 3:
        flag = 0

if not flag:
    print("I don't get what you want, sorry mate!")
    exit(0)


# First kind of input
if length_of_command == 3:
    num = command_list[2]
    if num.isdigit():
        if 0 < int(num) < 4000 and num[0] != '0':
            flag = 0
            print(f'Sure! It is {int_to_roman(int(num))}')
    else:
        int_num = roman_to_int(num)
        if int_num and num == int_to_roman(int_num):
            flag = 0
            print(f'Sure! It is {int_num}')
    if flag:
        print("Hey, ask me something that's not impossible to do!")
        exit(0)


# Second kind of input
if length_of_command == 5:
    first = command_list[2]
    second = command_list[4]
    print(second,set(second))
    print(len(second), len(set(second)))
    for i in second:
        if i not in set(second):
            print(111)
            print(i)
    if len(set(second)) == len(second):
        if first.isalpha():
            rule = get_rules(second)
            invalid = judge_valid(rule)
            result = general_roman_to_int(first, rule)
            if result and all(i not in first for i in invalid):
                compare = general_int_to_roman(result, rule)
                # print(compare, first)
                if compare == first:
                    flag = 0
                    print(f'Sure! It is {result}')

        elif first.isdigit():
            if int(first) > 0 and first[0] != '0':

                flag = 0
                rule = get_rules(second)
                result = general_int_to_roman(first, rule)
                print(f'Sure! It is {result}')

    if flag:
        print("Hey, ask me something that's not impossible to do!")
        exit(0)

# Third kind of input
if length_of_command == 4:
    roman = command_list[2]
    if roman.isalpha():
        process_roman = ''
        for i in roman:
            if i not in process_roman:
                process_roman += i

        # normal order
        rule_1 = get_rules(process_roman)
        invalid_1 = judge_valid(rule_1)
        for i in invalid_1:
            if i in roman:
                if '5' in str(rule_1[i[0]]):
                    rule_1[i] = rule_1[i[0]]
                    for j in rule_1:
                        if rule_1[j] > rule_1[i]:
                            if '5' in str(rule_1[j]):
                                rule_1[j] = 2 * rule_1[j]
                            else:
                                rule_1[j] = 5 * rule_1[j]
                    rule_1[i[0]] = 2 * rule_1[i[0]]
        count = 0
        for i in rule_1:
            if len(i) == 2:
                count += 1
                str_ = '_' * count
                rule_1[str_] = rule_1[i]
                del rule_1[i]
        rule_1 = dict(sorted(rule_1.items(), key=lambda x: x[1]))
        format_1 = ''.join(list(rule_1.keys())[::-1])
        result_1 = general_roman_to_int(roman, rule_1)
        compare_1 = general_int_to_roman(result_1, rule_1)

        print(rule_1,format_1)
        if compare_1 == roman:
        # reverse order
            rule_2 = get_rules(process_roman[::-1])
            invalid_2 = judge_valid(rule_2)
            for i in invalid_2:
                if i in roman:
                    if '5' in str(rule_2[i[0]]):
                        rule_2[i] = rule_2[i[0]]
                        for j in rule_2:
                            if rule_2[j] > rule_2[i]:
                                if '5' in str(rule_2[j]):
                                    rule_2[j] = 2 * rule_2[j]
                                else:
                                    rule_2[j] = 5 * rule_2[j]
                        rule_2[i[0]] = 2 * rule_2[i[0]]
            count = 0
            for i in rule_2:
                if len(i) == 2:
                    count += 1
                    str_ = '_' * count
                    rule_2[str_] = rule_2[i]
                    del rule_2[i]
            rule_2 = dict(sorted(rule_2.items(), key=lambda x: x[1]))
            format_2 = ''.join(list(rule_2.keys())[::-1])
            result_2 = general_roman_to_int(roman, rule_2)
            compare_2 = general_int_to_roman(result_2, rule_2)
            if compare_2 == roman:
                if result_1 > result_2:
                    flag = 0
                    print(f'Sure! It is {result_2} using {format_2}')
                else:
                    flag = 0
                    print(f'Sure! It is {result_1} using {format_1}')
            else:
                flag = 0
                print(f'Sure! It is {result_1} using {format_1}')
        else:
            #fefefefefefefefefefefefefe
            print("Hey, ask me something that's not impossible to do!")
            exit(0)

        # if compare == roman:
        #     flag = 0
        #     print(f'Sure! It is {result} using {format}')
        # else:
        #     print("Hey, ask me something that's not impossible to do!")
        #     exit(0)

    else:
        print("Hey, ask me something that's not impossible to do!")
        exit(0)



