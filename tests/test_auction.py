import auctionsite.main


def test_login_success():
    assert auctionsite.main.login("john", "password") is True


def test_browse_auctions():
    assert auctionsite.main.browse_auctions() == "an001"  # returns auction number


def test_make_bid_successful():
    assert auctionsite.main.make_bid(bid=10, auction_id="an001") is True


def test_make_bid_fail():
    assert auctionsite.main.make_bid(bid=0, auction_id="an001") is False


def test_save_as_favorite():
    assert auctionsite.main.save_as_favorite(auction="an001") is True


def test_get_price():
    assert auctionsite.main.get_price("an001") == 0