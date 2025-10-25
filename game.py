import os
import klassen
from klassen import Trainer, Pokemon

def calc_damage(attacker: Pokemon, defender: Pokemon, power: int) -> int:
    """
    Damage formula using attack and defense stats.
    - If power is falsy, damage is 0.
    - Uses a simplified Pokemon-like formula that scales with level.
    """
    if not power:
        return 0
    atk = getattr(attacker, 'attack', max(1, attacker.level * 5))
    defe = getattr(defender, 'defense', 1)
    if defe <= 0:
        defe = 1
    base = (2 * attacker.level) / 5 + 2
    # simplified damage: (((base * power * (atk/def)) / 50) + 2)
    damage = int(((base * power * (atk / defe)) / 50) + 2)
    return max(1, damage)

def choose_move(active: Pokemon) -> dict:
    """Show up to 4 moves and return the selected move entry (the API 'move' entry)."""
    moves = active.moveset[:4]
    if not moves:
        print(f"{active.name.title()} hat keine Züge.")
        return None
    for idx, m in enumerate(moves, start=1):
        print(f"{idx}. {m['move']['name']}")
    try:
        choice = int(input('Wähle einen Zug (Nummer): ').strip()) - 1
        if choice < 0 or choice >= len(moves):
            print("Ungültige Auswahl.")
            return None
        return moves[choice]
    except ValueError:
        print("Ungültige Eingabe.")
        return None

def use_bag(player: Trainer):
    """Show bag items and allow using a potion (heals active pokemon)."""
    bag = getattr(player, 'bag', {})
    if not bag:
        print("Dein Beutel ist leer.")
        return
    print("Beutel-Inhalt:")
    for item, cnt in bag.items():
        print(f"- {item}: {cnt}")
    cmd = input("Gib den Namen des Items zum Verwenden ein (oder leer zum Abbrechen): ").strip().lower()
    if not cmd:
        return
    if cmd not in bag or bag[cmd] <= 0:
        print("Item nicht verfügbar.")
        return
    # support only 'potion' for now
    if cmd == 'potion':
        active = player.pokemon[0]
        heal = 20
        active.hp += heal
        bag[cmd] -= 1
        print(f"{active.name.title()} wurde um {heal} HP geheilt. Jetzt {active.hp} HP.")
    else:
        print("Dieses Item ist noch nicht implementiert.")

def main():
    print("Willkommen zum Pokesim!")
    player_name = input('Wie lautet dein Name? --> ').strip() or "Trainer"
    starter_input = input('Wähle ein Pokemon (z.B. pikachu, charmander) --> ').strip().lower()
    try:
        poke2 = Pokemon(starter_input, 5)
    except Exception as e:
        print("Fehler beim Laden des gewählten Pokemons, standard Pikachu wird verwendet. Fehler:", e)
        poke2 = Pokemon('pikachu', 5)

    poke = Pokemon('pikachu', 5)
    poke1 = Pokemon('charmander', 10)

    player = Trainer([poke2, poke, poke1], player_name)
    # give player a simple potion in the bag
    player.bag = {'potion': 2}

    geg = Pokemon('pikachu', 5)

    if getattr(poke, 'typ1', None):
        print(poke.typ1.title())
    print('Ein wildes ' + geg.name.title() + ' erscheint!')

    while True:
        aktpk = player.pokemon[0]
        print(f"\nDein aktives Pokemon: {aktpk.name.title()} (Level {aktpk.level}) — {aktpk.hp} HP")
        print(f"Wilder Gegner: {geg.name.title()} — {geg.hp} HP")
        print('Was wird ' + player.name + ' tun?')
        print('1. Kampf  2. Pokemon  3. Beutel  4. Flucht  (tippe "help" für Befehle)')
        a = input().strip().lower()

        if a == 'help':
            print("Befehle:\n - 1: Kampf (wähle Zug)\n - 2: Pokemon tauschen\n - 3: Beutel nutzen\n - 4: Flucht\n - debug: zeige Informationen zum aktiven Pokemon")
            continue

        if a == 'debug':
            print("Aktives Pokemon Objekt:", aktpk)
            print("Moveset (raw):", aktpk.moveset)
            continue

        if a == '1':
            move_entry = choose_move(aktpk)
            if not move_entry:
                continue
            try:
                move_meta = klassen.holmove(move_entry['move']['url'], move_entry['move']['name'])
            except Exception as e:
                print("Fehler beim Laden des Zugs:", e)
                continue
            move_name = move_meta.get('name', 'Unbekannt')
            power = move_meta.get('power') or 0
            damage = calc_damage(aktpk, geg, power)
            print(f"{aktpk.name.title()} benutzt {move_name} (Power: {power}) -> verursacht {damage} Schaden")
            geg.hp -= damage
            if geg.hp <= 0:
                print(f"Das wilde {geg.name.title()} wurde besiegt!")
                break
            # simple enemy counterattack: use first known move if exists
            if geg.moveset:
                try:
                    geg_move = geg.moveset[0]
                    geg_meta = klassen.holmove(geg_move['move']['url'], geg_move['move']['name'])
                    geg_power = geg_meta.get('power') or 0
                    geg_damage = calc_damage(geg, aktpk, geg_power)
                    print(f"Das wilde {geg.name.title()} greift an mit {geg_meta.get('name','')}, verursacht {geg_damage} Schaden")
                    aktpk.hp -= geg_damage
                    if aktpk.hp <= 0:
                        print(f"{aktpk.name.title()} ist kampfunfähig!")
                        # swap to next available Pokemon if any
                        available = [p for p in player.pokemon if p.hp > 0]
                        if available:
                            player.pokemon[0] = available[0]
                            print(f"{player.pokemon[0].name.title()} ist jetzt aktiv.")
                        else:
                            print("Alle deine Pokemon sind kampfunfähig. Spiel vorbei.")
                            break
                except Exception as e:
                    print("Fehler beim Zug des Gegners:", e)
            continue

        if a == '2':
            print("Deine Pokemon:")
            print(player)
            try:
                b = int(input('Welches Pokemon (Nummer)? ').strip()) - 1
                if 0 <= b < len(player.pokemon):
                    player.pokemon[0], player.pokemon[b] = player.pokemon[b], player.pokemon[0]
                    print(f"{player.pokemon[0].name.title()} ist jetzt aktiv.")
                else:
                    print("Ungültiger Index.")
            except ValueError:
                print("Ungültige Eingabe.")
            continue

        if a == '3':
            use_bag(player)
            continue

        if a == '4':
            print('Du bist geflohen!')
            break

        print('Unbekannte Eingabe.')


if __name__ == "__main__":
    main()