import random

CARD_WEIGHS = "A 2 3 4 5 6 7 8 9 10 J Q K".split()
CARD_SUITS = "HSDC"

GAME_STATE_IDLE = "idle"
GAME_STATE_REACHED_MAX = 'reached_max'
GAME_STATE_WIN = "win"
GAME_STATE_WIN_BLACKJACK = "win_blackjack"
GAME_STATE_LOSE = "lose"
GAME_STATE_LOSE_BLACKJACK = "lose_blackjack"
GAME_STATE_DRAW = 'draw'
GAME_STATE_DRAW_BLACKJACK = "draw_blackjack"

class GameAlreadyFinishedError(Exception):
    pass

# Реализация игры блекджек
class Blackjack():
    def __init__(self, hand_player:list[tuple[str, str]]=[], hand_dealer:list[tuple[str, str]]=[], decks_n:int=4):
        if not (0 < decks_n < 5):
            raise Exception('Impossible number of decks, must be in between 1-4.')
        
        self.deck = [(weigh, suit) for weigh in CARD_WEIGHS for suit in CARD_SUITS[:decks_n]][::-1]
        self.goal = 21
        self.dealer_min = 17
        self.game_mode = 'H17'

        for card in hand_player:
            self.deck.remove(card)
        for card in hand_dealer:
            self.deck.remove(card)
        self.hand_player = hand_player
        self.hand_dealer = hand_dealer

        self.is_active = True
        random.shuffle(self.deck)
    
    # Начать игру
    def start(self):
        if not self.is_active:
            raise GameAlreadyFinishedError('Game is over, and so is your balance (tried to call a start method on a finished game)')
        
        for i in range(1):
            card = self.deck.pop()
            self.hand_dealer.append(card)
        dealer_sum, dealer_is_soft = self.sum_hand(self.hand_dealer)
        return self.hand_dealer, dealer_sum, dealer_is_soft
    
    # Взять карту игроку
    def hit(self):
        if not self.is_active:
            raise GameAlreadyFinishedError('Game is over, and so is your balance (tried to call a hit method on a finished game)')
        
        card = self.deck.pop()
        self.hand_player.append(card)
        player_sum, player_is_soft = self.sum_hand(self.hand_player)
        if player_sum > self.goal:
            self.end_game()
            game_state = GAME_STATE_LOSE
        elif player_sum == self.goal:
            card_dealer = self.hand_dealer[0][0]
            if player_sum == self.goal and len(self.hand_player) == 2 and not (card_dealer.isalpha() or card_dealer == '10'):
                game_state = GAME_STATE_WIN_BLACKJACK
            else:
                game_state = GAME_STATE_REACHED_MAX
        else:
            game_state = GAME_STATE_IDLE
        return game_state, self.hand_player[-1], player_sum, player_is_soft
    
    # Хватит брать карты игроку
    def stand(self):
        if not self.is_active:
            raise GameAlreadyFinishedError('Game is over, and so is your balance (tried to call a method on a finished game)')
        
        # Подсчет карт игрока и дилера
        player_sum, player_soft = self.sum_hand(self.hand_player)
        dealer_sum, dealer_soft = self.sum_hand(self.hand_dealer)
        
        while (dealer_sum < player_sum or dealer_sum < 17)\
                or (dealer_sum == 17 and len(self.hand_dealer) == 2 and self.game_mode == 'H17'):
            card = self.deck.pop()
            self.hand_dealer.append(card)
            # Каждый раз считаем заново из-за сложностей с учетом туза
            dealer_sum, dealer_soft = self.sum_hand(self.hand_dealer)
        if dealer_sum > 21 or player_sum > dealer_sum:
            if player_sum == self.goal and len(self.hand_player) == 2:
                game_state = GAME_STATE_WIN_BLACKJACK
            else:
                game_state = GAME_STATE_WIN
        elif player_sum < dealer_sum:
            if dealer_sum == self.goal and len(self.hand_dealer) == 2:
                game_state = GAME_STATE_LOSE_BLACKJACK
            else:
                game_state = GAME_STATE_LOSE
        elif player_sum == dealer_sum:
            if player_sum == self.goal:
                if len(self.hand_player) == 2 and len(self.hand_dealer) == 2:
                    game_state = GAME_STATE_DRAW_BLACKJACK
                elif len(self.hand_player) == 2:
                    game_state = GAME_STATE_WIN_BLACKJACK
                elif len(self.hand_dealer) == 2:
                    game_state = GAME_STATE_LOSE_BLACKJACK
                else:
                    game_state = GAME_STATE_DRAW
            else:
                game_state = GAME_STATE_DRAW
        
        self.end_game()
        return game_state, self.hand_dealer, dealer_sum, dealer_soft
    
    # Посчитать сумму карт на руках
    def sum_hand(self, hand: list):
        hand_sum = 0
        aces = 0
        soft = False
        for card in hand:
            weigh = card[0]
            if weigh.isdigit():
                hand_sum += int(weigh)
            elif weigh == 'A':
                hand_sum += 1
                aces += 1
            else:
                hand_sum += 10
        while aces and hand_sum + 10 <= self.goal:
            hand_sum += 10
            aces -= 1
            soft = True
        return hand_sum, soft

    def end_game(self):
        self.is_active = False
