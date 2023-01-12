import json



def get_mtgd(dbfile='oracle-cards-20230108100200.json'):

    with open(dbfile) as f:
        mtg = json.load(f)

    for card in mtg:
        mtgd[card['name']] = card

    return mtgd
