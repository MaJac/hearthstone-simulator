from hsgame.constants import CHARACTER_CLASS, CARD_RARITY, MINION_TYPE
from hsgame.game_objects import Card, Minion, MinionCard, SecretCard
import hsgame.targeting


class ArcaneMissiles(Card):
    def __init__(self):
        super().__init__("Arcane Missiles", 1, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.FREE)

    def use(self, player, game):
        super().use(player, game)
        for i in range(0, player.effective_spell_damage(3)):
            targets = game.other_player.minions.copy()
            targets.append(game.other_player.hero)
            target = targets[game.random(0, len(targets) - 1)]
            target.damage(1, self)


class IceLance(Card):
    def __init__(self):
        super().__init__("Ice Lance", 1, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_spell_target)

    def use(self, player, game):
        super().use(player, game)
        if self.target.frozen:
            self.target.damage(4, self)
        else:
            self.target.freeze()


class MirrorImage(Card):
    def __init__(self):
        super().__init__("Mirror Image", 1, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON)

    def use(self, player, game):
        super().use(player, game)

        class MirrorImageMinion(MinionCard):
            def __init__(self):
                super().__init__("Mirror Image", 0, CHARACTER_CLASS.MAGE,
                                 CARD_RARITY.SPECIAL)

            def create_minion(self, p):
                minion = Minion(0, 2)
                minion.taunt = True
                return minion

        for i in range(0, 2):
            mirror_image = MirrorImageMinion()
            mirror_image.summon(player, game, len(player.minions))


class ArcaneExplosion(Card):
    def __init__(self):
        super().__init__("Arcane Explosion", 2, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.FREE)

    def use(self, player, game):
        super().use(player, game)
        for minion in game.other_player.minions.copy():
            minion.damage(player.effective_spell_damage(1), self)


class Frostbolt(Card):
    def __init__(self):
        super().__init__("Frostbolt", 2, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_spell_target)

    def use(self, player, game):
        super().use(player, game)
        self.target.damage(player.effective_spell_damage(3), self)
        self.target.freeze()


class ArcaneIntellect(Card):
    def __init__(self):
        super().__init__("Arcane Intellect", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.FREE)

    def use(self, player, game):
        super().use(player, game)
        for c in range(0, 2):
            player.draw()


class FrostNova(Card):
    def __init__(self):
        super().__init__("Frost Nova", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON)

    def use(self, player, game):
        super().use(player, game)
        for minion in game.other_player.minions:
            minion.freeze()


class Counterspell(SecretCard):
    def __init__(self):
        super().__init__("Counterspell", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.RARE)

    def use(self, player, game):
        super().use(player, game)

    def _reveal(self, card):
        card.cancel = True
        super().reveal()

    def activate(self, player):
        player.game.current_player.bind_once("spell_cast", self._reveal)

    def deactivate(self, player):
        player.game.current_player.unbind("spell_cast", self._reveal)


class IceBarrier(SecretCard):
    def __init__(self):
        super().__init__("Ice Barrier", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON)

    def _reveal(self, attacker, player):
        player.hero.armour += 8
        super().reveal()

    def activate(self, player):
        player.hero.bind_once("attacked", self._reveal, player)

    def deactivate(self, player):
        player.hero.unbind("attacked", self._reveal)


class MirrorEntity(SecretCard):
    def __init__(self):
        super().__init__("Mirror Entity", 3, CHARACTER_CLASS.MAGE, CARD_RARITY.COMMON)

    def _reveal(self, minion, player):
        mirror = minion.copy(player)
        mirror.add_to_board(len(player.minions))
        super().reveal()

    def activate(self, player):
        player.game.current_player.bind_once("minion_played", self._reveal, player)

    def deactivate(self, player):
        player.game.current_player.unbind("minion_played", self._reveal)


