# -*- coding: utf-8 -*-

from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet, set_scenario
import pytest

xfail = pytest.mark.xfail


@dataset([DataSet("fr-pdl")])
class Destineo(object):
    """
    test for destineo with their custom scenario
    """
    def test_destineo_01(self):
        """
        we want to go at the bss north station from the bss south station
        all pt solution are way too long, only 3 non_pt solutions must be returned
        """
        self.journey(_from="poi:TRANSP44_202",
                     to="poi:TRANSP44_369", datetime="20141109T180000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['bss'],
                     min_nb_journeys=3)

    def test_destineo_02(self):
        """
        we go to "Pouzauges" from "La Mothe-Achard" nothing special with this one
        """
        self.journey(_from="admin:fr:85152",
                     to="admin:fr:85182", datetime="20141203T121000",
                     first_section_mode=['bike', 'bss', 'walking', 'car'],
                     last_section_mode=['bss'],
                     min_nb_journeys=3)

    def test_destineo_03(self):
        """
        we go to "Nantes" from "Treillieres"
        we must have a journey with car a departure, also know as P+R and tram train
        and we also check the sort by departure date (and not time), since normaly pure pt journey must be before journey with an alternative fallback
        """
        self.journey(_from="-1.585760091193374;47.29129921981793",
                     to="-1.544888102;47.21403406", datetime="20141201T090000",
                     first_section_mode=['walking', 'car'],
                     min_nb_journeys=3)

    @xfail(reason="http://jira.canaltp.fr/browse/NAVP-209", raises=AssertionError, strict=True)
    def test_destineo_04(self):
        """
        we go to "Pazanne-Mairie-(Ste) (Sainte-Pazanne)" from "gare de Ste-Pazanne (Sainte-Pazanne)"
        there is a non_pt_walk solution, all PT solutions must be filtered since they are way longer than the non pt
        """
        self.journey(_from='stop_area:SNC:SA:SAOCE87481226',
                     to='stop_area:SNC:SA:SAOCE87328625', datetime='20141204T101500',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3)

    def test_destineo_05(self):
        """
        we go from "rue JEAN GORIN (Nantes)" to "15 rue ADOLPHE MOITIE (Nantes)"
        """
        self.journey(_from='-1.5288823896877313;47.2093118677334',
                     to='-1.554597505;47.22280345', datetime='20141111T111000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3, max_nb_journeys=3)

    def test_destineo_06(self):
        """
        we go from "11 boulevard DE L'EGALITE (Nantes)" to "Pompidou (Nantes)"
        """
        self.journey(_from='-1.587547422;47.20738048',
                     to='stop_area:NAN:SA:PPDO', datetime='20141111T111000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3)

    def test_destineo_equivalent_journeys(self):
        """
        http://jira.canaltp.fr/browse/NAVITIAII-1630

        We don't want to take the same vjs but at different stop points, they should be filtered
        """
        self.journey(_from='stop_area:NAN:SA:COMM',
                     to='admin:fr:44066', datetime='20150124T200000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3)

    def test_destineo_07(self):
        """
        we go from "Pompidou (Nantes)" to "Mairie (Laval)"
        """
        self.journey(_from='stop_area:NAN:SA:PPDO',
                     to='stop_area:LAV:SA:245', datetime='20141212T111000',
                     first_section_mode=['walking', 'bike', 'bss', 'car'],
                     last_section_mode=['walking', 'bss'],
                     min_nb_journeys=3, datetime_represents='arrival')

    def test_destineo_08(self):
        """
        We go from "Baffert (La Roche-sur-Yon)" to "Les Alisiers (La Roche-sur-Yon)"
        and we want an accessible journey!
        """
        self.journey(_from='stop_area:LRY:SA:lrybaff',
                     to='stop_area:LRY:SA:lryaliz', datetime='20141015T174500',
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3, datetime_represents='departure', wheelchair=True)

    def test_destineo_09(self):
        """
        we go from "Blanchetiere (La chapelle sur erdre)" to "2 cours du champ de mars (Nantes)"
        we want an accessible journey but Blanchetiere is not accessible, and the next stop area: La Cogne,
        is only accessible on the other direction.
        Last but not least we will take the C2 line to "Commerce", this stop_area has two stop_point
        deserve by the C2 but only one of them is accessible and the transfers is longer!
        """
        self.journey(_from='stop_area:NAN:SA:BNCH',
                     to='-1.544430191;47.21391219', datetime='20141006T104000',
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3, datetime_represents='departure', wheelchair=True)

    def test_destineo_10(self):
        """
        We go from "Rosenberg (Saint-Herblain)" to "Cochardieres (Saint-Herblain)".
        We want an accessible journey but there is none!
        """
        self.journey(_from='stop_area:NAN:SA:RSNB',
                     to='stop_area:NAN:SA:CCDI', datetime='20141028T115000',
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3, datetime_represents='arrival', wheelchair=True)

    def test_destineo_11(self):
        """
        We go from "Cimetiere de Bouaye (Bouaye)" to "Piano'cktail (Bouguenais)".
        We want an accessible journey but there is none!
        """
        self.journey(_from='stop_area:NAN:SA:BYEE',
                     to='stop_area:NAN:SA:PIAO', datetime='20141028T115000',
                     first_section_mode=['walking', 'car'],
                     last_section_mode=['walking'],
                     min_nb_journeys=3, datetime_represents='departure', wheelchair=True)

    def test_destineo_autocomplete(self):
        """
        We want to find the street "rue de la Loire (Saint-Sebastien-sur-Loire)" as the first answer.

        """
        self.api('places?q=rue%20de%20la%20loire%20saint%20sebastien&count=1&')
        
    def test_geo_status(self):
        """
        check geodata sources and volume
        """
        self.api('_geo_status')

@set_scenario({"fr-pdl": {"scenario": "destineo"}})
class TestDestineo(Destineo, ArtemisTestFixture):
    pass
