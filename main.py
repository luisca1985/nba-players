from typing import List, Optional, Tuple
import requests
import sys
from bisect import bisect_left, bisect_right


def BinarySearch(a: List[int], x: int) -> Optional[Tuple]:
    """
    Return the left and right indexes of x in the ordered list a,
    using a binary search algorithm, whose complexity is O(log n).
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


def app(height_sum: int):
    """
    Download the raw data from https://mach-eight.uc.r.appspot.com 
    and print a list of all pairs of players whose height in inches 
    adds up to height_sum. If no matches are found, the application 
    will print "No matches found"

    :param int height_sum: pairs of players height sum.
    """

    URL = 'https://mach-eight.uc.r.appspot.com/'
    # Get all players from URL
    all_players = requests.get(URL).json()['values']
    # Order the players by height
    # sorted is O(n log n) both on average and in the worst case.
    all_players_sorted = sorted(all_players, key=lambda x: x['h_in'])
    # Get list with height of players in the same order
    all_h_in_sorted = [int(player['h_in']) for player in all_players_sorted]

    # Declare list to storage pair players
    pair_players_list = []
    # Declare variable to check if height of next player is equal or different
    # to the previous player
    prev_h_in = None

    # For all players get height and search all other players
    # whose heights sum is equal the user input.
    for idx, player in enumerate(all_players_sorted):
        # get player height
        h_in = int(player['h_in'])
        # get height of its pair players
        h_in_pair_players = height_sum - h_in

        # If height is the same than the last player, use the same pair players,
        # cause is the same sum.
        # If height is different, get a new index with the range of users whose
        # height sums the user input
        if h_in != prev_h_in:
            # Get the left and right indexes with the range of pair players
            # Use a binary search with complexity is O(log n)
            # Taking into account the for loop, the worst case is a O(n log n).
            indexes = BinarySearch(all_h_in_sorted, h_in_pair_players)

        # Verify if pair players range exist
        if indexes:
            # get the end of the sublist with pair player
            end = indexes[1]
            # Only take into account upper ranges of players to no repeat pairs.
            if idx < end:
                start = max(indexes[0], idx+1)

                # Get players in range to create pairs and append the player and
                # its pairs
                for player2 in all_players_sorted[start:end]:
                    pair_players_list.append({
                        'player1': {
                            'name': f"{ player['first_name'] } { player['last_name'] }",
                            'h_in': h_in
                        },
                        'player2': {
                            'name': f"{ player2['first_name'] } { player2['last_name'] }",
                            'h_in': h_in_pair_players
                        }
                    })

    # If list is not empty print player and its pair names
    # If list is empty print "No matches found"
    if len(pair_players_list) > 0:
        for pair_players in pair_players_list:
            print('-', pair_players['player1']['name'],
                  '\t', pair_players['player2']['name'])
    else:
        print("No matches found")


if __name__ == '__main__':
    # get height sum as an argument. If not exist use 139 as default.
    try:
        height_sum = int(sys.argv[1])
    except:
        height_sum = 139

    app(height_sum)
