'''
Created on Oct 26, 2021

@author: Cyrus
'''

world_order_warps_dict = {
    "1": [ # 009F
        "0EA40000F8234B06009F",
        "0ED70012F8634B06009F",
        ],
    "2": [ # 000C
        "FBD2007503512186000C",
        "FB2D007103012686000C",
        "FA7B005902AB2886000C",
        "FB50002903764706000C",
        "FA87002103154486000C",
        "FB5D006F03F72406000C",
        "FA96006D03972206000C",
        "FA07006403432186000C",
        ],
    "3": [ # 000D            
        "000000DEF4A26206000D",
        ],
    "4": [ # 000E
        "061B005800CE4306000E",
        ],
    "5": [ # 0073            
        "13BA00BA1AC396060073",
        "13DE00BA1A5C96060073",
        "13F800BA19F396060073",
        "141E00BA198396060073",
        ],
    "6": [ # 000F
        "0003029EE4B15406000F",
        ],
    "7": [ # 0010
        "FFF701C3FEE67F060010",
        ],
    "8": [ # 0011
        "0003035BF9825E060011",
        ],
    "9": [ # 0122
        "FFE60426F18189060122",
        ],
    }

learnable_moves_dict = {
    "Talon_Trot": "060C037A",
    "Beak_Buster": "058C037A",
    "Shock_Jump_Pad": "068C037A",
    "Eggs": "050C037A",
    "Fly": "070C037A",
    "Wonderwing": "078C037A",
    "Wading_Boots": "080C037A",
    "Beak_Bomb": "048C037A",
    "Turbo_Talon_Trot": "088C037A"
    }

bottles_moves_camera_dict = {
    "058C037A": { # Beak Buster
        "Primary_Camera": "01001702",
        "Secondary_Camera": None,
        },
    "060C037A": { # Talon Trot
        "Primary_Camera": "01001802",
        "Secondary_Camera": None,
        },
    "068C037A": { # Shock Jump Pad
        "Primary_Camera": "01000C02",
        "Secondary_Camera": None,
        },
    "050C037A": { # Eggs
        "Primary_Camera": "01001602",
        "Secondary_Camera": None,
        },
    "070C037A": { # Fly Pad
        "Primary_Camera": "01000D02",
        "Secondary_Camera": None,
        },
    "078C037A": { # Wonderwing
        "Primary_Camera": "01000102",
        "Secondary_Camera": None,
        },
    "080C037A": { # Wading Boots
        "Primary_Camera": "01001002",
        "Secondary_Camera": "01001102",
        },
    "048C037A": { # Beak Bomb
        "Primary_Camera": "01000F02",
        "Secondary_Camera": None,
        },
    "088C037A": { # Running Shoes
        "Primary_Camera": "01001902",
        "Secondary_Camera": "01002902",
        },
    }

possible_bottles_locations = {
        "Mumbo's Mountain": {
            "Beak_Buster": "0F67086BF2A2",
            "Talon_Trot": "F60A08CFFB3F",
            "Pink_Jinjo": "16F4012B0941",
            "Blue_Jinjo": "06A6FF830B7D",
            "Orange_Jinjo": "F31F0AC3FA73",
            "Yellow_Jinjo": "F024054B0444",
            },
        "Treasure Trove Cove": {
            "Fly": "FEE008710522",
            "Shock_Jump_Pad": "0A8A05ED0D0A",
            "Ledge_1_Up": "F6760C56F956",
            "Sharkfood_Island_1_Up": "16E802A51EDA",
            "Orange_Jinjo": "EA060C28F4D8",
            "Yellow_Jinjo": "FC3814EEFCF8",
            "Pink_Jinjo": "12F0053CFF10",
            },
        "Clanker's Cavern": {
            "Wonderwing": "FEFDFE0C0585",
            "Platform_1_Up": "11DA0E8F0ADF",
            "Alcove_1_Up": "06D81496F75A",
            "Yellow_Jinjo": "ED8A14D9FF92",
            "Orange_Jinjo": "17FA13DF0A4D",
            },
        "Bubblegloop Swamp": {
            "Wading_Boots": "10C90064188E",
            "Green_Jinjo": "0672064007C4",
            "Yellow_Jinjo": "F9BA01F40AED",
            },
        "Freezeezy Peak": {
            "Beak_Bomb": "E2DA00FA052C",
            "Finish_Pole_1_Up": "EE9E0637E311",
            "Mumbo_Skull_1_Up": "1B50056EF3A9",
            "Blue_Jinjo": "F5E41634003C",
            "Green_Jinjo": "17C301C20AB0",
            "Pink_Jinjo": "E53D04A903A2",
            "Yellow_Jinjo": "00000196FE01",
            "Blue_Present": "FDFB19800509",
            "Red_Present": "FD960017FD7D",
            "Green_Present": "039A0012F561",
            },
        "Gobi's Valley": {
            "Turbo_Talon_Trot": "E6D30B0FFCCA",
            "King_Sandybutt_1_Up": "0502001207B3",
            "Water_Pyramid_1_Up": "FF1A12D4EEBB",
            "Yellow_Jinjo": "0BFB01BF281E",
            "Green_Jinjo": "135809EA01B7",
#             "Orange_Jinjo": "081E0462FFCE",
            },
        "Mad Monster Mansion": {
            "Organ_1_up": "FFFF08D7F277",
            "Church_Secret_Room": "0000000D0267",
            "Blue_Jinjo": "170C012C041A",
            "Orange_Jinjo": "EF5700000A6C",
            "Yellow_Jinjo": "FF06021C012C",
            },
        "Rusty Bucket Bay": {
            "Big_Fish_Warehouse_1_Up": "FC4A0415FFCE",
            "Engine_Room_1_Up": "F6090429F5A6",
            "Blue_Jinjo": "FF3F0000FC2D",
            "Orange_Jinjo": "22C7FCE0F4B2",
            },
        "Click Clock Wood": {
            "Spring_Branch_1_Up": "EC7F0B50FC50",
            "Spring_Whipcrack_Room_Floor_1_Up": "FD4B00020210",
            "Summer_Grass_1_Up": "0E140016F054",
            "Summer_Treehouse_1_Up": "16D810940264",
            "Summer_Yellow_Jinjo": "F1EE000010AA",
            "Summer_Whipcrack_Room_1_Up": "034101B90085",
            "Fall_Orange_Jinjo": "F9C80384E847",
            "Fall_Acorn_Ledge": "003F0EEB1388",
            "Winter_Sir_Slush": "F9C00FB310CC",
            },
        }
