import tkinter as tk
from tkinter import messagebox
import customtkinter
import random
import time

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("600x400")

        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.label = customtkinter.CTkLabel(master=self.root, text="Welcome to Blackjack!")
        self.label.pack()

        self.hit_button = customtkinter.CTkButton(master=self.root, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = customtkinter.CTkButton(master=self.root, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.RIGHT, padx=10)

        self.player_frame = customtkinter.CTkFrame(master=self.root)
        self.player_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.dealer_frame = customtkinter.CTkFrame(master=self.root)
        self.dealer_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH, expand=True)

    def start_game(self):
        self.player_hand = [self.get_card(), self.get_card()]
        self.dealer_hand = [self.get_card(), self.get_card()]

        self.show_hands()

        if self.get_hand_value(self.player_hand) == 21:
            self.end_game("BLACKJACK! You Win!")
        elif self.get_hand_value(self.dealer_hand) == 21:
            self.end_game("Dealer has Blackjack! You lose!")

    def get_card(self):
        return random.randint(1, 11)

    def get_hand_value(self, hand):
        value = sum(hand)
        aces = hand.count(1)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def show_hands(self):
        # Clear previous cards
        for widget in self.player_frame.winfo_children():
            widget.destroy()

        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        # Display player's hand
        player_hand_text = "Your hand:\n"
        for i, card in enumerate(self.player_hand):
            card_label = customtkinter.CTkLabel(master=self.player_frame, text=self.get_card_ascii(card))
            card_label.grid(row=0, column=i, padx=5, pady=5)
            player_hand_text += f"{card} "
        player_hand_text += f"\nTotal: {self.get_hand_value(self.player_hand)}"
        player_total_label = customtkinter.CTkLabel(master=self.player_frame, text=player_hand_text)
        player_total_label.grid(row=1, column=0, columnspan=4)

        # Display dealer's hand
        dealer_hand_text = "Dealer's hand:\n"
        for i, card in enumerate(self.dealer_hand):
            if i == 0:
                card_label = customtkinter.CTkLabel(master=self.dealer_frame, text=self.get_card_ascii_back())
            else:
                card_label = customtkinter.CTkLabel(master=self.dealer_frame, text=self.get_card_ascii(card))
            card_label.grid(row=0, column=i, padx=5, pady=5)
            if i == 0:
                continue
            dealer_hand_text += f"{card} "
        if len(self.dealer_hand) > 1:
            dealer_hand_text += f"\nTotal: {self.get_hand_value(self.dealer_hand[1:])}"
        else:
            dealer_hand_text += "\nTotal: ???"
        dealer_total_label = customtkinter.CTkLabel(master=self.dealer_frame, text=dealer_hand_text)
        dealer_total_label.grid(row=1, column=0, columnspan=4)

    def get_card_ascii_back(self):
        return """
┌───┐
│░░░│
│░░░│
│░░░│
│░░░│
│░░░│
└───┘"""

    def get_card_ascii(self, card):
        if card == 1:
            return """
┌───┐
│ A       │
│          │
│   ♠    │
│          │
│     A   │
└───┘"""
        elif card == 2:
            return """
┌───┐
│ 2       │
│          │
│   ♠    │
│          │
│     2   │
└───┘"""
        elif card == 3:
            return """
┌───┐
│ 3       │
│          │
│   ♠    │
│          │
│     3  │
└───┘"""
        elif card == 4:
            return """
┌───┐
│ 4       │
│           │
│   ♠    │
│           │
│     4   │
└───┘"""
        elif card == 5:
            return """
┌───┐
│ 5       │
│           │
│   ♠    │
│           │
│     5   │
└───┘"""
        elif card == 6:
            return """
┌───┐
│ 6       │
│           │
│   ♠    │
│           │
│     6   │
└───┘"""
        elif card == 7:
            return """
┌───┐
│ 7       │
│           │
│   ♠    │
│           │
│     7   │
└───┘"""
        elif card == 8:
            return """
┌───┐
│ 8       │
│           │
│   ♠    │
│           │
│     8   │
└───┘"""
        elif card == 9:
            return """
┌───┐
│ 9       │
│           │
│   ♠    │
│           │
│     9   │
└───┘"""
        elif card == 10:
            return """
┌───┐
│ 10      │
│           │
│   ♠    │
│           │
│    10   │
└───┘"""
        elif card == 11:
            return """
┌───┐
│ J       │
│           │
│   ♠    │
│           │
│     J   │
└───┘"""
        elif card == 12:
            return """
┌───┐
│ Q       │
│           │
│   ♠    │
│           │
│     Q   │
└───┘"""
        elif card == 13:
            return """
┌───┐
│ K       │
│           │
│   ♠    │
│           │
│     K  │
└───┘"""

    def hit(self):
        self.player_hand.append(self.get_card())
        self.show_hands()

        if self.get_hand_value(self.player_hand) > 21:
            self.end_game("Busted! You Lose!")

    def stand(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.get_card())
            self.show_hands()
            time.sleep(0.5)  # Add a small delay
        player_value = self.get_hand_value(self.player_hand)
        dealer_value = self.get_hand_value(self.dealer_hand)

        if dealer_value > 21 or player_value > dealer_value:
            self.end_game("You Win!")
        elif player_value < dealer_value:
            self.end_game("Dealer Wins!")
        else:
            self.end_game("It's a Tie!")

    def end_game(self, message):
        time.sleep(0.5)  # Add a small delay
        play_again = messagebox.askyesno("Game Over", f"{message}\nDo you want to play again?")
        if play_again:
            self.start_game()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = customtkinter.CTk()
    game = BlackjackGame(root)
    root.mainloop()
