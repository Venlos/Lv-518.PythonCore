def areYouPlayingBanjo(name):
    # Implement me!
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#def areYouPlayingBanjo(name):
#    return name + (' plays banjo' if name[0]=='r' or name[0]=='R' else ' does not play banjo')

#def areYouPlayingBanjo(name):
#   return '{} {}'.format(name, 'plays banjo' if name.startswith('R') or name.startswith('r') else 'does not play banjo')