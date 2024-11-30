import random

class BlackjackTemplate():
    def __init__(self, decks_n):
        # хранить в атрибуте колоду c decks_n мастями (decks_n ∈ [1;4])
        pass

    def start_game(self):
        # перемешать колоду
        # записать в лог (если успеешь)
        pass
    
    def hit(self):
        # взять карту
        # возвратить результат ('blackjack' если 10 + туз /'lose' если сумма > 21 / 'idle' иначе), взятую карту и суммы игрока, дилера
        # если перебрал, закончить игру (self.end_game), придумай как-нибудь, чтобы последующие вызовы вызывали ошибку
        # можно в каждом внешнем методе сначала вызывать функцию проверки, например, которая будет проверять флаг
        pass

    def stand(self):
        # сыграть за дилера
        # возвратить результат ('win' / 'lose' / 'lose_blackjack' если 10 + туз / 'draw'), карты дилера, сумму дилера
        # если что, дилер берет карты пока у него меньше 17 или меньше игрока
        self.end_game()
        pass

    def end_game(self):
        # после вызова этой функции, все другие вызовы методов должны кидать exception
        # записать в лог (если успеешь)
        pass

    def xsdfcgvhbjnkml(self):
        # можешь создавать сколько угодно любых внутренних вспомогательных функций,
        # которые я не буду вызывать извне, но они могут использоваться тобой для логики остальных функций
        pass


class Blackjack():
    def __init__(self, pc, dc):
        self.deck = ['2H', '2S', '2D', '2C', '3H', '3S', '3D', '3C',
                     '4H', '4S', '4D', '4C', '5H', '5S', '5D', '5C', '6H', '6S', '6D', '6C',
                     '7H', '7S', '7D', '7C', '8H', '8S', '8D', '8C', '9H', '9S', '9D', '9C',
                     '10H', '10S', '10D', '10C', 'JH', 'JS', 'JD', 'JC', 'QH', 'QS', 'QD', 'QC',
                     'KH', 'KS', 'KD', 'KC', 'AH', 'AS', 'AD', 'AC']
        random.shuffle(self.deck)

        self.pc = pc
        for card in pc:
            self.deck.remove(card)
        self.dc = dc
        for card in dc:
            self.deck.remove(card)
        self.flag = 1
        self.w = 0

    def hit(self):
        if self.flag:
            ch = self.deck.pop()
            self.pc.append(ch)
            a = 0
            spp = 0
            for i in self.pc:
                j = i[:-1]
                if j.isdigit():
                    spp += int(j)
                elif j == 'A':
                    spp += 1
                    a = 1
                else:
                    spp += 10
            if a and spp <= 11:
                spp += 10
            if spp > 21:
                self.end_game()
            return ch, spp, 0
        else:
            raise Exception('Game is over, and so is your balance')

    def start(self):
        if self.flag:
            for i in range(2):
                ch = self.deck.pop()
                self.dc.append(ch)
            a = 0
            spp = 0
            for i in self.dc:
                j = i[:-1]
                if j.isdigit():
                    spp += int(j)
                elif j == 'A':
                    spp += 1
                    a = 1
                else:
                    spp += 10
            if a and spp <= 11:
                spp += 10
            return self.dc, spp
        else:
            raise Exception('Game is over, and so is your balance')

    def stand(self):
        a = 0
        if self.flag:
            spp = 0
            for i in self.pc:
                j = i[:-1]
                if j.isdigit():
                    spp += int(j)
                elif j == 'A':
                    spp += 1
                    a = 1
                else:
                    spp += 10
            if a and spp <= 11:
                spp += 10

            a = 0
            sup = 0
            for i in self.pc:
                j = i[:-1]
                if j.isdigit():
                    sup += int(j)
                elif j == 'A':
                    sup += 1
                    a = 1
                else:
                    sup += 10
            if a and sup <= 11:
                sup += 10
            while sup < 17 or sup <= spp:
                j = random.choice(self.deck)
                self.dc.append(j)
                if j.isdigit():
                    sup += int(j)
                elif j == 'A':
                    sup += 1
                    a = 1
                else:
                    sup += 10
                if a and sup <= 11:
                    sup += 10
                

            return self.dc, sup
        else:
            raise Exception('Game is over, and so is your balance')

    def end_game(self):
        self.flag = 0
