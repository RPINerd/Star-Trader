"""
    Space Trader (PalmOS) | RPINerd, 2024

    The thought with this file is to have a universal file that contains all the
    actions that the user can take in the game.
    In theory we can then just tie any UI into the functions of the game and not
    have to worry about rewriting the game logic.
"""

import src.constants as c
import src.economy as e


# Disordered list of user interactions
def get_system_info() -> tuple[list[str], str]:
    current_planet = c.GAME["universe"].planets[c.GAME["commander"].currentSystem]

    sys_info = current_planet.system_info()

    # Format system pressure
    pressure = current_planet.get_pressure()
    pressure_str = f"System is {c.SocietalPressure.name(pressure)}"

    return sys_info, pressure_str


def get_commander_info() -> dict:
    """
    Returns a dictionary of the commander's information
    """
    commander = c.GAME["commander"]
    return {
        "name": commander.name,
        "pilot": (commander.pilotSkill, commander.pilotSkill),
        "fighter": (commander.fighterSkill, commander.fighterSkill),
        "trader": (commander.traderSkill, commander.traderSkill),
        "engineer": (commander.engineerSkill, commander.engineerSkill),
        "kills": commander.kills,
        "time": commander.timePlayed,
        "cash": commander.credits,
        "debt": commander.debt,
        "net_worth": commander.get_net_worth(),
        "rep": commander.get_reputation(),
        "record": commander.get_police_record(),
        "difficulty": c.GAME["difficulty"],
    }


def buy_fuel():
    pass


def buy_news():
    print("Buying news!")


def warp():
    pass


def attack():
    pass


def flee():
    pass


def ignore():
    pass


def orbit_trade():
    """This is when a trader encounter requests to trade with the player"""
    pass


def repair():
    pass


def buy_pod():
    pass


def get_ware_list() -> list[str]:
    return e.Ware.lst()


def buy_good():
    pass


def sell_good():
    pass


def buy_ship():
    pass


def buy_equipment():
    pass


def sell_equipment():
    pass


def hire_crew():
    pass


def fire_crew():
    pass


def buy_insurance():
    pass


def get_loan():
    pass
