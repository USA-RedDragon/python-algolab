from algolab import AlgoLabAlgorithm
from algolab.apis.consumer import AlgoLabConsumerAPI as AlgoLabAPI
from algolab.apis.crypto import AlgoLabCoinGeckoAPI
from algolab.price_listener import AlgoLabPriceListener
from algolab.tradables.crypto import AlgoLabCryptoTradable


class MyAlgorithm(AlgoLabAlgorithm):
    """Your algorithm should be implemented in a single class"""

    def __init__(self, algo_maker: AlgoLabAPI):
        """The creation point of your algorithm class

        Data can be stored in "self" and accessed from
        within other class methods

        Args:
            algo_maker: an AlgoLabAPI object, used for
                things such as accessing your credentials
                and other secrets securely
        """
        self._algo_maker = algo_maker
        self._price_listener = AlgoLabPriceListener(AlgoLabCoinGeckoAPI(), AlgoLabCryptoTradable.BSV, self.process)
        self._price_listener_uuid = algo_maker.get_listener_service().register(self._price_listener)

    def __destroy__(self):
        """The deletion point of your algorithm class

        This is your opportunity to cleanly save things before
        deprovisioning
        """
        self._algo_maker.get_listener_service().deregister(self._price_listener_uuid)

    def process(self, data_point):
        """
        Processes a single data_point in the algorithm.

        data_point - the datapoint of the event

        Returns:
            any actions you would like to execute
        """
        print(data_point)
