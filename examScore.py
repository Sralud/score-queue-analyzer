import queue

def main():

    max_size = 10
    exam_queue = queue.Queue(maxsize=max_size)

    print("Enter exam scores (type 'done' to finish):")
    while not exam_queue.full():
        user_input = input()
        if user_input.lower() == 'done':
            break
        try:
            score = int(user_input)
            if 0 <= score <= 100:
                exam_queue.put(score)
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer score.")

    print("\nInitial Queue:")
    print(list(exam_queue.queue))

    filtered_scores = queue.Queue(maxsize=max_size)
    while not exam_queue.empty():
        score = exam_queue.get()
        if score != 100:
            filtered_scores.put(score)

    if filtered_scores.empty():
        print("\nThe queue is empty.")
    elif filtered_scores.full():
        print("\nThe queue is full.")
    else:
        print("\nThe queue is neither empty nor full.")

    print("\nFiltered Queue (scores != 100):")
    print(list(filtered_scores.queue))

main()