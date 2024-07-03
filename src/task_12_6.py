from collections import deque

def task_add(que, task):
    que.append(task)


def task_fin(que):
    que.popleft()

tasks = deque()


print(task_add(tasks, "task1"))
print(tasks)
print(task_add(tasks, "task2"))
print(tasks)
print(task_add(tasks, "task3"))
print(tasks)
print(task_fin(tasks))
print(tasks)
print(task_add(tasks, "task4"))
print(tasks)
print(task_fin(tasks))
print(tasks)
print(task_add(tasks, "task5"))
print(tasks)
print(task_add(tasks, "task6"))
print(tasks)
print(task_fin(tasks))
print(tasks)
print(task_fin(tasks))
print(tasks)
print(task_add(tasks, "task7"))
print(tasks)

