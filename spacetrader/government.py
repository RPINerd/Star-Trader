"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Government Module
    These classes and functions define the political systems and their
    respective traits as a result of the government.
"""

from enum import Enum

from constants import GOVT_NAMES, Activity, GovernmentId, TechLevel, TradeItemType


class PoliticalSystem:

    def __init__(
        self, name, stability, law, crime, economy, minTech, maxTech, trade, tradeable, smuggle, tradeItemType
    ):
        self.name = name
        self.stability = stability
        self.law = law
        self.crime = crime
        self.economy = economy
        self.minTech = minTech
        self.maxTech = maxTech
        self.trade = trade
        self.tradeable = tradeable
        self.smuggle = smuggle
        self.tradeItemType = tradeItemType


GOVERNMENTS = {
    GovernmentId.ANARCHY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.ANARCHY],
        0,
        Activity.ABSENT,
        Activity.SWARMS,
        Activity.MINIMAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        7,
        True,
        True,
        TradeItemType.FOOD,
    ),
    GovernmentId.CAPITALIST: PoliticalSystem(
        GOVT_NAMES[GovernmentId.CAPITALIST],
        2,
        Activity.SOME,
        Activity.FEW,
        Activity.SWARMS,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        1,
        True,
        True,
        TradeItemType.ORE,
    ),
    GovernmentId.COMMUNIST: PoliticalSystem(
        GOVT_NAMES[GovernmentId.COMMUNIST],
        6,
        Activity.ABUNDANT,
        Activity.MODERATE,
        Activity.MODERATE,
        TechLevel.AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        5,
        True,
        True,
        TradeItemType.NONE,
    ),
    GovernmentId.CONFEDERACY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.CONFEDERACY],
        5,
        Activity.MODERATE,
        Activity.SOME,
        Activity.MANY,
        TechLevel.AGRICULTURAL,
        TechLevel.POST_INDUSTRIAL,
        3,
        True,
        True,
        TradeItemType.GAMES,
    ),
    GovernmentId.CORPORATE: PoliticalSystem(
        GOVT_NAMES[GovernmentId.CORPORATE],
        2,
        Activity.ABUNDANT,
        Activity.FEW,
        Activity.SWARMS,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemType.ROBOTS,
    ),
    GovernmentId.CYBERNETIC: PoliticalSystem(
        GOVT_NAMES[GovernmentId.CYBERNETIC],
        0,
        Activity.SWARMS,
        Activity.SWARMS,
        Activity.MANY,
        TechLevel.POST_INDUSTRIAL,
        TechLevel.HI_TECH,
        0,
        False,
        False,
        TradeItemType.ORE,
    ),
    GovernmentId.DEMOCRACY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.DEMOCRACY],
        4,
        Activity.SOME,
        Activity.FEW,
        Activity.MANY,
        TechLevel.RENAISSANCE,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemType.GAMES,
    ),
    GovernmentId.DICTATORSHIP: PoliticalSystem(
        GOVT_NAMES[GovernmentId.DICTATORSHIP],
        3,
        Activity.MODERATE,
        Activity.MANY,
        Activity.SOME,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemType.NONE,
    ),
    GovernmentId.FASCIST: PoliticalSystem(
        GOVT_NAMES[GovernmentId.FASCIST],
        7,
        Activity.SWARMS,
        Activity.SWARMS,
        Activity.MINIMAL,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        0,
        False,
        True,
        TradeItemType.MACHINERY,
    ),
    GovernmentId.FEUDAL: PoliticalSystem(
        GOVT_NAMES[GovernmentId.FEUDAL],
        1,
        Activity.MINIMAL,
        Activity.ABUNDANT,
        Activity.FEW,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.RENAISSANCE,
        6,
        True,
        True,
        TradeItemType.FIREARMS,
    ),
    GovernmentId.MILITARY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.MILITARY],
        7,
        Activity.SWARMS,
        Activity.ABSENT,
        Activity.ABUNDANT,
        TechLevel.MEDIEVAL,
        TechLevel.HI_TECH,
        0,
        False,
        True,
        TradeItemType.ROBOTS,
    ),
    GovernmentId.MONARCHY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.MONARCHY],
        3,
        Activity.MODERATE,
        Activity.SOME,
        Activity.MODERATE,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        4,
        True,
        True,
        TradeItemType.MEDICINE,
    ),
    GovernmentId.PACIFIST: PoliticalSystem(
        GOVT_NAMES[GovernmentId.PACIFIST],
        7,
        Activity.FEW,
        Activity.MINIMAL,
        Activity.MANY,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.RENAISSANCE,
        1,
        True,
        False,
        TradeItemType.NONE,
    ),
    GovernmentId.SOCIALIST: PoliticalSystem(
        GOVT_NAMES[GovernmentId.SOCIALIST],
        4,
        Activity.FEW,
        Activity.MANY,
        Activity.SOME,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.INDUSTRIAL,
        6,
        True,
        True,
        TradeItemType.NONE,
    ),
    GovernmentId.SATORI: PoliticalSystem(
        GOVT_NAMES[GovernmentId.SATORI],
        0,
        Activity.MINIMAL,
        Activity.MINIMAL,
        Activity.MINIMAL,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.AGRICULTURAL,
        0,
        False,
        False,
        TradeItemType.NONE,
    ),
    GovernmentId.TECHNOCRACY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.TECHNOCRACY],
        1,
        Activity.ABUNDANT,
        Activity.SOME,
        Activity.ABUNDANT,
        TechLevel.EARLY_INDUSTRIAL,
        TechLevel.HI_TECH,
        2,
        True,
        True,
        TradeItemType.WATER,
    ),
    GovernmentId.THEOCRACY: PoliticalSystem(
        GOVT_NAMES[GovernmentId.THEOCRACY],
        5,
        Activity.ABUNDANT,
        Activity.MINIMAL,
        Activity.MODERATE,
        TechLevel.PRE_AGRICULTURAL,
        TechLevel.EARLY_INDUSTRIAL,
        0,
        True,
        True,
        TradeItemType.NARCOTICS,
    ),
}
