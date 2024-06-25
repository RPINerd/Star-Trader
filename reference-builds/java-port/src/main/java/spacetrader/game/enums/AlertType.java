package spacetrader.game.enums;

public enum AlertType implements SpaceTraderEnum {

    Alert,
    AppStart,
    ArrivalBuyNewspaper,
    ArrivalIFFuel,
    ArrivalIFFuelRepairs,
    ArrivalIFNewspaper,
    ArrivalIFRepairs,
    CargoIF,
    CargoNoEmptyBays,
    CargoNoneAvailable,
    CargoNoneToSell,
    CargoNotInterested,
    CargoNotSold,
    ChartJump,
    ChartJumpCurrent,
    ChartJumpNoSystemSelected,
    ChartTrackSystem,
    ChartWormholeUnreachable,
    Cheater,
    CrewFireMercenary,
    CrewNoQuarters,
    DebtNoBuy,
    DebtNone,
    DebtReminder,
    DebtTooLargeGrounded,
    DebtTooLargeLoan,
    DebtTooLargeTrade,
    DebtWarning,
    EncounterArrested,
    EncounterAttackNoDisruptors,
    EncounterAttackNoLasers,
    EncounterAttackNoWeapons,
    EncounterAttackPolice,
    EncounterAttackTrader,
    EncounterBothDestroyed,
    EncounterDisabledOpponent,
    EncounterDumpAll,
    EncounterDumpWarning,
    EncounterEscaped,
    EncounterEscapedHit,
    EncounterEscapePodActivated,
    EncounterLooting,
    EncounterOpponentEscaped,
    EncounterPiratesBounty,
    EncounterPiratesFindNoCargo,
    EncounterPoliceBribe,
    EncounterPoliceBribeCant,
    EncounterPoliceBribeLowCash,
    EncounterPoliceFine,
    EncounterPoliceNothingFound,
    EncounterPoliceNothingIllegal,
    EncounterPoliceSubmit,
    EncounterPoliceSurrender,
    EncounterScoop,
    EncounterScoopNoRoom,
    EncounterScoopNoScoop,
    EncounterSurrenderRefused,
    EncounterTradeCompleted,
    EncounterYouLose,
    EncounterYouWin,
    EquipmentAlreadyOwn,
    EquipmentBuy,
    EquipmentEscapePod,
    EquipmentExtraBaysInUse,
    EquipmentIF,
    EquipmentNotEnoughSlots,
    EquipmentSell,
    FileErrorOpen,
    FileErrorSave,
    FleaBuilt,
    GameAbandonConfirm,
    GameClearHighScores,
    GameEndHighScoreAchieved,
    GameEndHighScoreCheat,
    GameEndHighScoreMissed,
    GameEndKilled,
    GameEndRetired,
    GameEndScore,
    GameRetire,
    InsuranceNoEscapePod,
    InsurancePayoff,
    InsuranceStop,
    JailConvicted,
    JailFleaReceived,
    JailIllegalGoodsImpounded,
    JailInsuranceLost,
    JailMercenariesLeave,
    JailShipSold,
    LeavingIFInsurance,
    LeavingIFMercenaries,
    LeavingIFWormholeTax,
    NewGameConfirm,
    NewGameMoreSkillPoints,
    OptionsNoGame,
    PreciousHidden,
    RegistryError,
    ShipBuyConfirm,
    ShipBuyCrewQuarters,
    ShipBuyIF,
    ShipBuyIFTransfer,
    ShipBuyNoSlots,
    ShipBuyNotAvailable,
    ShipBuyNoTransfer,
    ShipBuyPassengerQuarters,
    ShipBuyTransfer,
    ShipDesignIF,
    ShipDesignThanks,
    SpecialIF,
    SpecialNoQuarters,
    SpecialNotEnoughBays,
    SpecialPassengerOnBoard,
    TravelArrival,
    TravelUneventfulTrip;

    @Override
    public int castToInt() {
        return ordinal();
    }
}
