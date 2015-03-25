def heal(person):
  person.hp += person.max_hp / 10
  if person.hp > person.max_hp:
    person.hp = person.max_hp

def tick(game):
  for person in game.party:
    heal(person)
