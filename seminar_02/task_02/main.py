from seminar_02.task_01.human import Human
from seminar_02.task_02.market import Market

market = Market()

visitors_names = ["Евгений", "Микаел", "Иван", "Алексей"]

for i in visitors_names:
    market.accept_to_market(Human(i))
    market.update()
