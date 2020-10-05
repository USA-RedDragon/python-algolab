from time import sleep

from algolab.service import AlgoLabService

from algo import MyAlgorithm

if __name__ == "__main__":
    svc = AlgoLabService()
    svc._start()
    svc._run_algo(MyAlgorithm)

    while True:
        try:
            sleep(10)
        except KeyboardInterrupt:
            svc._stop()
            exit(0)
