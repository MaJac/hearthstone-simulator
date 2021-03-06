class CARD_RARITY:
    FREE = 1
    COMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    SPECIAL = -1

    __rarities = {
        "FREE": FREE,
        "COMMON": COMMON,
        "RARE": RARE,
        "EPIC": EPIC,
        "LEGENDARY": LEGENDARY,
        "SPECIAL": SPECIAL,
    }

    @staticmethod
    def from_str(rarity_name):
        return CARD_RARITY.__rarities[rarity_name.upper()]


class CHARACTER_CLASS:
    ALL = 0
    MAGE = 1
    HUNTER = 2
    SHAMAN = 3
    WARRIOR = 4
    DRUID = 5
    PRIEST = 6
    PALADIN = 7
    ROGUE = 8
    WARLOCK = 9

    __classes = {
        "MAGE": MAGE,
        "HUNTER": HUNTER,
        "SHAMAN": SHAMAN,
        "WARRIOR": WARRIOR,
        "DRUID": DRUID,
        "PRIEST": PRIEST,
        "PALADIN": PALADIN,
        "ROGUE": ROGUE,
        "WARLOCK": WARLOCK,
        "": ALL,
    }

    @staticmethod
    def from_str(class_name):
        return CHARACTER_CLASS.__classes[class_name.upper()]

    @staticmethod
    def to_str(class_number):
        classes = {
            CHARACTER_CLASS.MAGE: "Mage",
            CHARACTER_CLASS.HUNTER: "Hunter",
            CHARACTER_CLASS.SHAMAN: "Shaman",
            CHARACTER_CLASS.WARRIOR: "Warrior",
            CHARACTER_CLASS.DRUID: "Druid",
            CHARACTER_CLASS.PRIEST: "Priest",
            CHARACTER_CLASS.PALADIN: "Paladin",
            CHARACTER_CLASS.ROGUE: "Rogue",
            CHARACTER_CLASS.WARLOCK: "Warlock",
        }
        return classes[class_number]


class MINION_TYPE:
    NONE = 0
    BEAST = 1
    MURLOC = 2
    DRAGON = 3
    GIANT = 4
    DEMON = 5
    PIRATE = 6
    TOTEM = 7

    @staticmethod
    def from_str(type_name):
        TYPES = {
            "": MINION_TYPE.NONE,
            "BEAST": MINION_TYPE.BEAST,
            "MURLOC": MINION_TYPE.MURLOC,
            "DRAGON": MINION_TYPE.DRAGON,
            "GIANT": MINION_TYPE.GIANT,
            "DEMON": MINION_TYPE.DEMON,
            "PIRATE": MINION_TYPE.PIRATE,
            "TOTEM": MINION_TYPE.TOTEM,
        }
        return TYPES[type_name.upper()]
