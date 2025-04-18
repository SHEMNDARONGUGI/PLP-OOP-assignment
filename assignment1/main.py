from music import LivePerformance

while True:
    composer = input("Composer: ")
    piece = input("Piece name: ")
    year = int(input("Year: "))
    instrument = input("Instrument: ")
    location = input("Performance Location: ")

    performance = LivePerformance(composer, piece, year, instrument, location)
    performance.play()

    choice = input("Stop from playing? (Yes/No): ").strip().lower()
    if choice in ("y", "yes"):
        performance.stop()

    again = input("Add another? (Yes/No): ").strip().lower()
    if again not in ("yes", "y"):
        break
