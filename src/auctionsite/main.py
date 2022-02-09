def get_price(auction_id):
    return 0

def make_bid(bid, auction_id):
    auction_price = get_price(auction_id)
    if bid <= auction_price:
        return False
    auction_price = bid
    return True