class Spellbender(SecretCard):
    def __init__(self):
        super().__init__("Spellbender", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.EPIC)

    def _reveal(self, card, player):
        if card.targetable:
            class SpellbenderMinion(MinionCard):
                def __init__(self):
                    super().__init__("Spellbender", 0, CHARACTER_CLASS.MAGE,
                                     CARD_RARITY.SPECIAL)

                def create_minion(self, p):
                    return Minion(1, 3)

            def choose_bender(targets):
                spell_bender = SpellbenderMinion()
                # TODO test what happens if Spellbender goes off when there are 7 minions down
                spell_bender.summon(player, player.game, len(player.minions))
                player.game.current_player.agent.choose_target = old_target
                return player.minions[-1]

            old_target = player.game.current_player.agent.choose_target
            player.game.current_player.agent.choose_target = choose_bender
            super().reveal()
        else:
            self.activate(player)

    def activate(self, player):
        player.game.current_player.bind_once("spell_cast", self._reveal,
                                             player)

    def deactivate(self, player):
        player.game.current_player.unbind("spell_cast", self._reveal)


class Vaporize(SecretCard):
    def __init__(self):
        super().__init__("Vaporize", 3, CHARACTER_CLASS.MAGE, CARD_RARITY.RARE)

    def _reveal(self, attacker):
        if type(attacker) is Minion:
            attacker.die(self)
            attacker.activate_delayed()
            super().reveal()
        else:
            self.activate(attacker.player.game.other_player)

    def activate(self, player):
        player.hero.bind_once("attacked", self._reveal)

    def deactivate(self, player):
        player.hero.unbind("attacked", self._reveal)


class IceBlock(SecretCard):
    def __init__(self):
        super().__init__("Ice Block", 3, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.EPIC)

    def _reveal(self, amount, attacker, player):
        if player.hero.health - amount <= 0:
            player.hero.immune = True
            player.hero.health += amount
            # TODO Check if this spell will also prevent damage to armour.
            super().reveal()
            player.hero.unbind("secret_damaged", self._reveal)

    def activate(self, player):
        player.hero.bind("secret_damaged", self._reveal, player)

    def deactivate(self, player):
        player.hero.unbind("secret_damaged", self._reveal)


class ConeOfCold(Card):
    def __init__(self):
        super().__init__("Cone of Cold", 4, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON,
                         hsgame.targeting.find_minion_spell_target)

    def use(self, player, game):
        super().use(player, game)

        self.target.damage(player.effective_spell_damage(1), self)
        self.target.freeze()
        index = self.target.index
        if self.target.index > 0:
            minion = self.target.player.minions[index - 1]
            minion.damage(player.effective_spell_damage(1), self)
            minion.freeze()

        if self.target.index < len(self.target.player.minions) - 1:
            minion = self.target.player.minions[index + 1]
            minion.damage(player.effective_spell_damage(1), self)
            minion.freeze()


class Fireball(Card):
    def __init__(self):
        super().__init__("Fireball", 4, CHARACTER_CLASS.MAGE, CARD_RARITY.FREE,
                         hsgame.targeting.find_spell_target)

    def use(self, player, game):
        super().use(player, game)
        self.target.damage(player.effective_spell_damage(6), self)


class Polymorph(Card):
    def __init__(self):
        super().__init__("Polymorph", 4, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.FREE,
                         hsgame.targeting.find_minion_spell_target)

    def use(self, player, game):
        super().use(player, game)

        class Sheep(MinionCard):
            def __init__(self):
                super().__init__("Sheep", 0, CHARACTER_CLASS.ALL,
                                 CARD_RARITY.SPECIAL)

            def create_minion(self, p):
                return Minion(1, 1, MINION_TYPE.BEAST)

        sheep = Sheep()
        minion = sheep.create_minion(None)
        minion.card = sheep
        self.target.replace(minion)


class Blizzard(Card):
    def __init__(self):
        super().__init__("Blizzard", 6, CHARACTER_CLASS.MAGE, CARD_RARITY.RARE)

    def use(self, player, game):
        super().use(player, game)
        for minion in game.other_player.minions.copy():
            minion.damage(player.effective_spell_damage(2), self)
            minion.freeze()


class Flamestrike(Card):
    def __init__(self):
        super().__init__("Flamestrike", 7, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.COMMON)

    def use(self, player, game):
        super().use(player, game)
        for minion in game.other_player.minions.copy():
            minion.damage(player.effective_spell_damage(4), self)


class Pyroblast(Card):
    def __init__(self):
        super().__init__("Pyroblast", 10, CHARACTER_CLASS.MAGE,
                         CARD_RARITY.EPIC, hsgame.targeting.find_spell_target)

    def use(self, player, game):
        super().use(player, game)
        self.target.damage(player.effective_spell_damage(10), self)
