class Animal:
  def __init__(self, name, group, number_of_legs, skills):
    self.name = name
    self.group = group
    self.number_of_legs = number_of_legs
    self.skills = skills


cat = Animal('cat', 'mammal', 4, ['meowing', 'hunting', 'zoomies'])
