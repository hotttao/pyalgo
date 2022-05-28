from prometheus_client import start_http_server, multiprocess, CollectorRegistry, Summary, Counter, generate_latest
import logging
import sys
import time
import os
import random
import multiprocessing

from datetime import datetime

os.environ["prometheus_multiproc_dir"] = "/tmp/prom"


# Prometheus metrics
FILE_GESTER_TIME = Summary(
    'BSA_file_gester_eft_worker', 'Time spent loading eft files & # loaded')
FILE_GESTER_LINE_COUNT = Counter(
    'BSA_file_gester_eft_line_count', 'Running counter of eft lines loaded')


@FILE_GESTER_TIME.time()
def worker(random_count):

    counter = 0
    while counter < random_count:
        FILE_GESTER_LINE_COUNT.inc()
        counter += 1
        # print(random_count, ' ', counter)
        time.sleep(1/5)
    return


def child_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)


def main():

    start_time = datetime.now()
    print('* Start Time               :', start_time)
    print('')

    try:

        # Start up the server to expose the metrics.
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        start_http_server(8000, registry=registry)
        print(os.environ["prometheus_multiproc_dir"])

        # Step 1: Init multiprocessing.Pool()
        pool = multiprocessing.Pool(4)

        x = 0
        while x < 4:

            # This works, this ends as a serial completing, worker one after the other
            #worker(random.randint(10, 120))

            # This does not increment counters, this is suppose to place the working each in his own work space, so that all 4 basically run in parrallel
            pool.apply_async(worker, (random.randint(10000, 1200000), ))

            x += 1

        pool.close()
        pool.join()     # Sleep here until all workers are done

    except KeyboardInterrupt:
        print('Shutting Down Unexpectedly')
        sys.stdout.flush()
        sys.exit(-1)

    except Exception as ex:
        print("Failed to create worker {err}".format(err=ex))

    finally:

        print('')
        print('Shutting Down')
        finish_time = datetime.now()
        run_time = finish_time - start_time
        print('* Total Run Time         :', run_time)


if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )

    main()

# end __name__ == '__main__'
