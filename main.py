from typing import List, Optional, Tuple
import requests
import sys
from bisect import bisect_left, bisect_right


def BinarySearch(a: List[int], x: int) -> Optional[Tuple]:
    """
    Return the left and right indexes of x in the ordered list a.
    If x is not in a return None.
    
    :param List a: Ordered list where we look for x.
    :param int x:
    :return: Tuple with left and right indexes
    :rtype: Tuple
    """
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

    pair_players_list = []
    prev_h_in = None
    for idx, player in enumerate(all_players_sorted):
        h_in = int(player['h_in'])
        h_in_other = arg - h_in
        if h_in != prev_h_in:
            indexes = BinarySearch(all_h_in_sorted, h_in_other)

        if indexes:
            end = indexes[1]
            if idx < end:
                start = max(indexes[0], idx+1)
                for player2 in all_players_sorted[start:end]:
                    pair_players_list.append({
                        'player1': {
                            'name': f"{ player['first_name'] } { player['last_name'] }",
                            'h_in': h_in
                        },
                        'player2': {
                            'name': f"{ player2['first_name'] } { player2['last_name'] }",
                            'h_in': h_in_other
                        }
                    })

    for pair_players in pair_players_list:
        print('-', pair_players['player1']['name'],'\t' , pair_players['player2']['name'])


if __name__ == '__main__':
    try:
        arg = int(sys.argv[1])
    except:
        arg = 139
    app(arg)
