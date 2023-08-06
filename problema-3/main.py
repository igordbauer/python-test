obj = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E"}


# def return_index(converted_answer):
#     for index, i in enumerate(converted_answer, start=0):
#         if converted_answer[index] == 1:
#             return index


def return_index(converted_answer):
    selected = 0
    count = 0
    for i in converted_answer:
        if converted_answer[count] == 1:
            selected = count
        else:
            count += 1
    return selected


def convert_answer(answers):
    int_answer_array = []
    for i in range(5):
        answer_array = answers.split(" ")
        int_answer_array.append(int(answer_array[i]))

    converted_answer = []
    for answer in int_answer_array:
        if int(answer) <= 127:
            converted_answer.append(1)
        else:
            converted_answer.append(0)

    return converted_answer


def isValid_answer(element):
    if element == 1:
        return True
    else:
        return False


def check_result(converted_answer):
    filtered_answer_list = list(filter(isValid_answer, converted_answer))
    if len(filtered_answer_list) > 1:
        return "*"
    else:
        return obj[f"{return_index(converted_answer)}"]


number_page_questions = int(input())
final_result_array = []
while number_page_questions != 0:
    for question in range(number_page_questions):
        answer = str(input())
        final_result = check_result(convert_answer(answer))
        final_result_array.append(final_result)
    number_page_questions = int(input())

for i in final_result_array:
    print(i)
