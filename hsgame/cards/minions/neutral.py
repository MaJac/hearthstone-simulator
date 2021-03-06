from hsgame.cards.battlecries import draw_card, silence, deal_one_damage, \
    gain_one_health_for_each_card_in_hand, deal_two_damage, heal_two, \
    heal_three, give_enemy_crystal, darkscale_healer, priestess_of_elune, \
    destroy_target, two_temp_attack, nightblade, ssc
from hsgame.game_objects import Minion, MinionCard
from hsgame.constants import CARD_RARITY, CHARACTER_CLASS, MINION_TYPE
import hsgame.targeting


class BloodfenRaptor(MinionCard):
    def __init__(self):
        super().__init__("Bloodfen Raptor", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(3, 2, MINION_TYPE.BEAST)


class ElvenArcher(MinionCard):
    def __init__(self):
        super().__init__("Elven Archer", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_battlecry_target)

    def create_minion(self, player):
        return Minion(1, 1, battlecry=deal_one_damage)


class NoviceEngineer(MinionCard):
    def __init__(self):
        super().__init__("Novice Engineer", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(1, 1, battlecry=draw_card)


class StonetuskBoar(MinionCard):
    def __init__(self):
        super().__init__("Stonetusk Boar", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        minion = Minion(1, 1, MINION_TYPE.BEAST)
        minion.charge = True
        return minion


class IronbeakOwl(MinionCard):
    def __init__(self):
        super().__init__("Ironbeak Owl", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_minion_battlecry_target)

    def create_minion(self, player):
        return Minion(2, 1, MINION_TYPE.BEAST, battlecry=silence)


class WarGolem(MinionCard):
    def __init__(self):
        super().__init__("War Golem", 7, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(7, 7)


class MogushanWarden(MinionCard):
    def __init__(self):
        super().__init__("Mogu'shan Warden", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 7)
        minion.taunt = True
        return minion


class FaerieDragon(MinionCard):
    def __init__(self):
        super().__init__("Faerie Dragon", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        def silence():
            minion.spell_targettable = lambda: True

        minion = Minion(3, 2, MINION_TYPE.DRAGON)
        minion.spell_targettable = lambda: False
        minion.bind("silenced", silence)
        return minion


class KoboldGeomancer(MinionCard):
    def __init__(self):
        super().__init__("Kobold Geomancer", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 2)
        minion.spell_damage = 1
        return minion


class ArgentSquire(MinionCard):
    def __init__(self):
        super().__init__("Argent Squire", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 1)
        minion.divine_shield = True
        return minion


class SilvermoonGuardian(MinionCard):
    def __init__(self):
        super().__init__("Silvermoon Guardian", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(3, 3)
        minion.divine_shield = True
        return minion


class TwilightDrake(MinionCard):
    def __init__(self):
        super().__init__("Twilight Drake", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        return Minion(4, 1, MINION_TYPE.DRAGON,
                      battlecry=gain_one_health_for_each_card_in_hand)


class MagmaRager(MinionCard):
    def __init__(self):
        super().__init__("Magma Rager", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(5, 1)


class DireWolfAlpha(MinionCard):
    def __init__(self):
        super().__init__("Dire Wolf Alpha", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):

        def add_effect(m, index):
            m.add_aura(1, 0, lambda mini: mini.index is m.index - 1 or mini.index is m.index + 1)

        minion = Minion(2, 2, MINION_TYPE.BEAST)
        minion.bind("added_to_board", add_effect)
        return minion


class WorgenInfiltrator(MinionCard):
    def __init__(self):
        super().__init__("Worgen Infiltrator", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 1)
        minion.stealth = True
        return minion


class Archmage(MinionCard):
    def __init__(self):
        super().__init__("Archmage", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(4, 7)
        minion.spell_damage = 1
        return minion


class DalaranMage(MinionCard):
    def __init__(self):
        super().__init__("Dalaran Mage", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 4)
        minion.spell_damage = 1
        return minion


class Malygos(MinionCard):
    def __init__(self):
        super().__init__("Malygos", 9, CHARACTER_CLASS.ALL,
                         CARD_RARITY.LEGENDARY)

    def create_minion(self, player):
        minion = Minion(4, 12, MINION_TYPE.DRAGON)
        minion.spell_damage = 5
        return minion


class AzureDrake(MinionCard):
    def __init__(self):
        super().__init__("Azure Drake", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        minion = Minion(4, 4, MINION_TYPE.DRAGON, battlecry=draw_card)
        minion.spell_damage = 1
        return minion


class OgreMagi(MinionCard):
    def __init__(self):
        super().__init__("Ogre Magi", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(4, 4)
        minion.spell_damage = 1
        return minion


class Spellbreaker(MinionCard):
    def __init__(self):
        super().__init__("Spellbreaker", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_minion_battlecry_target)

    def create_minion(self, player):
        return Minion(4, 3, battlecry=silence)


class BloodmageThalnos(MinionCard):
    def __init__(self):
        super().__init__("Bloodmage Thalnos", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.LEGENDARY)

    def create_minion(self, player):
        minion = Minion(1, 1, deathrattle=draw_card)
        minion.spell_damage = 1
        return minion


class LootHoarder(MinionCard):
    def __init__(self):
        super().__init__("Loot Hoarder", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 1, deathrattle=draw_card)
        return minion


class LeperGnome(MinionCard):  # idk, maybe this will work
    def __init__(self):
        super().__init__("Leper Gnome", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        enemy_hero = player.game.other_player

        def deal_enemy_hero_two_damage(minion):
            enemy_hero.damage(2)

        minion = Minion(2, 1)
        minion.deathrattle = deal_enemy_hero_two_damage
        return minion


class IronforgeRifleman(MinionCard):
    def __init__(self):
        super().__init__("Ironforge Rifleman", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_battlecry_target)

    def create_minion(self, player):
        return Minion(2, 2, battlecry=deal_one_damage)


class GnomishInventor(MinionCard):
    def __init__(self):
        super().__init__("Gnomish Inventor", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(2, 4, battlecry=draw_card)


class GoldshireFootman(MinionCard):
    def __init__(self):
        super().__init__("Goldshire Footman", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 2)
        minion.taunt = True
        return minion


class FrostwolfGrunt(MinionCard):
    def __init__(self):
        super().__init__("Frostwolf Grunt", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 2)
        minion.taunt = True
        return minion


class IronfurGrizzly(MinionCard):
    def __init__(self):
        super().__init__("Ironfur Grizzly", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(3, 3, MINION_TYPE.BEAST)
        minion.taunt = True
        return minion


class LordOfTheArena(MinionCard):
    def __init__(self):
        super().__init__("Lord of the Arena", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(6, 5)
        minion.taunt = True
        return minion


class MurlocRaider(MinionCard):
    def __init__(self):
        super().__init__("Murloc Raider", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(2, 1, MINION_TYPE.MURLOC)


class ManaAddict(MinionCard):
    def __init__(self):
        super().__init__("Mana Addict", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        def increase_attack(card):
            minion.change_temp_attack(2)

        minion = Minion(1, 3)
        player.bind("spell_cast", increase_attack)
        minion.bind_once("silenced", lambda: player.unbind("spell_cast",
                                                           increase_attack))
        return minion


class OasisSnapjaw(MinionCard):
    def __init__(self):
        super().__init__("Oasis Snapjaw", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(2, 7, MINION_TYPE.BEAST)


class RecklessRocketeer(MinionCard):
    def __init__(self):
        super().__init__("Reckless Rocketeer", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        minion = Minion(5, 2)
        minion.charge = True
        return minion


class RiverCrocolisk(MinionCard):
    def __init__(self):
        super().__init__("River Crocolisk", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(2, 3, MINION_TYPE.BEAST)


class SenjinShieldmasta(MinionCard):
    def __init__(self):
        super().__init__("Sen'jin Shieldmasta", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        minion = Minion(3, 5)
        minion.taunt = True
        return minion


class ScarletCrusader(MinionCard):
    def __init__(self):
        super().__init__("Scarlet Crusader", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(3, 1)
        minion.divine_shield = True
        return minion


class Shieldbearer(MinionCard):
    def __init__(self):
        super().__init__("Shieldbearer", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(0, 4)
        minion.taunt = True
        return minion


class SilverbackPatriarch(MinionCard):
    def __init__(self):
        super().__init__("Silverback Patriarch", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 4, MINION_TYPE.BEAST)
        minion.taunt = True
        return minion


class JunglePanther(MinionCard):
    def __init__(self):
        super().__init__("Jungle Panther", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(4, 2, MINION_TYPE.BEAST)
        minion.stealth = True
        return minion


class RavenholdtAssassin(MinionCard):
    def __init__(self):
        super().__init__("Ravenholdt Assassin", 7, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        minion = Minion(7, 5)
        minion.stealth = True
        return minion


class StormpikeCommando(MinionCard):
    def __init__(self):
        super().__init__("Stormpike Commando", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_battlecry_target)

    def create_minion(self, player):
        return Minion(4, 2, battlecry=deal_two_damage)


class StormwindKnight(MinionCard):
    def __init__(self):
        super().__init__("Stormwind Knight", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 5)
        minion.charge = True
        return minion


class StranglethornTiger(MinionCard):
    def __init__(self):
        super().__init__("Stranglethorn Tiger", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(5, 5, MINION_TYPE.BEAST)
        minion.stealth = True
        return minion


class Sunwalker(MinionCard):
    def __init__(self):
        super().__init__("Sunwalker", 6, CHARACTER_CLASS.ALL, CARD_RARITY.RARE)

    def create_minion(self, player):
        minion = Minion(4, 5)
        minion.divine_shield = True
        minion.taunt = True
        return minion


class ThrallmarFarseer(MinionCard):
    def __init__(self):
        super().__init__("Thrallmar Farseer", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 3)
        minion.windfury = True
        return minion


class WindfuryHarpy(MinionCard):
    def __init__(self):
        super().__init__("Windfury Harpy", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(4, 5)
        minion.windfury = True
        return minion


class YoungDragonhawk(MinionCard):
    def __init__(self):
        super().__init__("Young Dragonhawk", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(1, 1, MINION_TYPE.BEAST)
        minion.windfury = True
        return minion


class Wolfrider(MinionCard):
    def __init__(self):
        super().__init__("Wolfrider", 3, CHARACTER_CLASS.ALL, CARD_RARITY.FREE)

    def create_minion(self, player):
        minion = Minion(3, 1)
        minion.charge = True
        return minion


class BootyBayBodyguard(MinionCard):
    def __init__(self):
        super().__init__("Booty Bay Bodyguard", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(5, 4)
        minion.taunt = True
        return minion


class BoulderfistOgre(MinionCard):
    def __init__(self):
        super().__init__("Boulderfist Ogre", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(6, 7)


class ChillwindYeti(MinionCard):
    def __init__(self):
        super().__init__("Chillwind Yeti", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(4, 5)


class CoreHound(MinionCard):
    def __init__(self):
        super().__init__("Core Hound", 7, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(9, 5, MINION_TYPE.BEAST)


class VoodooDoctor(MinionCard):
    def __init__(self):
        super().__init__("Voodoo Doctor", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE,
                         hsgame.targeting.find_battlecry_target)

    def create_minion(self, player):
        return Minion(2, 1, battlecry=heal_two)


class EarthenRingFarseer(MinionCard):
    def __init__(self):
        super().__init__("Earthen Ring Farseer", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_battlecry_target)

    def create_minion(self, player):
        return Minion(3, 3, battlecry=heal_three)


class ArcaneGolem(MinionCard):
    def __init__(self):
        super().__init__("Arcane Golem", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        minion = Minion(4, 2, battlecry=give_enemy_crystal)
        minion.charge = True
        return minion


class PriestessOfElune(MinionCard):
    def __init__(self):
        super().__init__("Priestess of Elune", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(5, 4, battlecry=priestess_of_elune)
        return minion


class DarkscaleHealer(MinionCard):
    def __init__(self):
        super().__init__("Darkscale Healer", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(4, 5, battlecry=darkscale_healer)
        return minion


class ArgentCommander(MinionCard):
    def __init__(self):
        super().__init__("Argent Commander", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        minion = Minion(4, 2)
        minion.divine_shield = True
        minion.charge = True
        return minion


class BluegillWarrior(MinionCard):
    def __init__(self):
        super().__init__("Bluegill Warrior", 2, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(2, 1, MINION_TYPE.MURLOC)
        minion.charge = True
        return minion


class Wisp(MinionCard):
    def __init__(self):
        super().__init__("Wisp", 0, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        return Minion(1, 1)


class Nightblade(MinionCard):
    def __init__(self):
        super().__init__("Nightblade", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.FREE)

    def create_minion(self, player):
        return Minion(4, 4, battlecry=nightblade)


class ShatteredSunCleric(MinionCard):
    def __init__(self):
        super().__init__("Shattered Sun Cleric", 3, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_friendly_minion_battlecry_target)

    def create_minion(self, player):
        return Minion(3, 2, battlecry=ssc)


class TheBlackKnight(MinionCard):
    def __init__(self):
        super().__init__("The Black Knight", 6, CHARACTER_CLASS.ALL,
                         CARD_RARITY.LEGENDARY,
                         hsgame.targeting.find_minion_battlecry_target,
                         lambda minion: minion.taunt)

    def create_minion(self, player):
        return Minion(4, 5, battlecry=destroy_target)


class AbusiveSergeant(MinionCard):
    def __init__(self):
        super().__init__("Abusive Sergeant", 1, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_minion_battlecry_target)

    def create_minion(self, player):
        return Minion(2, 1, battlecry=two_temp_attack)


class DarkIronDwarf(MinionCard):
    def __init__(self):
        super().__init__("Dark Iron Dwarf", 4, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_minion_battlecry_target)

    def create_minion(self, player):
        return Minion(4, 4, battlecry=two_temp_attack)


class Abomination(MinionCard):
    def __init__(self):
        super().__init__("Abomination", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.RARE)

    def create_minion(self, player):
        def deal_two_to_all(minion):
            for target in hsgame.targeting.find_spell_target(player.game,
                                                             lambda x: True):
                target.damage(2, self)

        return Minion(4, 4, deathrattle=deal_two_to_all, taunt=True)


class FenCreeper(MinionCard):
    def __init__(self):
        super().__init__("Fen Creeper", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        minion = Minion(3, 6)
        minion.taunt = True
        return minion


class VentureCoMercenary(MinionCard):
    def __init__(self):
        super().__init__("Venture Co. Mercenary", 5, CHARACTER_CLASS.ALL,
                         CARD_RARITY.COMMON)

    def create_minion(self, player):
        class Filter:
            def __init__(self):
                self.amount = -3
                self.filter = lambda c: not c.is_spell()
                self.min = 0

        filter = Filter()
        minion = Minion(7, 6)
        minion.bind_once("silenced",
                         lambda: player.mana_filters.remove(filter))
        player.mana_filters.append(filter)
        return minion


class AmaniBerserker(MinionCard):
    def __init__(self):
        super().__init__("Amani Berserker", 2, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        def increase_attack():
            minion.change_attack(3)

        def decrease_attack():
            minion.change_attack(-3)

        def silenced():
            minion.unbind("enraged", increase_attack)
            minion.unbind("unenraged", decrease_attack)

        minion = Minion(2, 3)
        minion.bind("enraged", increase_attack)
        minion.bind("unenraged", decrease_attack)
        minion.bind("silenced", silenced)
        return minion


class SilverHandKnight(MinionCard):
    def __init__(self):
        super().__init__("Silver Hand Knight", 5, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):
        def summon_squire(m):
            class Squire(MinionCard):
                def __init__(self):
                    super().__init__("Squire", 1, CHARACTER_CLASS.ALL, CARD_RARITY.SPECIAL)

                def create_minion(self, player):
                    return Minion(2, 2)

            Squire().summon(player, player.game, m.index)

        return Minion(4, 4, battlecry=summon_squire)


class StormwindChampion(MinionCard):
    def __init__(self):
        super().__init__("Stormwind Champion", 7, CHARACTER_CLASS.ALL, CARD_RARITY.COMMON)

    def create_minion(self, player):

        def add_effect(m, index):
            m.add_aura(1, 1, lambda mini: mini is not minion)

        minion = Minion(6, 6)
        minion.bind("added_to_board", add_effect)
        return minion


class EmperorCobra(MinionCard):
    def __init__(self):
        super().__init__("Emperor Cobra", 3, CHARACTER_CLASS.ALL, CARD_RARITY.RARE)

    def create_minion(self, player):
        def poisonous(amount, target):
            if type(target) is Minion and not target.dead:
                target.die(self)

        minion = Minion(2, 3, MINION_TYPE.BEAST)
        minion.bind("did_damage", poisonous)
        minion.bind_once("silenced", lambda: minion.unbind("did_damage", poisonous))
        return minion
