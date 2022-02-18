import requests
import sys
from bisect import bisect_left, bisect_right


def BinarySearch(a, x):
    i_left = bisect_left(a, x)
    i_right = bisect_right(a, x)
    if i_left != len(a) and a[i_left] == x:
        return i_left, i_right
    else:
        return None


def app(arg):
    URL = 'https://mach-eight.uc.r.appspot.com/'
    all_players = requests.get(URL).json()['values']
    all_players_sorted = sorted(all_players, key=lambda x: x['h_in'])
    all_h_in_sorted = [int(player['h_in']) for player in all_players_sorted]

    players = []
    prev_h_in = None
    for idx, player in enumerate(all_players_sorted):
        h_in = int(player['h_in'])
        h_in_other = arg - h_in
        if h_in != prev_h_in:
            h_in_sorted_up = all_h_in_sorted[idx+1:]
            indexes = BinarySearch(all_h_in_sorted, h_in_other)
            players_sorted_up = all_players_sorted[idx+1:]

        if indexes:
            print(indexes)
            players_in_indexes = players_sorted_up[indexes[0]-1:indexes[1]-1]
            for player2 in players_in_indexes:
                players.append({
                    'player1': {
                        'name': f"{ player['first_name'] } { player['last_name'] }",
                        'h_in': h_in
                    },
                    'player2': {
                        'name': f"{ player2['first_name'] } { player2['last_name'] }",
                        'h_in': h_in_other
                    }
                })

    print(players)


if __name__ == '__main__':
    try:
        arg = int(sys.argv[0])
    except:
        arg = 140
    app(arg)
