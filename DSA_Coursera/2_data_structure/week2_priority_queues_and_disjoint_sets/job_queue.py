# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
Thread = namedtuple("Thread", ["available_at", "index"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    threads = [Thread(0, i) for i in range(n_workers)]

    for job in jobs:
        next_worker = threads[0]
        result.append(AssignedJob(next_worker.index, next_worker.available_at))
        updated_thread = Thread((next_worker.available_at + job), next_worker.index)
        threads[0] = updated_thread
        shift_down(0, threads)

    return result


def shift_down(index, array):
    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child >= len(array):
            break

        min_index = index
        if left_child < len(array) and array[left_child] < array[min_index]:
            min_index = left_child
        if right_child < len(array) and array[right_child] < array[min_index]:
            min_index = right_child

        if min_index == index:
            break
        else:
            array[index], array[min_index] = array[min_index], array[index]
            index = min_index


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
