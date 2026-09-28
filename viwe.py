""""аоказ списока"""
def show_collection(task_collection):
    print("-" * 30)
    for number, content in enumerate(task_collection):
        word = ''
        for symbol in content:
            if symbol == '|':
                word = f"{word}{symbol}"
            else:
                break
        print(number + 1, str(word))
    print("-" * 30)