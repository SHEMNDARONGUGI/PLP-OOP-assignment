# music.py
class Music:
    def __init__(self, composer, piece, year, instrument):
        self.composer = composer
        self.piece = piece
        self.year = year
        self.instrument = instrument
        
    def play(self):
        print(f"{self.composer} is playing {self.piece} on {self.instrument} in {self.year}")
        
    def stop(self):
        print(f"{self.composer} has stopped playing {self.piece}")


# Subclass using inheritance
class LivePerformance(Music):
    def __init__(self, composer, piece, year, instrument, location):
        super().__init__(composer, piece, year, instrument)
        self.location = location

    # Polymorphism: override play()
    def play(self):
        print(f"{self.composer} is performing '{self.piece}' live at {self.location} on the {self.instrument} in {self.year}")
