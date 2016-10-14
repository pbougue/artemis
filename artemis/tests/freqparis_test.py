from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("freqparis")])
class FreqParis():
    """
    TODO: put there comments about the dataset
    """
    def test_freqparis_01(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0700")

    def test_freqparis_02(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2330")

    def test_freqparis_03(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2200")

    def test_freqparis_04(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0008", datetime_represents="arrival")

    def test_freqparis_05(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T0020", datetime_represents="arrival")

    def test_freqparis_06(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2350")

    def test_freqparis_07(self):
        self.journey(_from="stop_area:FQP:SA:defen",
                     to="stop_area:FQP:SA:grest", datetime="20090922T2355")


@set_scenario({"freqparis": {"scenario": "default"}})
class TestFreqParisDefault(FreqParis, ArtemisTestFixture):
    pass

@set_scenario({"freqparis": {"scenario": "new_default"}})
class TestFreqParisNewDefault(FreqParis, ArtemisTestFixture):
    pass


@xfail(reason="Unsupported experimental scenario!", raises=AssertionError)
@set_scenario({"freqparis": {"scenario": "experimental"}})
class TestFreqParisExperimental(FreqParis, ArtemisTestFixture):
    pass