from pprint import pprint


def players_by_position(squads_list):
    grouped = {}

    for player in squads_list:
        number = player[0]
        position = player[1]
        name = player[2]
        date_of_birth = player[3]
        caps = player[4]
        club = player[5]
        country = player[6]
        club_country = player[7]
        tournament_year = player[8]

        player_dict = {
            "number": number,
            "position": position,
            "name": name,
            "date_of_birth": date_of_birth,
            "caps": caps,
            "club": club,
            "country": country,
            "club_country": club_country,
            "tournament_year": tournament_year
        }

         if position not in grouped:
            grouped[position] = []

        grouped[position].append(player_dict)

    return grouped



result = players_by_position(SQUADS_DATA)
pprint(result)