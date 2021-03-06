import random
import unittest

from hsgame.constants import MINION_TYPE
from tests.testing_agents import *
from tests.testing_utils import generate_game_for
from hsgame.cards import *


class TestWarlock(unittest.TestCase):
    def setUp(self):
        random.seed(1857)

    def test_MortalCoil(self):
        game = generate_game_for(BloodfenRaptor, MortalCoil, DoNothingBot, OneSpellTestingAgent)

        raptor = BloodfenRaptor()
        raptor.summon(game.players[0], game, 0)
        # player 0 plays raptor
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(2, game.players[0].minions[0].health)
        self.assertEqual(4, len(game.players[1].hand))

        game.play_single_turn()
        game.play_single_turn()
        # mortal coils the 2hp raptor
        self.assertEqual(4, len(game.players[1].hand))
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(1, game.players[0].minions[0].health)

        game.play_single_turn()
        game.play_single_turn()
        # mortal coils the 1hp raptor and draws
        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(5, len(game.players[1].hand))

    def test_MortalCoilDivineShield(self):
        game = generate_game_for(StonetuskBoar, MortalCoil, DoNothingBot, OneSpellTestingAgent)

        scarlet = ScarletCrusader()
        scarlet.summon(game.players[0], game, 0)
        # player 0 plays Scarlet Crusader
        self.assertTrue(game.players[0].minions[0].divine_shield)
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(1, game.players[0].minions[0].health)
        self.assertEqual(4, len(game.players[1].hand))

        game.play_single_turn()
        game.play_single_turn()
        # mortal coils the divine shield, no draw
        self.assertFalse(game.players[0].minions[0].divine_shield)
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(1, game.players[0].minions[0].health)
        self.assertEqual(4, len(game.players[1].hand))

        game.play_single_turn()
        game.play_single_turn()
        # mortal coils the 1hp scarlet crusader and draws
        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(5, len(game.players[1].hand))

    def test_FlameImp(self):
        game = generate_game_for(FlameImp, StonetuskBoar, MinionPlayingAgent, DoNothingBot)

        game.play_single_turn()
        # play Flame Imp, 3 damage to own hero
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(27, game.players[0].hero.health)

    def test_PitLord(self):
        game = generate_game_for(PitLord, StonetuskBoar, MinionPlayingAgent, DoNothingBot)
        for turn in range(0, 7):
            game.play_single_turn()
            # play Pit Lord, 5 damage to own hero
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(25, game.players[0].hero.health)

    def test_DreadInfernal(self):
        game = generate_game_for(DreadInfernal, StonetuskBoar, MinionPlayingAgent, MinionPlayingAgent)
        for turn in range(0, 10):
            game.play_single_turn()
        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(30, game.players[0].hero.health)
        self.assertEqual(5, len(game.players[1].minions))
        self.assertEqual(30, game.players[1].hero.health)

        game.play_single_turn()
        # Plays Dread Infernal, 1 damage to all
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(6, game.players[0].minions[0].health)
        self.assertEqual(29, game.players[0].hero.health)
        self.assertEqual(0, len(game.players[1].minions))
        self.assertEqual(29, game.players[1].hero.health)

    def test_Felguard(self):
        game = generate_game_for(Felguard, StonetuskBoar, MinionPlayingAgent, DoNothingBot)
        for turn in range(0, 4):
            game.play_single_turn()

        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(2, game.players[0].max_mana)

        game.play_single_turn()
        # Plays Felguard, destroys mana crystal
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(2, game.players[0].max_mana)

    def test_Succubus(self):
        game = generate_game_for(Succubus, StonetuskBoar, MinionPlayingAgent, DoNothingBot)
        for turn in range(0, 2):
            game.play_single_turn()

        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(4, len(game.players[0].hand))

        game.play_single_turn()
        # Plays Succubus, discards
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(3, len(game.players[0].hand))

    def test_Doomguard(self):
        game = generate_game_for(Doomguard, StonetuskBoar, MinionPlayingAgent, DoNothingBot)
        for turn in range(0, 8):
            game.play_single_turn()

        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(7, len(game.players[0].hand))

        game.play_single_turn()
        # Plays Doomguard, discards twice
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(5, len(game.players[0].hand))

    def test_Hellfire(self):
        game = generate_game_for(Hellfire, SilverbackPatriarch, SpellTestingAgent, MinionPlayingAgent)
        for turn in range(0, 6):
            game.play_single_turn()
            # plays 1 Silverback Patriarch
        self.assertEqual(1, len(game.players[1].minions))
        self.assertEqual(30, game.players[0].hero.health)
        self.assertEqual(4, game.players[1].minions[0].health)
        self.assertEqual(30, game.players[1].hero.health)

        game.play_single_turn()
        # Plays Hellfire, 3 damage to all
        self.assertEqual(1, len(game.players[1].minions))
        self.assertEqual(1, game.players[1].minions[0].health)
        self.assertEqual(27, game.players[0].hero.health)
        self.assertEqual(27, game.players[1].hero.health)

    def test_ShadowBolt(self):
        game = generate_game_for(ShadowBolt, SilverbackPatriarch, SpellTestingAgent, MinionPlayingAgent)
        for turn in range(0, 6):
            game.play_single_turn()
            # Plays Silverback Patriarch
        self.assertEqual(1, len(game.players[1].minions))
        self.assertEqual(30, game.players[0].hero.health)
        self.assertEqual(4, game.players[1].minions[0].health)
        self.assertEqual(30, game.players[1].hero.health)

        game.play_single_turn()
        # Uses Shadow Bolt
        self.assertEqual(0, len(game.players[1].minions))

    def test_DrainLife(self):
        game = generate_game_for(DrainLife, MindBlast, EnemySpellTestingAgent, SpellTestingAgent)
        for turn in range(0, 4):
            game.play_single_turn()
            # Uses Mind Blast
        self.assertEqual(25, game.players[0].hero.health)
        self.assertEqual(30, game.players[1].hero.health)

        game.play_single_turn()
        # Uses Drain Life
        self.assertEqual(27, game.players[0].hero.health)
        self.assertEqual(28, game.players[1].hero.health)

    def test_Soulfire(self):
        game = generate_game_for(Soulfire, StonetuskBoar, EnemySpellTestingAgent, DoNothingBot)

        game.play_single_turn()
        # It should play 2 copies of Soulfire at the enemy hero and discard the remaining 2 copies
        self.assertEqual(0, len(game.players[0].hand))
        self.assertEqual(22, game.players[1].hero.health)
        self.assertEqual(30, game.players[0].hero.health)

    def test_TwistingNether(self):
        game = generate_game_for(TwistingNether, SilverbackPatriarch, SpellTestingAgent, MinionPlayingAgent)
        for turn in range(0, 14):
            game.play_single_turn()
            # Plays Silverback Patriarch each turn
        self.assertEqual(5, len(game.players[1].minions))

        game.play_single_turn()
        # Plays Twisting Nether
        self.assertEqual(0, len(game.players[1].minions))

    def test_DemonfireEnemy(self):
        game = generate_game_for(Demonfire, FlameImp, EnemyMinionSpellTestingAgent, MinionPlayingAgent)
        for turn in range(0, 2):
            game.play_single_turn()
            # play Flame Imp, 3 damage to own hero
        self.assertEqual(1, len(game.players[1].minions))
        self.assertEqual(27, game.players[1].hero.health)

        game.play_single_turn()
        # Demonfire to kill enemy Flame Imp
        self.assertEqual(0, len(game.players[1].minions))

    def test_DemonfireAlly(self):
        game = generate_game_for(Demonfire, StonetuskBoar, SpellTestingAgent, DoNothingBot)
        imp = FlameImp()
        imp.summon(game.players[0], game, 0)

        for turn in range(0, 2):
            game.play_single_turn()

        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(30, game.players[0].hero.health)  # summon doesnt trigger battlecry

        game.play_single_turn()
        # Demonfire to buff own Flame Imp
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(4, game.players[0].minions[0].health)
        self.assertEqual(5, game.players[0].minions[0].calculate_attack())

    def test_DemonfireAllyNonDemon(self):
        game = generate_game_for(Demonfire, StonetuskBoar, SpellTestingAgent, DoNothingBot)
        raptor = BloodfenRaptor()
        raptor.summon(game.players[0], game, 0)

        for turn in range(0, 2):
            game.play_single_turn()

        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(30, game.players[0].hero.health)

        game.play_single_turn()
        # Demonfire to kill own Raptor
        self.assertEqual(0, len(game.players[0].minions))

    def test_SacrificialPact(self):
        game = generate_game_for(MindBlast, SacrificialPact, SpellTestingAgent, SpellTestingAgent)
        for turn in range(0, 3):
            game.play_single_turn()
            # Uses 1 Mindblast
        self.assertEqual(25, game.players[1].hero.health)
        imp = FlameImp()
        imp.summon(game.players[0], game, 0)

        game.play_single_turn()
        # Pact the Imp
        self.assertEqual(30, game.players[1].hero.health)

    def test_SiphonSoul(self):
        game = generate_game_for(MindBlast, SiphonSoul, OneSpellTestingAgent, SpellTestingAgent)
        for turn in range(0, 11):
            game.play_single_turn()
            # Uses Mindblast for 5 turns
        self.assertEqual(5, game.players[1].hero.health)
        boar = StonetuskBoar()
        boar.summon(game.players[0], game, 0)

        game.play_single_turn()
        # Siphon Soul on the Boar
        self.assertEqual(8, game.players[1].hero.health)

    def test_SenseDemons(self):
        game = generate_game_for([SenseDemons, Doomguard], StonetuskBoar, SpellTestingAgent, DoNothingBot)
        for turn in range(0, 4):
            game.play_single_turn()
        self.assertEqual(5, len(game.players[0].hand))

        game.play_single_turn()
        # plays Sense Demons and draws 2 Doomguards
        self.assertEqual(7, len(game.players[0].hand))
        self.assertEqual('Doomguard', game.players[0].hand[5].name)
        self.assertEqual('Doomguard', game.players[0].hand[6].name)

    def test_SenseDemonsNoDemons(self):
        game = generate_game_for(SenseDemons, StonetuskBoar, SpellTestingAgent, DoNothingBot)
        for turn in range(0, 4):
            game.play_single_turn()
        self.assertEqual(5, len(game.players[0].hand))

        game.play_single_turn()
        # plays Sense Demons and draws 2 Doomguards
        self.assertEqual(7, len(game.players[0].hand))
        self.assertEqual('Worthless Imp', game.players[0].hand[5].name)
        self.assertEqual('Worthless Imp', game.players[0].hand[6].name)

    def test_BaneOfDoom(self):
        game = generate_game_for(BaneOfDoom, StonetuskBoar, EnemyMinionSpellTestingAgent, DoNothingBot)
        imp = FlameImp()
        imp.summon(game.players[1], game, 0)

        for turn in range(0, 8):
            game.play_single_turn()

        self.assertEqual(1, len(game.players[1].minions))

        game.play_single_turn()
        # Kills enemy Imp with Bane of Doom and summons random demon
        self.assertEqual(1, len(game.players[0].minions))
        self.assertEqual(0, len(game.players[1].minions))
        self.assertEqual(MINION_TYPE.DEMON, game.players[0].minions[0].minion_type)
        self.assertEqual("Dread Infernal", game.players[0].minions[0].card.name)

        # Apparently this seed always rolls Dread Infernal

    def test_Corruption(self):
        game = generate_game_for(Corruption, StonetuskBoar, EnemyMinionSpellTestingAgent, DoNothingBot)
        imp = FlameImp()
        imp.summon(game.players[1], game, 0)
        self.assertEqual(1, len(game.players[1].minions))

        game.play_single_turn()
        # Casts Corruption on enemy Imp
        self.assertEqual(1, len(game.players[1].minions))
        self.assertEqual(3, len(game.players[0].hand))

        game.play_single_turn()
        # Enemy minion still alive until start of my turn
        self.assertEqual(1, len(game.players[1].minions))

        game.play_single_turn()
        # Corruption resolves at start of my turn, no targets to use remaining cards on
        self.assertEqual(0, len(game.players[1].minions))
        self.assertEqual(4, len(game.players[0].hand))

    def test_PowerOverwhelming(self):
        game = generate_game_for(PowerOverwhelming, StonetuskBoar, SpellTestingAgent, DoNothingBot)
        imp = FlameImp()
        imp.summon(game.players[0], game, 0)
        self.assertEqual(1, len(game.players[0].minions))

        def verify_poweroverwhelming():
            self.assertEqual(7, game.players[0].minions[0].calculate_attack())
            self.assertEqual(6, game.players[0].minions[0].health)

        game.players[0].minions[0].bind("health_changed", verify_poweroverwhelming)
        game.play_single_turn()

        self.assertEqual(0, len(game.players[0].minions))
        self.assertEqual(3, len(game.players[0].hand))
