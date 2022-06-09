
from project.booking import Booking

    
with Booking(teardown=False) as bot:
    bot.land_first_page()
     # bot.change_currency(currency='GBP')
    bot.reserve('New York', '2022-05-31', '2022-06-01', 10)
    bot.apply_filtrations()
    bot.export_to_excel()