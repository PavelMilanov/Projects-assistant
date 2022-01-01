from api.trello_request import TrelloRequest
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger


trello = TrelloRequest()
scheduler = BackgroundScheduler()

logger.add('debug/logs.log', format='{time} {level} {message}', level='DEBUG', rotation="100 KB", compression="zip")


if __name__ == '__main__':
    
    scheduler.start()
    scheduler.add_job(trello.archive_done_cards, 'cron', day_of_week='tue')

    while True:
        pass


# [
#     {
#         "id": "612bb559cea8df32b855b183",
#         "name": "Колонка экспертов. Когда есть баг или задача ставьте ее Софии. Обязательно доьавляйте себя к карточке и Софию. !Описать как есть, описать как надо и добавить скрин!",
#         "closed": false,
#         "pos": 69631.5,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "61a668560ba28f822390deb8",
#         "name": "Тех поддержка (Любовь)",
#         "closed": false,
#         "pos": 82687.40625,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "61961256942fdc8c1fb9d387",
#         "name": "Колонка Тестировщиков (Андрей)",
#         "closed": false,
#         "pos": 95743.3125,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "5fde88e317b35d02e79cde7b",
#         "name": "For Sofia",
#         "closed": false,
#         "pos": 104447.25,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": true
#     },
#     {
#         "id": "60797a28719f45233491d824",
#         "name": "For Oleg",
#         "closed": false,
#         "pos": 139263,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "61b9bfddede1262deed40cb8",
#         "name": "For Kost",
#         "closed": false,
#         "pos": 167935,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "5fde6c0e6837394e7ec3ea29",
#         "name": "For Jury",
#         "closed": false,
#         "pos": 196607,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "5fde6c0e6837394e7ec3ea2a",
#         "name": "В работе",
#         "closed": false,
#         "pos": 262143,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "5fde6c0e6837394e7ec3ea2c",
#         "name": "Testing DEV",
#         "closed": false,
#         "pos": 311295,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": true
#     },
#     {
#         "id": "5fde83a9cfdd620aaca4ead4",
#         "name": "К заливке на PROD",
#         "closed": false,
#         "pos": 352255,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "5fde8524864ca6204bd273e2",
#         "name": "Testing PROD",
#         "closed": false,
#         "pos": 372735,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": true
#     },
#     {
#         "id": "5fde6c0e6837394e7ec3ea2d",
#         "name": "Done PROD 🎉",
#         "closed": false,
#         "pos": 393215,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     },
#     {
#         "id": "612bb62a18c35a73ba3a59be",
#         "name": "Задачи на будущее",
#         "closed": false,
#         "pos": 458751,
#         "softLimit": null,
#         "idBoard": "5fde6c0e6837394e7ec3ea26",
#         "subscribed": false
#     }
# ]